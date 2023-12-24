import random
import requests
import sendgrid
from sendgrid.helpers.mail import Mail
import os
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context #not sure what this line does but it was needed

sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_PY'))
#sg = sendgrid.SendGridAPIClient('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')

apiNASA = os.environ.get('NASA_API')
#apiNASA = 'dXIgIS03gugAFnz3mfdOUlLVkwS8iTRxqBx23xht'
#print(apiNASA)
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

    print(photoHTML)

    return photoHTML


'''
this method sends the email
'''
def sendEmail(fromEmail, toEmail, subject, img_url):
    mail = Mail(fromEmail, toEmail, subject, html_content='<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

    # Get a JSON-ready representation of the Mail object
    mailJSON = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mailJSON)
    print(response.status_code)
    print(response.headers)

#these are the params that can be changed. Maybe put in a different file
fromEmail = "calleigh@seas.upenn.edu"
toEmail = "calleighwinberg@gmail.com"
subject = "Daily Mars Photo"
img_url = getMarsPhoto('1000')
#content = '<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

sendEmail(fromEmail, toEmail, subject, img_url)

#making new  change here
