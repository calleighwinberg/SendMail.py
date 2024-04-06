# Exploring Space Using NASA APIs

This application aims to streamline space exploration and education by providing a user-friendly platform to explore NASA's public APIs. Users can search for a specific NASA
Picture Of The Day or request a random Mars photo from NASA's largest and most capable Mars rover, Curiosity. 

<img width="945" alt="Screenshot 2023-12-30 at 7 20 48 PM" src="https://github.com/calleighwinberg/SendMail.py/assets/149536156/670f3472-c35d-44ef-b4f5-c4dd1590cbe0">


## Description

NASA has been producing their Astronomy picture of the day since June 16, 1995. NASA's official picture of the day website can be found at https://apod.nasa.gov/apod/astropix.html. 
This application aims to build an alternative resource that allows users to to choose a particular date and display the corresponding photo or video from NASA's picture of the day API. The app also taps into NASA's extensive collection of Mars Rover images by allowing users to receive emailed mars photos at random. When a user sends an email to 'mars@calleighwinberg@courses.com', they receive a randomly chosen photo that offers a fresh perspective and diverse glimpse into the Martian landscape. 

## Getting Started

### Built with
* Python
* Flask
* Streamlit
* Render deployment

### Dependencies

* Python 3
* Flask as a webframe for receiving HTTP requests.
* A free sendgrid account.
* A domain in which you can receive emails.
* Ngrok for testing 
* Streamlit to create and deploy your applciation UI.

### Installing

1. Clone the repository. 
   ```
   git clone https://github.com/calleighwinberg/SendMail.py.git
   ```
2. Install the sendgrid Python helper library in your virtual environment.
    ```
   pip install sendgrid
   ```
3. Install Flask in your virtual environment.
  ```
 pip install Flask
 ```
4. Install streamlit in your virtual environment.
  ```
 pip install streamlit
 ```
5. Install ngrok in your virtual environment.
  ```
 brew install ngrok/ngrok/ngrok
 ```
6. Install guinicorn in your virtual environment.
  ```
 pip install gunicorn
 ```
7. After creating your sendgrid account, create a sendgrid API key and save it in a environment variable named "SENDGRID_API_PYTHON"
8. Generate a free NASA API key here - https://api.nasa.gov/. Save your API key in an environment variable named "NASA_API"


### Executing program

Steps for sending and receiving Mars photos using ngrok
1. To test your app before deployment, run your flask_interface.py in the terminal. With the flask_interface.py file running, open the ngrok tunnel in a seperate terminal.
```
ngrok http 5000
```
2. Now that you have a publicly accessible URL, configure the Sendgrid Inbound Parse webhook in your SendGrid dashboard. This is where need a domain name that can recieve emails.
3. Enter the ngrok generated pulic URL with '/email' at the end.

Steps for deploying your app to send and receive Mars photos
1. Follow the steps to successfully deploy the app on render - https://docs.render.com/deploy-flask
2. Follow the same process above to configure the Sendgrid Inbound Parse webhook in your SendGrid dashboard.
3. You can now send emails.

<img width="445" alt="Screenshot 2023-12-30 at 7 20 48 PM" src="https://github.com/calleighwinberg/SendMail.py/assets/149536156/c56745a8-de91-49ad-a336-101933635af6">

Steps for executing Streamlit app.
1. To deploy your streamlit app for production, follow instructions here - https://docs.streamlit.io/streamlit-community-cloud/get-started. 

## Help

1. Make sure to add environment variables to your 'secrets' when deploying your streamlit app.
2. The ngrok tunnel url will reset everytime ngrok is stopped or restarted, so you will need to update the imbound parse URL in SendGrid.
3. Activate your virtual environment before installing or upgrading any dependencies or packages or there may be unintentional effects on other packages. 
```
source venv/bin/activate
```

## Useful Links
* NASA APIs - https://api.nasa.gov/
* SendGrid - https://app.sendgrid.com/

## Author

Calleigh Winberg


