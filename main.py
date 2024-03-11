#!/usr/bin/env python3

# pip install pywhatkit
import pywhatkit as kit

import discord
import asyncio
import json

import os

from datetime import datetime


def send_WhatsApp_message(message):
    try:
        # Specify the phone number (with country code) and the message
        phone_number = os.getenv('MY_PHONE_NUMBER')        # numarul meu

        # Send the message instantly
        kit.sendwhatmsg_instantly(phone_number, message)
    
        print(f"WhatsApp message to '{phone_number}' : {message}")

    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")




def get_msg():
    dt = datetime.now()
    h_m = dt.strftime('%H:%M')
    day = dt.isoweekday()       # ziua saptamanii


    msg = ""


    if day == 1 and h_m == "00:00":
        week_parity = 1 - week_parity


    if day == 1 and h_m == "07:00":
        msg = "Buna dimineata!"


    if day == 1 and (h_m == "09:50" or h_m == "10:00"):
        msg = "Lab de PCOM, 10:00 - 12:00, sala EG 205"

    if day == 1 and (h_m == "11:50" or h_m == "12:00"):
        if week_parity == 1:
            msg = "Curs de PCOM 12:00 - 14:00, sala PR 001"
        else:
            pass
    
    if day == 1 and (h_m == "13:50" or h_m == "14:00"):
        if week_parity == 0:
            msg = "Curs de SOC (OBLIGATORIU), 14:00 - 16:00, sala PR 001"
        else:
            msg = "Curs de ED, 14:00 - 16:00, sala PR 001"

    
    if day == 1 and (h_m == "15:50" or h_m == "16:00"):
        msg = "Curs de ELTH 16:00 - 18:00, sala AN 030"
    

    if day == 2 and h_m == "05:00":
        msg = "Buna dimineata!"

    if day == 2 and (h_m == "07:50" or h_m == "08:00"):
        msg = "Curs ED, 8:00 - 10:00, sala PR 001"

    if day == 2 and (h_m == "08:50" or h_m == "10:00"):
        msg = "Curs SOC (OBLIGATORIU), 10:00 - 12:00, sala PR 001"

    if day == 2 and (h_m == "11:50" or h_m == "12:00"):
        if week_parity == 1:
            msg = "Curs PP (OBLIGATORIU), 12:00 - 14:00, sala PR 001"
        else:
            pass
        
    if day == 2 and (h_m == "15:50" or h_m == "16:00"):
        msg = "Curs PA, 16:00 - 18:00, sala EC 004"

    if day == 3 and h_m == "07:00":
        msg = "Buna dimineata!"


    if day == 3 and (h_m == "09:50" or h_m == "10:00"):
        msg = "Curs PCOM, 10:00 - 12:00, sala PR 001"

    if day == 3 and (h_m == "11:50" or "12:00"):
        msg = "Curs PP (OBLIGATORIU), 12:00 - 14:00, sala PR 001"

    if day == 3 and (h_m == "15:50" or h_m == "16:00"):
        if week_parity == 1:
            msg = "Seminar ED (impar), 16:00 - 18:00, sala EG 303"
        else:
            pass
    
    if day == 3 and (h_m == "17:50" or h_m == "18:00"):
        if week_parity == 1:
            msg = "Curs PCT (impar), 18:00 - 20:00, sala A04 LEU"
        else:
            pass


    if day == 4 and h_m == "05:00":
        msg = "Buna dimineata"

    if day == 4 and (h_m == "07:50" or h_m == "08:00"):
        if week_parity == 1:
            msg = "lab ELTH (impar), 8:00 - 10:00, sala EB 206, EB 207"
        else:
            msg = "seminar ELTH (par), 8:00 - 10:00, sala PR 001"

    if day == 4 and (h_m == "11:50" or h_m == "12:00"):
        if week_parity == 1:
            msg = "Lab SOC (impar), 12:00 - 14:00, sala ED 220"
        else:
            pass

    if day == 4 and (h_m == "13:50" or h_m == "14:00"):
        if week_parity == 1:
            msg = "Lab SOC (impar), 14:00 - 16:00, sala ED 220"
        else:
            pass

    if day == 4 and (h_m == "15:50" or h_m == "16:00"):
        if week_parity == 1:
            msg = "Lab SOC (impar), 16:00 - 18:00, sala ED 220"
        else:
            pass


    if day == 5 and h_m == "07:00":
        msg = "Buna dimineata"

    if day == 5 and (h_m == "09:50" or h_m == "10:00"):
        if week_parity == 1:
            msg = "sport (impar)"
        else:
            pass

    if day == 5 and (h_m == "11:50" or h_m == "12:00"):
        msg = "Lab PA, 12:00 - 14:00, sala EG 405"


    if day == 5 and (h_m == "13:50" or h_m == "14:00"):
        msg = "Lab PA, 14:00 - 16:00, sala EG 103 b"


    if h_m == "21:00":
        msg = "Noapte buna!"


    if msg != "":
        send_WhatsApp_message(msg)


    return msg


def get_min(h_m):
    (hour, minute) = h_m.split(':')
    print(f"{hour}   {minute}")



def main():
    global week_parity
    week_parity = 0

    # Replace 'YOUR_TOKEN' with your Discord bot token
    TOKEN = ''
    GUILD_ID = ''  # Replace with your server ID
    CHANNEL_ID = ''  # Replace with your channel ID

    with open('discord_authentification_keys.json', 'r') as file:
        data = json.load(file)

    TOKEN = os.getenv('MY_DISCORD_MESSENGER_BOT_TOKEN')
    GUILD_ID = os.getenv('MY_DISCORD_SERVER_ID')
    CHANNEL_ID = os.getenv('MY_DISCORD_CHANNEL_ID')
    
    MY_USERNAME = os.getenv('MY_DISCORD_USERNAME')
    TARGET_USER_ID = os.getenv('MY_DISCORD_USER_ID')             # eu: Bogdan24


    file.close()

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

        # first message
        welcome_message = "Hello, I'm your bot! I am now online and ready to assist."
        await send_discord_message(welcome_message)



        # Set up the task to send the current time every minute
        await send_discord_message_task()





    @client.event
    async def on_message(message):
        # Display the message content in the terminal
        print(f"Message from {message.author}: {message.content}")



    async def send_discord_message(msg_content):
        channel = client.get_channel(int(CHANNEL_ID))
        await channel.send(f'<@{TARGET_USER_ID}> {msg_content}')


    async def send_discord_message_task():
        await client.wait_until_ready()
        channel = client.get_channel(int(CHANNEL_ID))
        guild = discord.utils.get(client.guilds, id=int(GUILD_ID))


        while not client.is_closed():
            message = ''
            message = get_msg()


            if message == '':
                current_time = datetime.now().strftime('%H:%M')
                message = f'Current time: {current_time}\nNothing for now'


            # Send the current time to the specified channel
            await channel.send(f"<@{TARGET_USER_ID}> {message}")




            # another message can be sent after 60 seconds
            await asyncio.sleep(60)




    # Run the bot
    client.run(TOKEN)




if __name__ == '__main__':
    main()

