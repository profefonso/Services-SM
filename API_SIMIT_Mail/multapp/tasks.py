from API_SIMIT_Mail.simit_services.celery import app

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@app.task
def asinc_mail(list_emails=[], subject='NO SUBJECT', template=None, content_data=None):
    sender = "SIMIT SERVICES <infomercadigital@gmail.com>"

    merge_data = content_data
    text_body = render_to_string("../templates/"+template+".txt", merge_data)
    html_body = render_to_string("../templates/"+template+".html", merge_data)

    msg = EmailMultiAlternatives(subject=subject, from_email=sender,
                                 to=list_emails, body=text_body)
    msg.attach_alternative(html_body, "text/html")
    msg.send()
