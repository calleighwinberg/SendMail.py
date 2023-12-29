from flask import Flask, request
import re
from marsEmail import get_mars_photo, send_email

#create flask app object
app = Flask(__name__)

#create a route on the app object and select which http method is accepted by the route
@app.route('/email', methods=['POST'])
#email response function will be called when a post request is made
def emailResponse():
    #all parameters found in sendgrids website for incoming requests
    toEmail = request.form['to']
    fromEmail = request.form['from']
    emailContent = request.form['text']

    #error checking will grab the first occurence of a number in the users email. If the number is above 4000, interface
    #will use 1000 instead. Sol days are limited above 4000
    try:
        sol_day = re.search('\d+', emailContent).group()
        img_url, sol_day = get_mars_photo(sol_day)
    except:
        img_url, sol_day = get_mars_photo('1000')
        #solDay = '1000'

    #img_url = getMarsPhoto(solDay)

    send_email(toEmail, fromEmail, img_url, sol_day)

    #we need to return a 200 status code because sendgrid has retry logic
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)