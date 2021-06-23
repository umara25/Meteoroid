import discord
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('{0.user} is ready'
          .format(bot))


@bot.command()
async def weather(ctx, *, cityname):
    link = 'REDACTED'.format \
        (cityname)

    reqs = requests.get(link)

    city_weather = reqs.json()

    temp = city_weather['main']['temp']
    wind_speed = city_weather['wind']['speed']

    description = city_weather['weather'][0]['description']

    datatobesent = (('Temperature : {}°C'.format(temp)) +
                    "\n" +
                    ('Wind Speed : {} m/s'.format(wind_speed) +
                     "\n" +
                     ('Description : {}'.format(description))))

    embedVar = discord.Embed(title="Weather for " + cityname, color=0x00ff00)
    embedVar.add_field(name=cityname + ":", value=datatobesent, inline=False)
    await ctx.send(embed=embedVar)


@bot.command()
async def Meteoroidhelp(ctx):
    embedVar = discord.Embed(title="Meteoroid Help", color=0x00ff00)
    embedVar.add_field(name="Commands:",
                       value="To get the weather of a city do $weather and then the name of city" + "\n" + "For example: $weather Toronto" +
                             "\n" + "\n" + "$Meteoroidhelp gives you help with the bot",

                       inline=False)
    await ctx.send(embed=embedVar)


@bot.command()
async def Meteoroidinfo(ctx):
    embedVar = discord.Embed(title="Info about Meteroid", color=0x00ff00)
    embedVar.add_field(name="Info:",
                       value="The code for this bot can be found at " +
                             "https://github.com/umara25/Meteoroid/blob/main/Meteoroid.py", inline=False) 
    await ctx.send(embed=embedVar)

bot.run(REDACTED)
