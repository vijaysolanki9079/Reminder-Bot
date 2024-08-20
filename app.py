import discord
from nextcord import Embed, Color  
from discord.ext import commands, tasks
from datetime import datetime, time
import asyncio
import tracemalloc 
tracemalloc.start() 

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True

tasks_schedule = {
    "Monday": {
        "6:30": "Time to wake up!",  
        "7:30": "Time to exercise!",  
        "7:45": "Time to take Breakfast!",  
        "8:00": "Ready for the classes!",  
        "1:30": "Time to have lunch",
        "13:00": "Time to take nap!",  
        "17:00": "Time to play Badminton!",  
        "20:00": "Time to have dinner",
        "20:30": "Read book",
        "1:00": "Sleep"
    },
    "Tuesday": {
        "6:30": "Time to wake up!",  
        "7:30": "Time to exercise!",  
        "7:45": "Time to take Breakfast!",  
        "8:00": "Ready for the classes!",  
        "1:30": "Time to have lunch",
        "13:00": "Time to take nap!",  
        "17:00": "Time to play Badminton!",  
        "20:00": "Time to have dinner",
        "20:30": "Read book",
        "1:00": "Sleep"

    },
    "Wednesday": {
        "6:30": "Time to wake up!",  
        "7:30": "Time to exercise!",  
        "7:45": "Time to take Breakfast!",  
        "8:00": "Ready for the classes!",  
        "1:30": "Time to have lunch",
        "13:00": "Time to take nap!",  
        "17:00": "Time to play Badminton!",  
        "20:00": "Time to have dinner",
        "20:30": "Read book",
        "23:22": "Checking",
        "1:00": "Sleep"

    },
    "Thursday": {

        "6:30": "Time to wake up!",  
        "7:30": "Time to exercise!",  
        "7:45": "Time to take Breakfast!",  
        "8:00": "Ready for the classes!",  
        "1:30": "Time to have lunch",
        "13:00": "Time to take nap!",  
        "17:00": "Time to play Badminton!",  
        "20:00": "Time to have dinner",
        "20:30": "Read book",
        "1:00": "Sleep"
    },
    "Friday": {
        "6:30": "Time to wake up!",  
        "7:30": "Time to exercise!", 
        "7:45": "Time to take Breakfast!", 
        "8:00": "Ready for the classes!",
        "1:30": "Time to have lunch",
        "13:00": "Time to take nap!",  
        "17:00": "Time to play Badminton!", 
        "20:00": "Time to have dinner",
        "20:30": "Read book",
        "1:00": "Sleep"

    },
    "Saturday": {
        "1:40":"Testing for the reminder",
        "6:30": "Time to wake up!",  
        "7:30": "Time to exercise!",
        "7:45": "Time to take Breakfast!",   
        "8:00": "Ready for the classes!",  
        "11:12": "testing bot autp daily message",
        "11:13": "Test1",
        "11:14": "Test2",  
        "17:00": "Time to play Badminton!",  
        "20:00": "Time to have dinner",
        "20:30": "Read notes",
        "1:00": "Sleep"

    },
    "Sunday": {
        "6:30": "Time to wake up!",  
        "7:30": "Time to exercise!",  
        "7:45": "Time to take Breakfast!",  
        "8:00": "Ready for the classes!",  
        "1:30": "Time to have lunch",
        "13:00": "Time to take nap!",  
        "17:00": "Time to play Badminton!",  
        "20:00": "Time to have dinner",
        "20:30": "Read notes",
        "1:00": "Sleep"

    }
}

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name="hi")
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user) 
async def SendMessage(ctx): 
    await ctx.send("Hello")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.",color=Color.red())
    await ctx.send(embed=em)
    
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord!")
    weekly_task_reminder.start()
    weekly_task_reminder2.start()

# 1 reminder for extra add_tasks
extra_tasks_schedule = {}
lock = asyncio.Lock()


async def add_task(task, day, time):
    async with lock:
        if day not in extra_tasks_schedule:
            extra_tasks_schedule[day] = {}
        extra_tasks_schedule[day][time] = task


@tasks.loop(seconds=60)  # in every 60 seconds it will revise the code again
async def weekly_task_reminder2():
    try:
        current_time = datetime.now().strftime('%A %H:%M')   # str[0] = day , str[1] = time
        weekday, current_time = current_time.split()[0], current_time.split()[1]

        if weekday in extra_tasks_schedule and current_time in extra_tasks_schedule[weekday]:
            channel = bot.get_channel(Token id)    # cannott share the token id of the channerl
            await channel.send(extra_tasks_schedule[weekday][current_time])
    except Exception as e:
        print(f"An error occurred in weekly_task_reminder2: {e}")


# Command to add tasks
@bot.command()
async def add_task(ctx, task, day, time):
    await add_task_async(task, day, time)
    await ctx.send(f"Task '{task}' added for {day} at {time}.")

async def add_task_async(task, day, time):
    async with lock:
        if day not in extra_tasks_schedule:
            extra_tasks_schedule[day] = {}
        extra_tasks_schedule[day][time] = task


# 2 for daily work reinder
@tasks.loop(seconds=60)  # loop every minute
async def weekly_task_reminder():
    current_time = datetime.now().strftime('%A %H:%M')
    weekday, current_time = current_time.split()[0], current_time.split()[1]

    if weekday in tasks_schedule:
        if current_time in tasks_schedule[weekday]:
            channel = bot.get_channel(Token ID)  # --- > cannot share the token id of the channerl
            await channel.send(tasks_schedule[weekday][current_time])


bot.run("channel id")




 