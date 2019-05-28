from django.core.mail import EmailMessage


class SendMailNotifications:

    def send_mail(self, list_emails=[], subject='NO SUBJECT', content_xml=None):

        sender = "SIMIT SERVICES <infomercadigital@gmail.com>"

        msg = EmailMessage(subject, content_xml, sender, list_emails)
        msg.content_subtype = "html"
        msg.send()
