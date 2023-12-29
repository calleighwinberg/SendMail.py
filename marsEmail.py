import random
import requests
import sendgrid
from sendgrid.helpers.mail import Mail
import os

#sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_PY'))
sg = sendgrid.SendGridAPIClient('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')

#apiNASA = os.environ.get('NASA_API')
apiNASA = 'k0y6BcPxBWVadmOUKOdlFYU6vFaNy9rbdGPWPaS0'

urlNASAapod = 'https://api.nasa.gov/planetary/apod'

urlNASA = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'


def get_photo_of_day(date):

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
    media_type = data['media_type']

    return [photo, title, explanation, media_type]

#lst = get_photo_of_day('2023-12-11')
#print(len(lst))
#print(lst[1])
#print(lst[2])
#print(lst[3])

def get_mars_photo(sol):

    sol_picture = False

    while not sol_picture:
        params = {'sol': sol, 'api_key': apiNASA}
        response = requests.get(urlNASA, params)
        if (response.status_code != 200):
            print("Error")
            return response.text

        data = response.json()
        photos = data['photos']
        #print(photos)
        #error checking for the given sol. Sometimes a camera is inactive for a few days so there are no photos.
        if len(photos) == 0:
            int_sol = int(sol)
            int_sol +=1
            sol = str(int_sol)
        else:
            sol_picture = True

    #print(photos)
    photoHTML = random.choice(photos)['img_src']

    print(photoHTML)

    return photoHTML


'''
this method sends the email
'''
def send_email(fromEmail, toEmail, img_url):
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
img_url = get_mars_photo('2300')
print(type(img_url))
#content = '<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

#send_email(fromEmail, toEmail, img_url)

#making new  change here
