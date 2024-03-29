import os

from flask_interface import app
import re
from mars_email import get_mars_photo, send_email

if __name__ == '__main__':
    app.run()