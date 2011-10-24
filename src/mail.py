import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Header import Header

class MailConfig(object):
    def __init__(self, config):
        self.smtp_host = config.smtp_host
        self.smtp_port = config.smtp_port
        self.smtp_local_hostname = config.smtp_local_hostname
        self.smtp_timeout = config.smtp_timeout

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
        
        server.set_debuglevel(1)
        server.sendmail(from_addr, receiver_addr, msg.as_string())
        server.quit()
        
    def _append_header(self, msg, from_addr, receiver_addr, subject, is_multipart = False):
        header_charset = 'ISO-8859-1'
        msg['Subject'] = Header(unicode(subject), header_charset)
        msg['From'] = from_addr
        msg['To'] = receiver_addr
        if is_multipart:
            msg.preamble = 'This is a multi-part message in MIME format.'
        return msg
    
    def _get_plaintext_message(self, from_addr, receiver_addr, subject, body):
        body_charset = self._get_charset(body)
        msg = MIMEText(body.encode(body_charset), 'plain', body_charset)
        msg = self._append_header(msg, from_addr, receiver_addr, subject)
        return msg
        
    def _get_body_as_mimetext(self, body, mime_type):
        charset = self._get_charset(body)
        mime_text = MIMEText(body.encode(charset), mime_type, charset)
        return mime_text
    
    def _get_multipart_message(self, from_addr, receiver_addr, subject, body, body_html):
        msg_root = MIMEMultipart('related')
        msg_root = self._append_header(msg_root, from_addr, receiver_addr, subject, True)  
        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.        
        msg_alternative = MIMEMultipart('alternative')
        msg_root.attach(msg_alternative)
        msg_alternative.attach(self._get_body_as_mimetext(body,'plain'))
        msg_alternative.attach(self._get_body_as_mimetext(body_html,'html'))
        return msg_root
    
    def _get_charset(self, text):
        for charset in 'US-ASCII', 'ISO-8859-1', 'UTF-8':
            try:
                text.encode(charset)
            except UnicodeError:
                pass
            else:
                break
        return charset

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