import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from multapp.utility.notification import SendMailNotifications


class NotificationServicesRest(APIView):
    name = 'notification_service'

    '''
        {
            "mail_list": ["mail@domain.com", "other_mail@domail.com"],
            "subject": "Notification Fake",
            "content_html": "<h1>Content Mail</h1>"
        }
    '''

    def post(self, request, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        ''' 
        {
            "mail_list": ["user@domain.com", "user_two@domain2.com"],
            "subject": "Notification Fake",
            "template": "infraction_mail",
            "content_data": {
                "offender_name":"Gonzalito",
                "infraction_id": "34",
                "date":"12-12-12",
                "location":"Bogota"
            }
        }
        '''

        if 'mail_list' in body and 'subject' in body and 'template' in body and 'content_data' in body:

            try:
                sendmailnotification = SendMailNotifications()
                sendmailnotification.send_mail(
                    list_emails=body['mail_list'],
                    subject=body['subject'],
                    template=body['template'],
                    content_data=body['content_data']
                )

                return Response(
                    {'data': {'mail': 'OK'}},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                print(e)
                return Response(
                    {'data': {'error': 'Message Don´t Send'}},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        else:
            return Response(
                {'message': 'invalid message'},
                status=status.HTTP_400_BAD_REQUEST
            )
