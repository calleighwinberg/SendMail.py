import requests
import sendgrid
from sendgrid.helpers.mail import Mail
import os

apiNASAapod = '2vgBDamI9RzdXai3bjYyNMdUQKHmkQlgcajHhC5W'

urlNASAapod = 'https://api.nasa.gov/planetary/apod'

def getPhotoOfDay(date):

    params = {'date': date, 'api_key': apiNASAapod}
    response = requests.get(urlNASAapod, params)
    print(response.status_code)
    if (response.status_code != 200):
        print("Error")
        return []

    data = response.json()
    photo = data['url']

    #photoHTML = random.choice(photos)['img_src']

    print(photo)

    return photo


getPhotoOfDay('2023-12-12')