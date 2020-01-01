
'''
Discord Invite Auto Joiner - Self Bot!
RKuangDev
'''

import discord
import datetime
import requests

token = "Token" #Replace with discord token
client = discord.Client()

print(r'''
====================================================================================
______ _                       _   _   _ _ _               _____ _  __ _       
|  _  (_)                     | | | \ | (_) |             |  __ (_)/ _| |      
| | | |_ ___  ___ ___  _ __ __| | |  \| |_| |_ _ __ ___   | |  \/_| |_| |_ ___ 
| | | | / __|/ __/ _ \| '__/ _` | | . ` | | __| '__/ _ \  | | __| |  _| __/ __|
| |/ /| \__ \ (_| (_) | | | (_| | | |\  | | |_| | | (_) | | |_\ \ | | | |_\__ \
|___/ |_|___/\___\___/|_|  \__,_| \_| \_/_|\__|_|  \___/   \____/_|_|  \__|___/

By: RockyLogic
=====================================================================================
''')

input("""
I've Read The ReadMe File, And I Choose to Continue:
Press Any 'Enter' To Continue: """)

print ("\n Monitoring... \n")

@client.event
async def on_message(message):
    if "discord.gift/" in message.content:
        print("[{}]".format(datetime.datetime.now()),
              "[Server: {0.guild.name}][{0.channel}][{0.author}]:'{0.content}'".format(message))
        print("[{}] Found Nitro Gift".format(datetime.datetime.now()))

        indexNum = message.content.find("discord.gift/")
        indexNum += 13
        giftCode = message.content[indexNum:indexNum+16]

        print("[{}] Gift Code: ".format(datetime.datetime.now()), giftCode)

        URL = "https://discordapp.com/api/v6/entitlements/gift-codes/" + giftCode + "/redeem"

        headers = {
            "authorization": "{}".format(token),
        }

        requestResponse = requests.post(url=URL, data="", headers=headers)

        print(f"[{datetime.datetime.now()}] Attempting to Redeem")

        if requestResponse.status_code == 200:
            print(f"[{datetime.datetime.now()}] Successfully Attempted To Redeem Nitro")
        else:
            print(f"[{datetime.datetime.now()}] Failed To Redeem Nitro")

client.run(token, bot=False)