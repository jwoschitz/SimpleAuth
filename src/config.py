import os.path
from ConfigParser import SafeConfigParser, ParsingError, MissingSectionHeaderError
from exception import Error

class FileParseError(Error):
    def __init__(self, file_path):
        super(self.__class__, self).__init__("Could not parse config file '{0}'".format(file_path))
        
class FileNotExistsError(Error):
    def __init__(self, file_path):
        super(self.__class__, self).__init__("Config file '{0}' does not exist.".format(file_path))   

class SectionMissingError(Error):
    def __init__(self, section_name, file_path):
        super(self.__class__, self).__init__("Config section '{0}' is missing in config file '{1}'".format(section_name, file_path))

class MandatoryOptionMissingError(Error):
    def __init__(self, option_name):
        super(self.__class__, self).__init__("Config option '{0}' is mandatory and seems to be missing.".format(option_name))
        
class _ConfigItem(object):
    def __init__(self, name, default_value = None, is_mandatory = False, convert_func = None):
        self.name = name
        self.default_value = default_value
        self.is_mandatory = is_mandatory
        self.convert_func = convert_func
	
class Config(object):
    CONFIG_SECTION_NAME = 'auth'
    
    _config_items = [
        _ConfigItem('db_host', 'localhost'),
        _ConfigItem('db_user', None, True),
        _ConfigItem('db_password', None, True),
        _ConfigItem('db_catalog', None, True),
        _ConfigItem('smtp_host', 'localhost'),
        _ConfigItem('smtp_port', 25, False, lambda val: int(val)),
        _ConfigItem('smtp_local_hostname'),
        _ConfigItem('smtp_timeout'),
        _ConfigItem('smtp_use_ttls'),
        _ConfigItem('smtp_user'),
        _ConfigItem('smtp_password'),
        _ConfigItem('mail_from', 'webmaster@your-site.com'),
        _ConfigItem('mail_subject', 'Welcome to Website - Please confirm your email address'),
        _ConfigItem('mail_body', 'Please go to http://your-site.com/?activate_email={ACTIVATION_TOKEN} to activate your email address.'),
        _ConfigItem('mail_body_html', None),
        _ConfigItem('mail_activation_expire', 86400, False, lambda val: int(val)),
        _ConfigItem('password_min_length', 8, False, lambda val: int(val)),
        _ConfigItem('login_max_attempts', 5, False, lambda val: int(val)),
        _ConfigItem('login_attempt_expire', 43200, False, lambda val: int(val))        
    ]   
    
    def __init__(self, file_path_to_config = None):
        if not file_path_to_config:
            self._create_default_config()
        else:
            self._create_config_from_file(file_path_to_config)
        
    def _create_default_config(self):
        for item in self._config_items:
            setattr(self, item.name, item.default_value)            
    
    def _create_config_from_file(self, file_path_to_config):
        parser = self._get_initialized_config_parser(file_path_to_config)
        for item in self._config_items:
            value = self._get_value_from_config(parser, item)
            if item.convert_func:
                value = item.convert_func(value)
            setattr(self, item.name, value)
        
    def _get_initialized_config_parser(self, file_path_to_config):
        if not os.path.isfile(file_path_to_config):
            raise FileNotExistsError(file_path_to_config)
        parser = SafeConfigParser()
        try:
            parser.read(file_path_to_config)
            if not parser.has_section(self.CONFIG_SECTION_NAME):
                raise SectionMissingError(self.CONFIG_SECTION_NAME, file_path_to_config)
            return parser
        except MissingSectionHeaderError:
            raise SectionMissingError(self.CONFIG_SECTION_NAME, file_path_to_config)
        except ParsingError:  
            raise FileParseError(file_path_to_config)

    
    def _get_value_from_config(self, parser, item):
        if parser.has_option(self.CONFIG_SECTION_NAME, item.name):
            return parser.get(self.CONFIG_SECTION_NAME, item.name)            
        if item.is_mandatory:
            raise MandatoryOptionMissingError(item.name)
        return item.default_value