from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import logging
import cv2 as cv
import numpy as np
from pyzbar import pyzbar
import requests



app = Flask(__name__)

@app.route('/')
def test():
    return "OK!"


@app.route("/whatsapp", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    logging.warning(request.values)
    # Start our TwiML response
    # Create response object
    resp = MessagingResponse()
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    if body:
        # Add your response logic to respond to text based requests
        resp.message("receieved request!")
        return str(resp)

    # Chek if media user sent was an image
    media = request.values.get('MediaContentType0', None)
    if 'image' in media:
        img_url = request.values.get('MediaUrl0') # get the url of the image
        img_raw = requests.get(img_url).content
        img_data = np.asarray(bytearray(img_raw), dtype="uint8")
        img = cv.imdecode(img_data, cv.IMREAD_COLOR)
        if img.size > 0:
            res = pyzbar.decode(img)
            try:
                code_data = res[0].data
                code_type = res[0].type
                if code_type != 'QRCODE':
                    code_type = 'BARCODE'
                # Add your response logic here to send a message, here it's just "hello world"
                resp.message(f"Your {code_type} is {code_data}")
            except IndexError:
                resp.message("No Code Detected In Image.")
        else:
            resp.message("Image couldn't be read/parsed")
    else:         
        # Add your response logic here to send a message, here it's just "hello world"
        resp.message("Sorry, could you try sending your message again?")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")