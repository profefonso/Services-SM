import requests


class Sendmail:

    @staticmethod
    def send_mail(subject='', template='', offender_name='', infraction_id='', date='', location=''):
        url = 'http://localhost:8002/notification/'
        data = {
            "mail_list": ["alfonsocarop@gmail.com", "alfonsocaro18@hotmail.com"],
            "subject": subject,
            "template": template,
            "content_data": {
                "offender_name": offender_name,
                "infraction_id": infraction_id,
                "date": date,
                "location": location
            }
        }
        r = requests.post(url, data=data)
        result = r.json()
        print(result)
        if result['data']['mail'] == 'OK':
            return True
        else:
            return False
