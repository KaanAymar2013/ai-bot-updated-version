import discord
from discord.ext import commands
from bot_token import token
from class_detection import detect_rapper

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command() 
async def algila(ctx):
    await ctx.send("Algılama başlandı")
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/(image_path)"
            await attachment.save(file_path)
            await ctx.send("Gorsel kaydedildi!")
            model_path = "keras_model.h5"
            labels_path = "labels.txt"

            name,score = detect_rapper(file_path, model_path, labels_path)
            await ctx.send(f"Bu bir {name.strip()},bundan % {int(score*100)} eminim!")
    else:
        await ctx.send("Lütfen komutla birlikte bir görsel yükleyin")
           

bot.run(token)