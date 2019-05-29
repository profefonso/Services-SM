import requests
import json


class Sendmail:

    @staticmethod
    def send_mail(mail_list=[], subject='', template='', offender_name='', infraction_id='', date='', location=''):
        url = 'http://mail:8002/notification/'
        data = {
            "mail_list": mail_list,
            "subject": subject,
            "template": template,
            "content_data": {
                "offender_name": offender_name,
                "infraction_id": infraction_id,
                "date": date,
                "location": location
            }
        }

        data_send = json.dumps(data, ensure_ascii=False)
        r = requests.post(url, data=data_send)
        result = r.json()
        print(result)
        if result['data']['mail'] == 'OK':
            return True
        else:
            return False
