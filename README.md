# Overview

This is a project that demonstrates the use of cloud databases through the use of MongoDB and Discord. I created a Discord bot that will respond to messages from the user and update the database according the messages it recieves.

I had wanted to make a Discord bot for a while and also wanted to learn more about cloud databases so this was a good project to do both at once.

[Software Demo Video](https://youtu.be/qwScuMaB1VE)

# Cloud Database

The database I am using for this project is run by MongoDB.

The the database is included in a shared cluster which is run on MongoDB's cloud servers. The database itself is within the cluster and contains collections within to store your data. In this project I add documents to a collection in my database.

# Development Environment

* Visual Studio Code
* Python 3.10.1 64-bit
* MongoDB 4.4.11
* MongoDB Compass 1.30.1
* PyMongo 4.0.1
* Discord.py 1.7.3

# Useful Websites

* [Python 3.10 Ref Manual](https://docs.python.org/3.10/)
* [MongoDB Docs](https://docs.mongodb.com/)
* [Discordpy Docs](https://discordpy.readthedocs.io/en/stable/)
* [Pymongo Docs](https://pymongo.readthedocs.io/en/stable/)
* [W3Schools](https://www.w3schools.com/)

# Future Work

* Add bot commands.
* Test support of multiple users.
* Add feature that counts reactions to comments.