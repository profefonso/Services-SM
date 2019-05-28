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

        ''' message = '<h2>Multa de Transito N0: ' + str(numquote) + \
                  '</h2></br><p>Estimado proveedor se ha creado una nueva cotizacion para el cliente ' + client_name + \
                  '</p></br><p>Ingrese a la plataforma o cree su Oferta a traves de los servicios disponibles</p>' + \
                  '<br><h3>MERCA DIGITAL SA</h3>'
                  
                  
            subject =  'Multa de Transito - Simit Services'
        '''

        if 'mail_list' in body and 'subject' in body and 'content_html' in body:

            try:
                sendmailnotification = SendMailNotifications()
                sendmailnotification.send_mail(
                    list_emails=body['mail_list'],
                    subject=body['subject'],
                    content_xml=body['content_html']
                )

                return Response(
                        {'data': {'mail': 'OK'}},
                        status=status.HTTP_200_OK
                    )
            except:
                return Response(
                    {'data': {'error': 'Message Don´t Send'}},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        else:
            return Response(
                {'message': 'invalid message'},
                status=status.HTTP_400_BAD_REQUEST
            )
