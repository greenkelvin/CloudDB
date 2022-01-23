import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient

# Connecting with Discord
token = open("BotToken.txt", "r").read()
client = discord.Client()

# Connections needed to connect with MongoDB
try:
    conn = open("connection_url.txt", "r").read()
except:
    print("Did not connect to MongoDB")

cluster = MongoClient(conn)
database = cluster["MyData"]
collection = database["MyData"]

# Message to notify we are connected to Discord
@client.event
async def on_ready():
    print(f'I have connected to Discord as {client.user}')

# Runs whenever a message is sent on Discord
@client.event
async def on_message(message): 
    # Display messages in terminal
    print(f"{message.channel}: {message.author.name}: {message.content}")
    # ID of the writer of the message
    myquery = { "_id": message.author.id }

    # Check if user already exists in database, if it does not, adds user
    if (collection.count_documents(myquery) == 0):
        if "hello world" in str(message.content.lower()):
            data = {"_id": message.author.id, "score": 1, "pizza": 1, "potato": 1}
            collection.insert_one(data)
            await message.channel.send(f'Hello {message.author.name}')

    # If user exists, update their score
    else:
        if "hello world" in str(message.content.lower()):
            user = collection.find(myquery)
            for result in user:
                score = result["score"]
            new_score = score + 1
            collection.update_one(myquery, {"$set":{"score":new_score}})
            await message.channel.send(f'Hello {message.author.name}')

        # Adds more pizza to your document
        elif "pizza" in str(message.content.lower()):
            user = collection.find(myquery)
            for result in user:
                pizza = result["pizza"]
            new_pizza = pizza + 1
            collection.update_one(myquery, {"$set":{"pizza":new_pizza}})
            await message.channel.send(f'Gave pizza to {message.author.name}')

        elif "potato" in str(message.content.lower()):
            user = collection.find(myquery)
            for result in user:
                potato = result["potato"]
            new_potato = potato + 1
            collection.update_one(myquery, {"$set":{"potato":new_potato}})
            await message.channel.send(f'Gave a potato to {message.author.name}')

        # Removes a score from your document
        elif "goodbye world" in str(message.content.lower()):
            user = collection.find(myquery)
            for result in user:
                score = result["score"]
            new_score = score - 1
            collection.update_one(myquery, {"$set":{"score":new_score}})
            await message.channel.send(f'Goodbye {message.author.name}')

        # Finds the document of the user in the database and prints result
        elif "query" in str(message.content.lower()):
            user = collection.find(myquery)
            document = []
            for result in user:
                document.append(result)
            await message.channel.send(f'Results: {document}')

        # Removes user from database
        elif "remove" in str(message.content.lower()):
            collection.delete_one(myquery)
            await message.channel.send(f'Removed record of: {message.author.name}')

        # Resets the users score back to 1
        elif "reset" in str(message.content.lower()):
            user = collection.find(myquery)
            for result in user:
                score = result["score"]
            new_score = 1
            collection.update_one(myquery, {"$set":{"score": new_score}})
            await message.channel.send(f'Score reset')

        # Gives count of number of documents in the database
        elif "count" in str(message.content.lower()):
            count = collection.count_documents(myquery)
            await message.channel.send(f'Number of documents in database: {count}')

client.run(token)
