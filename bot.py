import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello! How can I help you today?")


@bot.command(name="add")
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f"The result of {num1} + {num2} is {result}.")


bot.run(token)
