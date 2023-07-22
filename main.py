import discord
from discord.ext import commands
import requests


URL = 'https://script.google.com/macros/s/AKfycbz3RVdeu2OCHSIWj2CzZpYbABLUyp_OzlIUp_IzLK94bp8r219HQsCoSmriELREteegxA/exec?action=getUsers'

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="?help"))
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    latency = bot.latency
    latency_ms = round(latency * 1000)  # Convert latency to milliseconds
    await ctx.send(f'Pong! Latency: `{latency_ms}ms` 🏓')


bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Commands", color=discord.Color.blue())
    embed.add_field(name="?hw", value="Search your homework in specific date.\nExample: `?hw (your id) (date dd/mm/yyyy)`", inline=False)
    embed.add_field(name="?ping", value="Show bot ping.", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def hw(ctx, arg1, arg2):
    r = requests.get(url=URL)
    data = r.json()
    b = False
    for x in data:
        if int(arg1) == x['id'] and arg2 == x['date']:
            b = True
            break

    if b:
        await ctx.send(embed=discord.Embed(title="เลขที่ " + arg1 + " การบ้านของวันที่ " + arg2 + " ได้แก่:",
                                            description=x['details'].replace(', ','\n'), 
                                            color=discord.Color.from_rgb(0,255,0)))
    else:
        await ctx.send(embed=discord.Embed(title="ไม่พบข้อมูล",
                                            color=discord.Color.red()))


bot.run('YOUR TOKEN')