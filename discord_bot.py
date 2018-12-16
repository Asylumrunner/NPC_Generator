import discord
import generator
import secrets

client = discord.Client()

@client.event
async def on_ready():
    print("RoboGM has signed in!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!generate'):
        try:
            split_message_content = message.content.split()
            num_characters = 1
            if len(split_message_content) > 1:
                num_characters = min(5, int(split_message_content[1]))
                num_characters = max(num_characters, 1)
            attribute_list = []
            if len(split_message_content) > 2:
                attribute_list = split_message_content[2:]

            characters = generator.generate_characters(num_characters, attribute_list)

            chat_message = ""
            for character in characters:
                chat_message += "```Name: {}\n".format(character['Name'])
                chat_message += "Traits: {}\n".format(", ".join(character['Traits']))
                chat_message += "Attributes: {}```\n".format(", ".join(character['Attributes']))
            await client.send_message(message.channel, chat_message)
        except Exception:
            await client.send_message(message.channel, "Whoopsies! Something went bad!")

client.run(secrets[client_key])
