import random
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_PYTHON'))

apiNASA = os.environ.get('NASA_API')

urlNASAapod = 'https://api.nasa.gov/planetary/apod'

urlNASA = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

'''
This function takes in a date as a string and returns NASA photo of the day for that date.
Uses requests to send a request to the APOD NASA api with my api key and the date as parameters. 
There is error catching logic to catch sol days that are out of bounds. 
:param sol: string for requested date
:return: The date, photo http, photo title, photo description, and media tpye (not always a photo)
'''
def get_photo_of_day(date):

    params = {'date': date, 'api_key': apiNASA}
    #send a GET request to the nasa apod url with given params
    response = requests.get(urlNASAapod, params)
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


'''
This function takes in a mars sol day as a string and return a random photo taken by the mars rover on that sol.
Sends a request to the mars rover NASA api with my api key and the sol date as parameters. There is error catching 
logic to catch sol days that are out of bounds.
:param sol: string for the sol day that 
:return: The sol day used and the http string for the photo
'''
def get_mars_photo(sol):

    sol_int = int(sol)
    if (sol_int > 4000):
        sol = '1000'

    sol_picture = False

    while not sol_picture:
        params = {'sol': sol, 'api_key': apiNASA}
        # send a GET request to the nasa mars rover url with given params
        response = requests.get(urlNASA, params)
        if (response.status_code != 200):
            print("Error")
            return response.text

        data = response.json()
        photos = data['photos']

        #error checking for the given sol. Sometimes a camera is inactive for a few days so there are no photos.
        if len(photos) == 0:
            sol_int = int(sol)
            sol_int +=1
            sol = str(sol_int)
        else:
            sol_picture = True

    photoHTML = random.choice(photos)['img_src']

    return photoHTML, sol


'''
This function takes in email parameters and makes use of sendgrid's Mail class to send an email with the given data.
Using my personal sendgrid api to make a post request that sends an email
:param sol: from_email, to_email, img_url, sol_day will be received from flask file
:return: status code or error
'''
def send_email(from_email, to_email, img_url, sol_day):
    mail = Mail(from_email, to_email, subject="Here is your Mars Rover Photo!",
                html_content='<strong>Check out this Mars picture from Curiosity\'s 'f'{sol_day} sol exploring Mars. </strong> <br> <img src="{img_url}"></img>')

    try:
        # Get a JSON-ready representation of the Mail object
        mailJSON = mail.get()
        # Send an HTTP POST request to mail.send.post
        response = sg.client.mail.send.post(request_body=mailJSON)
        print(response.status_code)
        print(response.headers)
        return response.status_code

    except Exception:
        return 'error'



#testing params
fromEmail = "mars@calleighwinberg.courses"
#toEmail = "calleigh@seas.upenn.edu"
toEmail = "calleighlife@gmail.com"
img_url, sol = get_mars_photo('4001')
#send_email(fromEmail, toEmail, img_url, sol)
