import random
import requests
import sendgrid
from sendgrid.helpers.mail import Mail
import os

#sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_PY'))
sg = sendgrid.SendGridAPIClient('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')

#apiNASA = os.environ.get('NASA_API')
apiNASA = '2vgBDamI9RzdXai3bjYyNMdUQKHmkQlgcajHhC5W'

urlNASAapod = 'https://api.nasa.gov/planetary/apod'

urlNASA = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


def getPhotoOfDay(date):

    params = {'date': date, 'api_key': apiNASA}
    response = requests.get(urlNASAapod, params)
    #print(response.status_code)
    if (response.status_code != 200):
        print("Error")
        print(response.text)
        return response.text

    data = response.json()
    photo = data['url']
    title = data['title']
    explanation = data['explanation']
    print(photo)
    print(title)
    print(explanation)

    return photo, title, explanation

getPhotoOfDay('2023/12/12')
#print(a)
#print(b)
#print(c)

def getMarsPhoto(sol):

    params = {'sol': sol, 'api_key': apiNASA}
    response = requests.get(urlNASA, params)
    if (response.status_code != 200):
        print("Error")
        return response.text

    data = response.json()
    photos = data['photos']

    photoHTML = random.choice(photos)['img_src']

    print(photoHTML)

    return photoHTML


'''
this method sends the email
'''
def sendEmail(fromEmail, toEmail, img_url):
    mail = Mail(fromEmail, toEmail, subject="Here is your Mars Rover Photo!",
                html_content='<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

    # Get a JSON-ready representation of the Mail object
    mailJSON = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mailJSON)
    print(response.status_code)
    print(response.headers)

#these are the params that can be changed. Maybe put in a different file
fromEmail = "calleigh@seas.upenn.edu"
toEmail = "calleighwinberg@gmail.com"
#subject = "Here is your Mars Rover Photo!"
img_url = getMarsPhoto('1000')
#content = '<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

#sendEmail(fromEmail, toEmail, img_url)

#making new  change here
