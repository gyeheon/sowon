import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '#')

@bot.command(aliases = ['write'])
async def writing_(ctx, *, message):
    text=message + '<br>\n'
    with open("C:/Users/PC/Desktop/HTML/sowon.html", 'a', encoding="UTF-8") as file:    
        file.write(text)



bot.run('OTUyMjE3MTkwODgxNDQ3OTQw.GtGRAv.eihdQ_mYI--q2HKHAVXRge7TLd44KUOeCaFmOs')












