class Error(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
		print "", self.msg
        
class ModuleNotConfiguredError(Error):
    def __init__(self, module_name):
        super(self.__class__, self).__init__("Module '{0}' contains no valid configuration. Set configuration before instantiation.".format(module_name))

class PropertyNotSetError(Error):
    def __init__(self, property_name):
        super(self.__class__, self).__init__("Property '{0}' has no valid value.".format(property_name))