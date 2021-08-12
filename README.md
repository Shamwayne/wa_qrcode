# Whatsapp Code Reader (Supports both Barcodes and QR Codes Thanks to the power of Pyzbar!)

## What's this all about?

It's a Whatsapp Code Reader bot for Twilio. This is code for a whatsapp bot that can convert any qrcode or barcode image sent to it into text. Useful for quite a few things, for example support automation by taking photos of a product's label and running it through a database instead of asking a user to find the serial number and then looking for it manually.

## Major Dependencies (that some people find tricky)

- Pyzbar: on windows, ```pip install pyzbar``` works fine, but you'll need to also install Visual C++ 13 dlls which can be found on the microsoft site at https://www.microsoft.com/en-US/download/details.aspx?id=40784 (download and run). This is critical because most likely it is not installed on most Windows 10 PC's and will lead to a ```ImportError``` or a ```DecodeError``` and pyzbar will be unable to decode the images for you
- OpenCV: preferably should be pre-installed if an anaconda distribution was used. If not however, should still work fine if pip installed as long as you have Visual C++ 15 distribution installed.
- Numpy: preferably pre-installed if an anaconda distribution was used

