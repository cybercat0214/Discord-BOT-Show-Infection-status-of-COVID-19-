import discord
import InfectionStatus

#Please put your TOKEN
TOKEN=''

#Create object to connect
client =discord.Client()

#Create object to get InfectionData
Infection =InfectionStatus.InfectedNumber()

#define async function to reply
async def reply(message):
    reply=Infection.GetInfectedNumber(message)
    await message.channel.send(reply)

#Define an event handler to be executed when someone comment
@client.event
async def on_message(message):
     if message.content == '/Number of infected':
         await reply(message)

#launch BOT and connect discord surver
client.run(TOKEN)