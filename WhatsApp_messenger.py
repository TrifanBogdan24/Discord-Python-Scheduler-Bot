#!/usr/bin/env python3

# pip3 install pywhatkit
import pywhatkit as kit     # for WhatsApp API

import os

def send_WhatsApp_message(phone_number, message):
    """ sends a Message to WhatsApp
    primeste ca parametru numarul de telefon catre care va fi trimis mesajul
    """
    try:
        # Specify the phone number (with country code) and the message

        # Send the message instantly
        kit.sendwhatmsg_instantly(phone_number, message)

        print(f"WhatsApp message to '{phone_number}' : {message}")

    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")



def main():

    phone_number = os.getenv('MY_PHONE_NUMBER')        # numarul meu

    phone_nr = input('Phone number: ') 
    msg = input('Message: ')
    # send_WhatsApp_message_to_me(msg)
    send_WhatsApp_message(phone_nr, msg)



if __name__ == '__main__':
    main()
