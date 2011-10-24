import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Header import Header
from email import Charset

class MailConfig(object):
    def __init__(self, config):
        self.smtp_host = config.smtp_host
        self.smtp_port = config.smtp_port
        self.smtp_local_hostname = config.smtp_local_hostname
        self.smtp_timeout = config.smtp_timeout
        self.smtp_use_ttls = config.smtp_use_ttls
        self.smtp_user = config.smtp_user
        self.smtp_password = config.smtp_password

class MailDispatcher(object):
    def __init__(self, mail_config):
        self.config = mail_config
        
    def send_mail(self, from_addr, receiver_addr, subject, body, body_html = None):
        server = smtplib.SMTP(
            self.config.smtp_host, 
            self.config.smtp_port, 
            self.config.smtp_local_hostname, 
            self.config.smtp_timeout
        )
        
        if body_html:
            msg = self._get_multipart_message(from_addr, receiver_addr, subject, body, body_html)
        else:
            msg = self._get_plaintext_message(from_addr, receiver_addr, subject, body)
        
        if(self.config.smtp_use_ttls):
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.config.smtp_user,self.config.smtp_password)
        
        server.set_debuglevel(1)
        server.sendmail(from_addr, receiver_addr, msg.as_string())
        server.quit()
        
    def _append_header(self, msg, from_addr, receiver_addr, subject, is_multipart = False):
        #header_charset = 'ISO-8859-1'
        #msg['Subject'] = Header(unicode(subject), header_charset)
        msg['Subject'] = Header(subject.encode('utf-8'), 'UTF-8').encode()
        msg['From'] = from_addr
        msg['To'] = receiver_addr
        if is_multipart:
            msg.preamble = 'This is a multi-part message in MIME format.'
        return msg
    
    def _get_plaintext_message(self, from_addr, receiver_addr, subject, body):
        msg = self._get_body_as_mimetext(body,'plain')
        msg = self._append_header(msg, from_addr, receiver_addr, subject)
        return msg
        
    def _get_body_as_mimetext(self, body, mime_type):
        Charset.add_charset('utf-8', Charset.QP, Charset.QP, 'utf-8')
        mime_text = MIMEText(body.encode('utf-8'), mime_type, 'UTF-8')
        return mime_text
    
    def _get_multipart_message(self, from_addr, receiver_addr, subject, body, body_html):
        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.        
        msg = MIMEMultipart('alternative')
        msg = self._append_header(msg, from_addr, receiver_addr, subject, True)  
        msg.attach(self._get_body_as_mimetext(body,'plain'))
        msg.attach(self._get_body_as_mimetext(body_html,'html'))
        return msg
        
class TemplateMailDispatcher(MailDispatcher):
    def __init__(self, mail_config, template, html_template = None):
        super(self.__class__, self).__init__(mail_config)
        self.template = template
        self.html_template = html_template
        
    def send_mail(self, from_addr, receiver_addr, subject, template_fill_args_dictionary):
        msg = self._get_filled_template(self.template, template_fill_args_dictionary)
        if self.html_template:
            msg_html = self._get_filled_template(self.html_template, template_fill_args_dictionary)
        else:
            msg_html = None
        super(self.__class__, self).send_mail(from_addr, receiver_addr, subject, msg, msg_html)
        
    def _get_filled_template(self, template, template_fill_args_dictionary):
        prepared_template = template
        for key, value in template_fill_args_dictionary.items():
            prepared_template = prepared_template.replace(key, value)
        return prepared_template