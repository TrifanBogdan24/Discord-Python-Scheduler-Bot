#!/usr/bin/env python3

# pip3 install discord
import discord              # for Discord API
from discord.ext import commands
import asyncio
import json

import os, sys
from dotenv import load_dotenv      # environment variables

from datetime import datetime

# classes
from data_structures import DataHandler
from data_structures import ScheduleUser
from data_structures import WeeklyActivity
from data_structures import OtherActivity
from data_structures import Deadline
from data_structures import Birthday




import random




users_schedules = []



def get_msg(target_user_id):
    """ obtine un mesaj sugestiv pentru a fi trimis in functie de ora curenta
    """
    dt = datetime.now()
    h_m = dt.strftime('%H:%M')
    day = dt.isoweekday()       # ziua saptamanii (index, numar de 1-7)


    timestamp_now = DataHandler().get_timestamp(h_m)
    ten_min_timestamp = DataHandler().get_timestamp("00:10")

    msg = ''

    
    user = ScheduleUser.get_user_by_id(target_user_id, users_schedules)


    for activ in user.weekly_activities:

        if activ.user_id != target_user_id:
            continue



        if activ.is_next_in_schedule(user) == True:
            msg += f"Next: {activ}"
        if activ.is_current_in_schedule(user) == True:
            msg += f"Now: {activ}"





    return msg



def append_not_none(l, el):
    if type(l) != list:
        pass

    if el is not None:
        l.append(el)


def get_min(h_m):
    (hour, minute) = h_m.split(':')

    # print(f"{hour}   {minute}")
    
    return (hour, minute)



def hardcode_schedule(user_id):

    global users_schedules
    print(user_id)
    owner_user = ScheduleUser.get_user_by_id(user_id, users_schedules)

    weekly_activities = []


    # WeeklyActivity('name', 'location', 'descritption', 'day', 'start_time_h_m', 'stop_time_h_m', 'week_parity)
    # luni:
    new_activ = WeeklyActivity(user_id, 'Lab PCOM', 'sala EG 205', '-', 'luni', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Curs SOC', 'sala PR 001', 'obligatoriu', 'luni', '12:00', '14:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_acitv = WeeklyActivity(user_id, 'Curs PCOM', 'sala PR 001', '-', 'luni', '14:00', '16:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Curs ED', 'sala PR 001', '-', 'luni', '14:00', '16:00', 'par')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Curs ELTH CA', 'sala AN 030', 'la seria CA', 'luni', '16:00', '18:00', '-')
    append_not_none(weekly_activities, new_activ)
    # marti:
    new_activ = WeeklyActivity(user_id, 'Curs ED', 'sala PR 001', '-', 'marti', '7:00', '10:00', '-')
    new_activ = WeeklyActivity(user_id, 'Curs ED', 'sala PR 001', '-', 'marti', '8:00', '10:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Curs SOC', 'sala PR 001', 'obligatoriu', 'marti', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Curs PA', 'sala EC 004', '-', 'marti', '16:00', '18:00', '-')
    append_not_none(weekly_activities, new_activ)
    # miercuri:
    new_activ = WeeklyActivity(user_id, 'seminar PCT', 'sala PR 106', '', 'miercuri', '8:00', '10:00', 'par')
    append_not_none(weekly_activities, new_activ)
    new_acitv = WeeklyActivity(user_id, 'Curs PCOM', 'sala PR 001', '-', 'miercuri', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Curs PP', 'sala PR 001', 'obligatoriu', 'miercuri', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'seminar ED', 'sala EG 303', '-', 'miercuri', '16:00', '18:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_acitv = WeeklyActivity(user_id, 'Curs PCT', 'sala A04 LEU', 'optional', 'miercuri', '18:00', '20:00', 'par')
    append_not_none(weekly_activities, new_activ)
    # joi:
    new_activ = WeeklyActivity(user_id, 'seminar ELTH', 'PR 003', '-', 'joi', '8:00', '10:00', 'impar')
    append_not_none(weekly_activities, new_acitv)
    new_activ = WeeklyActivity(user_id, 'lab ELTH', 'EB 206-207', '-', 'joi', '8:00', '10:00', 'par')
    append_not_none(weekly_activities, new_acitv)
    new_activ = WeeklyActivity(user_id, 'sport (impar)', 'sala de sport', '-', 'joi', '10:00', '12:00', 'impar')
    append_not_none(weekly_activities, new_acitv)
    new_activ = WeeklyActivity(user_id, 'Lab SOC', 'sala ED 220', '-', 'joi', '12:00', '14:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Lab SOC', 'sala ED 220', '-', 'joi', '14:00', '16:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Lab ED', 'sala ED 314', '-', 'joi', '16:00', '18:00', 'impar')
    append_not_none(weekly_activities, new_activ)
    # vineri:
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Lab PA', 'sala EG 405', '-', 'vineri', '10:00', '12:00', '-')
    append_not_none(weekly_activities, new_activ)
    new_activ = WeeklyActivity(user_id, 'Lab PP', 'sala EG 103 b', '-', 'vineri', '12:00', '14:00', '-')
    append_not_none(weekly_activities, new_activ)



    owner_user.weekly_activities = weekly_activities






def messenger_API():


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
    intents.members = True

    bot = commands.Bot(command_prefix='/', intents=intents)

    # remove default bot commands (in order to replace with something else)
    if 'help' in bot.all_commands:
        del bot.all_commands['help']

    # Define your global variables here


    global users_schedules

    

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
        
            message = get_msg(target_user_id)

            if message == '' or message is None:
                # pentru a afisa ora din minut in minut, atunci cand nu e nimic de afisat
                # decomenteaza liniile de mai jos
                
                # # current_time = datetime.now().strftime('%H:%M')
                # # message =  f"Current time: {current_time}\nNothing for now"
                # # message = f"<@{target_user_id}> {message}"
                # # await send_discord_message(channel, target_user_id, message)
                pass
            else:
                message = f"<@{target_user_id}> {message}"
                await send_discord_message(channel, target_user_id, message)

            # 60 de secunde = un minut
            await asyncio.sleep(60)


    async def send_goodnight_message_task(channel, target_user_id):
        """
        """

        user = ScheduleUser.get_user_by_id(target_user_id, users_schedules)

        while True:

            dt = datetime.now()
            h_m = dt.strftime('%H:%M')
            timestamp_now = DataHandler.get_timestamp(h_m)

            timestamp_user_bedtime = DataHandler.get_timestamp(user.bedtime)

            if timestamp_user_bedtime == timestamp_now:
                await goodnight_message_helper(channel, target_user_id)
                
            # verifica ora din minut in munit
            await asyncio.sleep(60)


    async def goodnight_message_helper(channel, target_user_id):

        try:
            dir_content = os.listdir('images/bedtime')
            gif_names = [name for name in dir_content if name.endswith('.gif')]
        except:
            print(f"Missing path for GIFs `images/bedtime`")
            return


        while True:
            try:
                gif_name = random.choice(gif_names)

                file_location = os.path.join(os.getcwd(), 'images/bedtime', gif_name)

                with open(file_location, 'rb') as f:
                    gif_file = discord.File(f)


                msg = f"Good night, <@{target_user_id}>!\n"

                # trimite un mesaj text, alaturi de o imagine GIF
                await channel.send(f"{msg}", file=gif_file)
                break
            except:
                continue
        
            

    

        

    @bot.event
    async def on_ready():
        """ aceasta functia este rulata o singura data
        la conectarea bot-ului la serverul de discord
        """


        print(f"We have logged in as {bot.user}")

        # Get the channel and guild using IDs
        channel = bot.get_channel(int(CHANNEL_ID))
        guild = discord.utils.get(bot.guilds, id=int(SERVER_ID))

        # The first message sent by the bot
        welcome_message = f"Hello @everyone, I'm your bot! I am now online and ready to assist.\n"
        
        welcome_message += f"\nAvailable commands:\n"
        welcome_message += f"- `/help`\n"                   # works
        welcome_message += f"- `/help-all-cmds`\n"          # works
        welcome_message += f"- `/help [cmds]`\n"            # works
        welcome_message += f"- `/clear`\n"                  # works

        welcome_message += f"- `/toggle-week-parity`\n"     # works
        welcome_message += f"- `/toggle-holiday`\n"         # works
        welcome_message += f"- `/get-week-state`\n"
        welcome_message += f"- `/get-week-parity`\n"
        welcome_message += f"- `/get-is-holiday-parity`\n"

        welcome_message += f"- `/get-today-timetable`\n"
        welcome_message += f"- `/get-weekly-timetable`\n"
        welcome_message += f"- `/get-deadlines-table`\n"
        welcome_message += f"- `/get-birthdays-table`\n"


        welcome_message += f"- `/get-now`\n"
        welcome_message += f"- `/get-now-weekly-actvity`\n"
        welcome_message += f"- `/get-now-other-activity`\n"

        welcome_message += f"- `/get-next`\n"
        welcome_message += f"- `/get-next-weekly-activity`\n"
        welcome_message += f"- `/get-next-other-activity`\n"
        welcome_message += f"- `/get-next-deadline`\n"
        welcome_message += f"- `/get-next-birthday`\n"

        welcome_message += f"- `/add-weekly-activity`\n"
        welcome_message += f"- `/add-other-activity`\n"
        welcome_message += f"- `/add-deadline`\n"
        welcome_message += f"- `/add-birthday`\n"

        welcome_message += f"- `/del-weekly-acitvity`\n"
        welcome_message += f"- `/del-other-acitvity`\n"
        welcome_message += f"- `/del-deadline`\n"
        welcome_message += f"- `/del-birthday`\n"

        welcome_message += f"- `/shutdown-bot`\n"           # works


        # Add your commands information here

        await send_discord_message(channel, USER_ID, welcome_message)

        
        
        # Get the guild (server) where the bot is connected
        guild = bot.guilds[0]  # Assuming the bot is only connected to one guild
        
        # Fetch all members in the guild
        await guild.chunk()

        # Extract user IDs and names and print them
        print("User IDs and Names in this chat:")
        
        for member in guild.members:
            if member == bot.user:
                continue
            print(f"ID: {member.id}, Name: {member.name}")
            users_schedules.append(ScheduleUser(member.id, member.name))

            # Set up the task to send messages from times to time to each user
            bot.loop.create_task(send_discord_message_task(channel, member.id))
            bot.loop.create_task(send_goodnight_message_task(channel, member.id))

        hardcode_schedule(int(USER_ID))



    @bot.event
    async def on_message(message):
        # Display the message content in the terminal
        print(f"Message from {message.author}: {message.content}")
        
        # Enable interpreting the message as a command and reading it in the same time
        await bot.process_commands(message)




    @bot.command(name='help-all-cmds', command_prefix='/')
    async def help_all_cmds(ctx, *args):
        """Command to display help information for all commands"""
        
        help_msg = f"Welcome to the help menu, {ctx.author.mention}!\n\n"
        help_msg += f"Available commands:\n"
        
        help_msg += help_all_cmds_msg()
        
        # sending the message to the chat
        await ctx.send(help_msg)


    @bot.command(name='help', command_prefix='/')
    async def help_cmd(ctx, *args):
        """Command to display help information
        for specified commands
        or all of them, if there are no commands specified
        """



        help_msg = ''

        if len(args) == 0:
            help_msg = help_all_cmds_msg()


        # all unique elements, keeps the order
        unique_cmds = []
        for arg in args:
            if arg not in unique_cmds:
                unique_cmds.append(arg)

        unrecognised_cmds = []

        for cmd in unique_cmds:

            if cmd == 'help':
                help_msg += f"- `/help` = opens the manual of all commands\n"
                help_msg += f"- `/help [cmds]` = opens the manual of the specified commands\n"
                continue
            if cmd == 'help-all-cmds':
                help_msg += f"- `/help-all-cmds` = opens the manul of all commands\n"
                continue
            if cmd == 'clear':
                help_msg += f"- `/clear` = deletes all previous messages\n"
                continue
            if cmd == 'toggle-week-parity':
                help_msg += f"- `/toggle-week-parity` = the week index becomes odd if it was even and vice versa"
                continue
            if cmd == 'toggle-holiday':
                help_msg += f"- `/toggle-holiday` = switches between a holiday week (weekly activities will no longer be displayed) to a working week\n"
                continue
            if cmd == 'get-week-state':
                help_msg += f"- `/get-week-state` = displays information regarding the parity of the week and whether it is a holoday or not\n"
                continue
            if cmd == 'get-week-parity':
                help_msg += f"- `/get-week-parity` = displays wheter the index of the week is odd or even\n"
                continue
            if cmd == 'get-is-holiday':
                help_msg += f"- `/get-is-holiday` = prints the state of the week\n"
                continue
            if cmd == 'get-today-timetable':
                help_msg += f"- `/get-today-timetable` = gets relevant details for the today's plan\n"
                continue
            if cmd == 'get-weekly-timetable':
                help_msg += f"- `/get-weekly-timetable` = prints the schedule for this week\n"
                continue
            if cmd == 'get-deadlines-table':
                help_msg += f"- `/get-deadlines-table` = displays all the deadlines, sorted from the most to the least recent\n"
                continue
            if cmd == 'get-birthdays-table':
                help_msg += f"- `/get-birthdays-table` = displays all the birthdays, sorted from the most to the least recent\n"
                continue
            if cmd == 'get-now':
                help_msg += f"- `get-now` = displays the current activity (all types)\n"
                continue
            if cmd == 'get-next':
                help_msg += f"- `get-next` = displays the nexts activity (all types)\n"
                continue
            if cmd == 'get-next-weekly-activity':
                help_msg += f"- `get-next-weekly-actvity` = displays the next weekly activity\n"
                continue
            if cmd == 'get-next-other-activity':
                help_msg += f"- `get-next-other-activity`= displays the next activity, other than the weekly ones\n"
                continue
            if cmd == 'get-next-deadline':
                help_msg += f"- `get-next-other-activity`= displays the next activity, other than the weekly ones\n"
                continue
            if cmd == 'get-next-birthday':
                help_msg += f"- `get-next-birthday` = displays the next birthday in chalendar\n"
                continue
            if cmd == 'add-weekly-activity':
                help_msg += f"- `add-weekly-activity [name] [location] [description] [day] [start_time HH:MM] [stop_time HH:MM] [week_parity]`\n"
                continue
            if cmd == 'add-other-activity':
                help_msg += f"- `add-other-activity [name] [location] [description] [day] [month] [year] [start_time HH:MM] [stop_time HH:MM]`\n"
                continue
            if cmd == 'add-deadline':
                help_msg += f"- `add-deadline [name] [description] [day] [month] [year] [time HH:MM]`\n"
                continue
            if cmd == 'add-birthday':
                help_msg += f"- `add-birthday [name] [day] [month] [year]`\n"
                continue
            if cmd == 'del-weekly-acitivity':
                help_msg += f"- `del-weekly-acitvity [name] [day] [week-parity] [start_time HH:MM] [stop_time HH:MM]`\n"
                continue
            if cmd == 'del-other-activity':
                help_msg += f"- `del-other-acitivity [name] [day] [month] [year] [start_time HH:MM] [stop_time HH:MM]`\n"
                continue
            if cmd == 'del-deadline':
                help_msg += f"- `del-deadline [name] [day] [month] [year] [time HH:MM]`\n"
                continue
            if cmd == 'del-birthday':
                help_msg += f"- `del-birthday 'name'`\n"
                continue
            if cmd == 'shutdown-bot':
                help_msg += f"- `shutdown-bot` = the Discord bot will leave the chat\n"
                continue
            else:
                unrecognised_cmds.append(cmd)


        if len(unrecognised_cmds) == 1:
            help_msg += f"\nUnrecognized command: '{unrecognised_cmds[0]}'"       
        elif len(unrecognised_cmds) > 1:
            help_msg += f"\nUnrecognized commands: {unrecognised_cmds}"       


        # sending the message to the chat
        await ctx.send(help_msg)



    def help_all_cmds_msg():
        help_msg = ''
        

        help_msg += f"- `/help` = opens the manual of all commands\n"
        help_msg += f"- `/help [cmds]` = opens the manual of the specified commands\n"
        help_msg += f"- `/help-all-cmds` = opens the manul of all commands\n"
        help_msg += f"- `/clear` = deletes all previous messages\n"

        help_msg += f"- `/toggle-week-parity` = the week index becomes odd if it was even and vice versa\n"
        help_msg += f"- `/toggle-holiday` = switches between a holiday week (weekly activities will no longer be displayed) to a working week\n"
        help_msg += f"- `/get-week-parity` = displays wheter the index of the week is odd or even\n"
        help_msg += f"- `/get-is-holiday` = prints the state of the week\n"

        help_msg += f"- `/get-today-timetable` = gets relevant details for the today's plan\n"
        help_msg += f"- `/get-weekly-timetable` = prints the schedule for this week\n"
        help_msg += f"- `/get-deadlines-table` = displays all the deadlines, sorted from the most to the least recent\n"
        help_msg += f"- `/get-birthdays-table` = displays all the birthdays, sorted from the most to the least recent\n"


        help_msg += f"- `get-now` = displays the current activity (all types)\n"

        help_msg += f"- `get-next` = displays the nexts activity (all types)\n"
        help_msg += f"- `get-next-weekly-actvity` = displays the next weekly activity\n"
        help_msg += f"- `get-next-other-activity`= displays the next activity, other than the weekly ones\n"
        help_msg += f"- `get-next-deadline` = displays the next deadline in chalendar\n"
        help_msg += f"- `get-next-birthday` = displays the next birthday in chalendar\n"

        help_msg += f"- `add-weekly-activity [name] [location] [description] [day] [start_time HH:MM] [stop_time HH:MM] [week_parity]`\n"
        help_msg += f"- `add-other-activity [name] [location] [description] [day] [month] [year] [start_time HH:MM] [stop_time HH:MM]`\n"

        help_msg += f"- `del-weekly-acitvity [name] [day] [week-parity] [start_time HH:MM] [stop_time HH:MM]`\n"
        help_msg += f"- `del-other-acitivity [name] [day] [month] [year] [start_time HH:MM] [stop_time HH:MM]`\n"
        help_msg += f"- `del-deadline [name] [day] [month] [year] [time HH:MM]`\n"
        help_msg += f"- `del-birthday [name] [day] [month] [year]`\n"
        help_msg += f"- `del-birthday [name]`\n"

        help_msg += f"- `shutdown-bot` = the Discord bot will leave the chat\n"

        return help_msg



    @bot.command(name='clear', command_prefix='/')
    async def clear_messages(ctx):
        """Command to delete all previous messages ever sent in the chat"""
        
        channel = ctx.channel
        deleted_messages = await channel.purge(limit=None, check=lambda m: m.author == bot.user or m.author == ctx.author)
        deleted_count = len(deleted_messages)
        
        await ctx.send(f"{deleted_count} messages deleted.")
        await ctx.send(f"Quick reminder: type `/help` or `/help-all-cmds` to see all available commands.")
    


    
    @bot.command(name='shutdown-bot', command_prefix='/')
    async def shutdown_bot(ctx, *args):
        """Command to disconect the bot
        """
        
        if int(ctx.author.id) == int(USER_ID):
            # disconecting the bot
            await ctx.send("Goodbye, @everyone! I will be leaving the chat.")
            await bot.close()
            os.exit(0)
        
        else:
            await ctx.send(f"Sorry, {ctx.author.mention}, you are not authorized to use this command.")



    @bot.command(name='toggle-week-parity', command_prefix='/')
    async def toggle_week_parity(ctx, *args):

        schedule_user = ScheduleUser.get_user_by_id(ctx.author.id, users_schedules)

        if schedule_user.is_holiday == True:
            await ctx.send(f"{ctx.authro.mention} este in vacanta.")
            return


        if schedule_user.week_parity == 1:
            schedule_user.week_parity = 0
            await ctx.send(f"{ctx.author.mention} ai trecut la o saptamana para.")
        else:
            schedule_user.week_parity = 1
            await ctx.send(f"{ctx.author.mention} ai trecut la o saptamana impara.")


    @bot.command(name='toggle-holiday', command_prefix='/')
    async def togle_holiday(ctx, *args):
        schedule_user = ScheduleUser.get_user_by_id(ctx.author.id, users_schedules)

        if schedule_user.week_parity == False:
            schedule_user.week_parity = True
            await ctx.send(f"{ctx.author.mention} esti in vacanta.")
        else:
            schedule_user.week_parity = False
            await ctx.send(f"{ctx.author.mention} esti intr-o saptamana lucratoare")


    @bot.command(name='get-week-state', command_prefix='/')
    async def get_week_state(ctx, *args):
        schedule_user = ScheduleUser.get_user_by_id(ctx.author.id, users_schedules)

        week_parity = schedule_user.week_parity
        is_holiday = schedule_user.is_holiday

        msg = ''
        paritate = ('para' if week_parity == 1 else 'impara')
        neg_par = ('impara' if week_parity == 1 else 'para')


        if is_holiday == True:
            msg = f"Esti in vacanta momentan"
            msg += f", nu ai de ce sa iti faci griji :)"
            msg += f"\nFriendly reminder: urmatoarea saptamana de lucru va fi {paritate}"
        else:
            msg = f"Saptamana de lucru curenta este {neg_par}\n"


        await ctx.send(f"{ctx.author.mention} {msg}")



    @bot.command(name='get-week-parity', command_prefix='/')
    async def get_week_parity(ctx, *args):
        schedule_user = ScheduleUser.get_user_by_id(ctx.author.id, users_schedules)

        week_parity = schedule_user.week_parity
        is_holiday = schedule_user.is_holiday

        msg = ''

        if week_parity == 1:
            msg = f"Esti intr-o saptamana impara\n"
        else:
            msg = f"Esti intr-o saptamana para\n"


        await ctx.send(f"{ctx.author.mention} {msg}")


    @bot.command(name='get-is-holiday', command_prefix='/')
    async def get_is_holiday(ctx, *args):
        schedule_user = ScheduleUser.get_user_by_id(ctx.author.id, users_schedules)

        week_parity = schedule_user.week_parity
        is_holiday = schedule_user.is_holiday

        msg = ''

        if is_holiday == True:
            msg = f"Esti liber saptamana asta.\n"
        else:
            msg = f"Esti intr-o saptamana lucratoare.\n"


        await ctx.send(f"{ctx.author.mention} {msg}")





    @bot.command(name='get-today-timetable', command_prefix='/')
    async def get_today_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-today-timetable')
        # TODO: trimite un mesaj care contine un tabel, ca cele generate de fisierele markdown



    @bot.command(name='get-weekly-timetable', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-weekly-timetable')
        # TODO: implementeaza comanda


    @bot.command(name='get-deadlines-table', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-deadlines-timetable')
        # TODO: implementeaza comanda




    @bot.command(name='get-birthdays-table', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-birthdays-timetable')
        # TODO: implementeaza comanda


    @bot.command(name='get-now', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-now')
        # TODO: implementeaza comanda


    @bot.command(name='get-now-weekly-activity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-now-weekly-activity')
        # TODO: implementeaza comanda


    @bot.command(name='get-now-other-acitivity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-now-other-activity')
        # TODO: implementeaza comanda


    @bot.command(name='get-next', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-next')
        # TODO: implementeaza comanda


    @bot.command(name='get-next-weekly-activity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-next-weekly-activity')
        # TODO: implementeaza comanda

    @bot.command(name='get-next-other-activity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-next-other-activity')
        # TODO: implementeaza comanda


    @bot.command(name='get-next-deadline', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-next-deadline')
        # TODO: implementeaza comanda


    @bot.command(name='get-next-birthday', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'get-next-birthday')
        # TODO: implementeaza comanda



    @bot.command(name='add-weekly-activity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'add-weekly-activity')
        # TODO: implementeaza comanda


    @bot.command(name='add-other-activity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'add-other-activity')
        # TODO: implementeaza comanda


    @bot.command(name='add-deadline', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'add-deadline')
        # TODO: implementeaza comanda



    @bot.command(name='add-birthday', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'add-birthday')
        # TODO: implementeaza comanda


    @bot.command(name='del-weekly-activity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'del-weekly-activity')
        # TODO: implementeaza comanda

    @bot.command(name='del-other-activity', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'del-other-activity')
        # TODO: implementeaza comanda


    @bot.command(name='del-deadline', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'del-deadline')
        # TODO: implementeaza comanda


    @bot.command(name='del-birthday', command_prefix='/')
    async def get_weekly_timetable(ctx, *args):
        await command_under_construction(ctx, 'del-birthday')
        # TODO: implementeaza comanda


    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            cmd_name = ctx.message.content.split()[0]
            err_msg = f"Unknown command `{cmd_name}`.\n"
            err_msg += f"Type `/help-all-cmds` to see available commands."
            await ctx.send(err_msg)
    
    
    
    @bot.event
    async def command_under_construction(ctx, cmd_name):
        """Va afisa un text de eroare si un`GIF` sugestiv
        """


        await ctx.send(f"Sorry.... the command `{cmd_name}` is not available right now.")



        try:
            dir_content = os.listdir('images/under-construction')
            gif_names = [name for name in dir_content if name.endswith('.gif')]
        except:
            print(f"Missing path for GIFs `images/under-construction`")
            return


        while True:
            
            # ne asigram trimiterea unui `GIF` pe discord

            try:

                gif_name = random.choice(gif_names)

                file_location = os.path.join(os.getcwd(), 'images/under-construction', gif_name)

                with open(file_location, 'rb') as f:
                    gif_file = discord.File(f)
            
                await ctx.send(file=gif_file)
                break
            
            except:
                continue


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
    load_dotenv()
    main()
