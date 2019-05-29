from ..tasks import asinc_mail


class SendMailNotifications:

    def send_mail(self, list_emails=[], subject='NO SUBJECT', template=None, content_data=None):
        asinc_mail.delay(list_emails, subject, template, content_data)
        return True
