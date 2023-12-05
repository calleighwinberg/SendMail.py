import random
import requests
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

sg = sendgrid.SendGridAPIClient(api_key='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')

apiNASA = 'dXIgIS03gugAFnz3mfdOUlLVkwS8iTRxqBx23xht'
urlNASA = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def getMarsPhoto(sol):
    params = {'sol': sol, 'api_key': apiNASA}
    response = requests.get(urlNASA, params)
    if (response.status_code != 200):
        print("Error")
        return []

    data = response.json()
    photos = data['photos']

    photoHTML = random.choice(photos)['img_src']

    return photoHTML


'''
'''
def sendEmail(fromEmail, toEmail, subject, img_url):
    mail = Mail(fromEmail, toEmail, subject, html_content='<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)


fromEmail = "calleigh@seas.upenn.edu"  # Change to your verified sender
toEmail = "calleighwinberg@gmail.com"  # Change to your recipient
subject = "Daily Mars Photo"
img_url = getMarsPhoto('1000')
#content = '<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

sendEmail(fromEmail, toEmail, subject, img_url)
