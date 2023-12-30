import random
import requests
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_PYTHON'))

apiNASA = os.environ.get('NASA_API')

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

    sol_int = int(sol)
    if (sol_int > 4000):
        sol = '1000'

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
            sol_int = int(sol)
            sol_int +=1
            sol = str(sol_int)
        else:
            sol_picture = True

    #print(photos)
    photoHTML = random.choice(photos)['img_src']

    #print(photoHTML)

    return photoHTML, sol


'''
this method sends the email
'''
def send_email(fromEmail, toEmail, img_url, sol_day):
    mail = Mail(fromEmail, toEmail, subject="Here is your Mars Rover Photo!",
                html_content='<strong>Check out this Mars picture from Curiosity\'s 'f'{sol_day} sol exploring Mars. </strong> <br> <img src="{img_url}"></img>')

    try:
        # Get a JSON-ready representation of the Mail object
        mailJSON = mail.get()
        print(mailJSON)
        print(sg.client.mail.send.post(request_body=mailJSON))
        # Send an HTTP POST request to mail.send.post
        response = sg.client.mail.send.post(request_body=mailJSON)
        print(response)
        print(response.status_code)
        print(response.headers)
        return response.status_code

    except Exception:
        #print(response.status_code)
        return 'error'



#these are the params that can be changed. Maybe put in a different file
fromEmail = "mars@calleighwinberg.courses"
toEmail = "calleighwinberg@gmail.com"
#subject = "Here is your Mars Rover Photo!"
img_url, sol = get_mars_photo('2344')
print('img url ', img_url)
#print(sol)
#content = '<strong>Check out this Mars pic</strong><br>'f'<img src="{img_url}"></img>')

send_email(fromEmail, toEmail, img_url, sol)
