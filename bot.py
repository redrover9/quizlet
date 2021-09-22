import discord
import os
import json
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/question'):
        with open("quizlet.json") as json_file:
            data = json.load(json_file)
            question = random.choice(list(data))
            print(question)
            global answer
            answer = data.get(question)
            print(answer)
            await message.channel.send(question)
    if message.content.startswith('/answer'):
        with open("quizlet.json") as json_file:
            data = json.load(json_file)
            await message.channel.send(answer)
client.run(os.getenv('TOKEN'))
