#!/usr/bin/env python3

# pip3 install discord
import discord              # for Discord API
import asyncio
import json

import os, sys

from datetime import datetime

# structures
from data_structures import WeeklyActivity
from data_structures import OtherActivity

# functions
from data_structures import get_timestamp
from data_structures import get_h_m
from data_structures import get_day_idx
from data_structures import get_day_str

# global variables
from data_structures import week_parity_code   # 0, 1, None
from data_structures import is_holiday         # False, True
from data_structures import weekly_activities
from data_structures import other_activities
from data_structures import deadlines




def get_msg():
    """ obtine un mesaj sugestiv pentru a fi trimis in functie de ora curenta
    """
    dt = datetime.now()
    h_m = dt.strftime('%H:%M')
    day = dt.isoweekday()       # ziua saptamanii (index, numar de 1-7)

    timestamp_now = get_timestamp(h_m)
    ten_min_timestamp = get_timestamp("00:10")

    msg = ''

    

    for activ in weekly_activities:
        print(f"{activ}")
        if activ.is_next_in_schedule() == True:
            msg += f"Next: {activ}"
        if activ.is_current_in_schedule() == True:
            msg += f"Now: {activ}"




    # if msg != '':
    #     send_WhatsApp_message(msg)


    return msg



def append_not_none(l, el):
    if type(l) != list:
        pass

    if el is not None:
        l.append(el)


def get_min(h_m):
    (hour, minute) = h_m.split(':')

    print(f"{hour}   {minute}")
    
    return (hour, minute)



def hardcode_schedule():

    # `global` specifica interpretorului sa nu defineasca variabilele acestea in functie
    # ci sa foloseasca variabilele globale care poarte aceste nume
    global week_parity
    global is_holiday
    global weekly_activities
    global other_activities
    global deadlines

    week_parity_code = 1        # 0, 1
    is_holiday = False          # False, True
    weekly_activities = []
    other_activities = []
    deadlines = []


    # WeeklyActivity('name', 'location', 'descritption', 'day', 'start_time_h_m', 'stop_time_h_m', 'week_parity)
    # luni:
    new_activ = WeeklyActivity.new('Lab PCOM', 'sala EG 205', '-', 'luni', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Curs SOC', 'sala PR 001', 'obligatoriu', 'luni', '12:00', '14:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_acitv = WeeklyActivity.new('Curs PCOM', 'sala PR 001', '-', 'luni', '14:00', '16:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Curs ED', 'sala PR 001', '-', 'luni', '14:00', '16:00', 'par')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Curs ELTH CA', 'sala AN 030', 'la seria CA', 'luni', '16:00', '18:00', '-')
    append_not_none(weekly_activities, new_activ)
    # marti:
    new_activ = WeeklyActivity.new('Curs ED', 'sala PR 001', '-', 'marti', '8:00', '10:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Curs SOC', 'sala PR 001', 'obligatoriu', 'marti', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Curs PA', 'sala EC 004', '-', 'marti', '16:00', '18:00', '-')
    append_not_none(weekly_activities, new_activ)
    # miercuri:
    new_activ = WeeklyActivity.new('seminar PCT', 'sala PR 106', '', 'miercuri', '8:00', '10:00', 'par')
    append_not_none(weekly_activities, new_activ)
    new_acitv = WeeklyActivity.new('Curs PCOM', 'sala PR 001', '-', 'miercuri', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Curs PP', 'sala PR 001', 'obligatoriu', 'miercuri', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('seminar ED', 'sala EG 303', '-', 'miercuri', '16:00', '18:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_acitv = WeeklyActivity.new('Curs PCT', 'sala A04 LEU', 'optional', 'miercuri', '18:00', '20:00', 'par')
    append_not_none(weekly_activities, new_activ)
    # joi:
    new_activ = WeeklyActivity.new('Lab SOC', 'sala ED 220', '-', 'joi', '12:00', '14:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Lab SOC', 'sala ED 220', '-', 'joi', '14:00', '16:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Lab ED', 'sala ED 314', '-', 'joi', '16:00', '18:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    # vineri:
    new_activ = WeeklyActivity.new('sport (impar)', 'sala de sport', '-', 'vineri', '8:00', '10:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Lab PA', 'sala EG 405', '-', 'vineri', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity.new('Lab PP', 'sala EG 103 b', '-', 'vineri', '12:00', '14:00', '-')
    append_not_none(weekly_activities, new_activ)



def init_reset_schedule():
    """ reseteaza tot orarul la o varianta care nu contine nimic
    """

    # `global` specifica interpretorului sa nu defineasca variabilele acestea in functie
    # ci sa foloseasca variabilele globale care poarta aceste nume
    global week_parity
    global is_holiday
    global weekly_activities
    global other_activities
    global deadlines

    week_parity = 1
    is_holiday = False
    weekly_activities = []
    other_activities = []
    deadlines = []




def messenger_API():


    # `global` specifica interpretorului sa nu defineasca variabilele acestea in functie
    # ci sa foloseasca variabilele globale care poarta aceste nume
    global week_parity
    global is_holiday
    global weekly_activities
    global other_activities
    global deadlines


    init_reset_schedule()

    hardcode_schedule()         # datele sunt deja inserate in program



    # sensitive data (token, ids) are stored in environment variables
    INVITE_LINK = os.getenv('MY_DAILY_DISCORD_BOT_INVITATION_LINK')

    TOKEN = os.getenv('MY_DISCORD_DAILY_MESSENGER_BOT_TOKEN')
    GUILD_ID = os.getenv('MY_DISCORD_DAILY_SERVER_ID')
    CHANNEL_ID = os.getenv('MY_DISCORD_DAILY_CHANNEL_ID')
    
    MY_USERNAME = os.getenv('MY_DISCORD_DAILY_USERNAME')
    TARGET_USER_ID = os.getenv('MY_DISCORD_DAILY_USER_ID')             # eu: Bogdan24



    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():

        print(f"We have logged in as {client.user}")

        # first message
        welcome_message = f"Hello, I'm your bot! I am now online and ready to assist.\n"
        
        welcome_message += ("Even" if week_parity_code == 1 else "Odd")
        welcome_message += f" indexed week\n"

        welcome_message += f"\nAvailable commands:\n"
        welcome_message += f"- `/get-all-cmds`\n"
        welcome_message += f"- `/help [cmds]`\n\n"
        welcome_message += f"- `/get-current-activity`\n"
        welcome_message += f"- `/get-current-weekly-activity`\n"
        welcome_message += f"- `/get-current-other-activity`\n"
        welcome_message += f"- `/get-current-deadline`\n\n"
        welcome_message += f"- `/get-next-activity`\n"
        welcome_message += f"- `/get-next-weekly-activity`\n"
        welcome_message += f"- `/get-next-other-activity`\n"
        welcome_message += f"- `/get-next-deadline`\n\n"


        await send_discord_message(welcome_message)



        # Set up the task to send the current time every minute
        await send_discord_message_task()




    @client.event
    async def on_message(message):
        # Display the message content in the terminal
        print(f"Message from {message.author}: {message.content}")



    async def send_discord_message(msg_content):
        channel = client.get_channel(int(CHANNEL_ID))
        await channel.send(f"<@{TARGET_USER_ID}> {msg_content}")


    async def send_discord_message_task():
        await client.wait_until_ready()
        channel = client.get_channel(int(CHANNEL_ID))
        guild = discord.utils.get(client.guilds, id=int(GUILD_ID))


        while not client.is_closed():
            message = ''
            message = get_msg()


            if message == '':
                current_time = datetime.now().strftime('%H:%M')
                message = f"Current time: {current_time}\nNothing for now"


            # Send the current time to the specified channel
            await channel.send(f"<@{TARGET_USER_ID}> {message}")




            # another message can be sent after 60 seconds
            await asyncio.sleep(60)




    # Run the bot
    client.run(TOKEN)






def main():


    nr_args = len(sys.argv)

    if nr_args > 1:
        print("Err: Invalid command")
        print("Try: ./main.py")
        sys.exit(255)
    
    else:
        messenger_API()


if __name__ == '__main__':
    main()

