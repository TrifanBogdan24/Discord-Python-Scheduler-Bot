#!/usr/bin/env python3

# pip3 install discord
import discord              # for Discord API
from discord.ext import commands
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

    global week_parity
    global is_holiday
    global weekly_activities
    global other_activities
    global deadlines


    if check_env_vars() == True:
        # environment variables not set
        return


    # Discord authentification
    BOT_TOKEN = os.getenv('MY_DAILY_SCHEDULER_MESSENGER_DISCORD_BOT_TOKEN')
    SERVER_ID = os.getenv('MY_DAILY_SCHEDULER_DISCORD_SERVER_ID')
    CHANNEL_ID = os.getenv('MY_DAILY_SCHEDULER_DISCORD_CHANNEL_ID')
    USER_ID = os.getenv('MY_DISCORD_USER_ID')

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='/', intents=intents)

    # Define your global variables here


    init_reset_schedule()

    hardcode_schedule()

    async def send_discord_message(channel, target_user_id, msg_content):
        """ Trimite un mesaj pe un canal de pe un server de Discord
        """
        await channel.send(f"{msg_content}")

    async def send_discord_message_task(channel, target_user_id):
        """ La fiecare 5 minute, functia va itera acitivitatile
        si va raporta daca urmeaza sa se intample ceva
        sau vreo activitate este in desfasuare
        """
        while True:
            
            message = get_msg()

            if message == '' or message is None:
                current_time = datetime.now().strftime('%H:%M')
                message = f"Current time: {current_time}\nNothing for now"

            message = f"<@{target_user_id}> {message}"

            await send_discord_message(channel, target_user_id, message)

            # 60 de secunde = un minut
            await asyncio.sleep(60)

    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user}")

        # Get the channel and guild using IDs
        channel = bot.get_channel(int(CHANNEL_ID))
        guild = discord.utils.get(bot.guilds, id=int(SERVER_ID))

        # The first message sent by the bot
        welcome_message = f"Hello @everyone, I'm your bot! I am now online and ready to assist.\n"
        welcome_message += ("Even" if week_parity == 1 else "Odd") + f" indexed week\n"
        
        welcome_message += f"\nAvailable commands:\n"
        welcome_message += f"- `/help [cmds]`\n"
        welcome_message += f"- `/help-all-cmds`\n"
        welcome_message += f"- `/clear`\n"

        welcome_message += f"- `/change-week-parity`\n"
        welcome_message += f"- `/is-holiday`"
        welcome_message += f"- `/is-working-week"

        welcome_message += f"- `get-now`\n"
        welcome_message += f"- `get-now-weekly-actvity`\n"
        welcome_message += f"- `get-now-other-activity`\n"

        welcome_message += f"- `get-next`\n"
        welcome_message += f"- `get-next-weekly-activity`\n"
        welcome_message += f"- `get-next-other-activity`\n"
        welcome_message += f"- `get-next-deadline`\n"
        welcome_message += f"- `get-next-birthday`\n"

        welcome_message += f"- add-weekly-activity`\n"
        welcome_message += f"- `add-other-activity`\n"
        welcome_message += f"- `del-weekly-acitvity\n"
        welcome_message += f"- `del-deadline`\n"
        welcome_message += f"- `del-birthday`\n"

        welcome_message += f"- shutdown-bot`\n"


        # Add your commands information here

        await send_discord_message(channel, USER_ID, welcome_message)

        # Set up the task to send messages every minute
        bot.loop.create_task(send_discord_message_task(channel, USER_ID))


    @bot.event
    async def on_message(message):
        # Display the message content in the terminal
        print(f"Message from {message.author}: {message.content}")
        
        # Enable interpreting the message as a command and reading it in the same time
        await bot.process_commands(message)


    @bot.command(name='help-all-cmds', command_prefix='/')
    async def help_all_cmds(ctx, *args):
        """Command to display help information"""
        
        help_msg = f"Welcome to the help menu, {ctx.author.mention}!\n\n"
        help_msg += f"Available commands:\n"
        


        help_msg += f"- `/help [cmds]` = opens the manual of the specified commands\n"
        help_msg += f"- `/help-all-cmds` = opens the manul of all commands\n"
        help_msg += f"- `/clear` = deletes all previous messages\n"

        help_msg += f"- `/change-week-parity`"
        help_msg += f"- `/is-holiday`"
        help_msg += f"- `/is-working-week`"


        help_msg += f"- `get-now` = displays the current activity (all types)\n"
        help_msg += f"- `get-now-weekly-actvity` = displays the current weekly activity\n"
        help_msg += f"- `get-now-other-activity`= displays the current activity, other than the weekly ones\n"

        help_msg += f"- `get-next` = displays the nexts activity (all types)\n"
        help_msg += f"- `get-next-weekly-actvity` = displays the next weekly activity\n"
        help_msg += f"- `get-next-other-activity`= displays the next activity, other than the weekly ones\n"
        help_msg += f"- `get-next-deadline` = displays the next deadline in chalendar\n"
        help_msg += f"- `get-next-birthday` = displays the next birthday in chalendar\n"

        help_msg += f"- `add-weekly-activity 'name' 'location' 'description' 'day' 'start_time' 'stop_time' 'week_parity`\n"
        help_msg += f"- `add-other-activity 'name' 'location' 'description' 'day' 'month' 'year' start_time' 'stop_time`\n"

        help_msg += f"- `del-weekly-acitvity 'name' 'day' 'week-parity' 'start_time' 'stop_time`\n"
        help_msg += f"- `del-other-acitivity 'name' 'day' 'month' 'year' 'start_time' 'stop_time' `\n"
        help_msg += f"- `del-deadline 'name' 'day' 'month' 'year' 'time'`\n"
        help_msg += f"- `del-birthday 'name' 'day' 'month' 'year'`\n"
        help_msg += f"- `del-birthday 'name'`\n"

        help_msg += f"- `shutdown-bot` = the Discord bot will leave the chat\n"


        # sending the message to the chat
        await ctx.send(help_msg)



    @bot.command(name='clear', command_prefix='/')
    async def clear_messages(ctx):
        """Command to delete all previous messages ever sent in the chat"""
        
        channel = ctx.channel
        deleted_messages = await channel.purge(limit=None, check=lambda m: m.author == bot.user or m.author == ctx.author)
        deleted_count = len(deleted_messages)
        
        await ctx.send(f"{deleted_count} messages deleted.")
        await ctx.send(f"Quick reminder: type `help-all-cmds` to see all available commands.")
    


    
    @bot.command(name='shutdown-bot', command_prefix='/')
    async def shutdonw_bot(ctx, *args):
        """Command to disconect the bot"""
        
        if int(ctx.author.id) == int(USER_ID):
            # disconecting the bot
            await ctx.send("Goodbye, @everyone! I will be leaving the chat.")
            await bot.close()
            os.exit(0)
        
        else:
            await ctx.send(f"Sorry, {ctx.author.mention}, you are not authorized to use this command.")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            cmd_name = ctx.message.content.split()[0]
            err_msg = f"Unknown command `{cmd_name}`.\n"
            err_msg += f"Type `/help-all-cmds` to see available commands."
            await ctx.send(err_msg)
    
    


    # Run the bot
    bot.run(BOT_TOKEN)






def check_env_vars():
    is_err = False

    if 'MY_DAILY_SCHEDULER_MESSENGER_DISCORD_BOT_TOKEN' not in os.environ:
        print(os.getenv('MY_DAILY_SCHEDULER_MESSENGER_DISCORD_BOT_TOKEN'))
        print("please set and export the `MY_DAILY_SCHEDULER_MESSENGER_DISCORD_BOT_TOKEN` environment variable")
        is_err = True
    
    if 'MY_DAILY_SCHEDULER_DISCORD_SERVER_ID' not in os.environ:
        print("please set and export the `MY_DAILY_SCHEDULER_DISCORD_SERVER_ID` environment variable")
        is_err = True

    if 'MY_DAILY_SCHEDULER_DISCORD_CHANNEL_ID' not in os.environ:
        print("please set and export the `MY_DAILY_SCHEDULER_DISCORD_CHANNEL_ID` environment variable")
        is_err = True

    if 'MY_DISCORD_USER_ID' not in os.environ:
        print("please set and export the `MY_DISCORD_USER_ID` environment variable")
        is_err = True
    
    return is_err



def main():


    nr_args = len(sys.argv)

    if nr_args > 1:
        print("Err: Invalid command")
        print("Try: ./main.py")
        is_err = True
        sys.exit(255)
    else:
        messenger_API()


if __name__ == '__main__':
    main()
