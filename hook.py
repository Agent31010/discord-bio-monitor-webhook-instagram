import sqlite3
from webhook import DiscordWebhook, DiscordEmbed
from instagram import Instagram
from time import sleep
import string
import re
connection=sqlite3.connect('instagram')
cursor=connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS bios(
                  name varchar(255),
                  bio text);''')

while True:
    cursor.execute('''SELECT * FROM bios''')
    results=cursor.fetchall()
    for user in results:
        try:
            bio=Instagram(user[0]).bio
        except:
            sleep(30)
        if bio != user[1]:
            webhook = DiscordWebhook(url='WEBHOOK URL')
            # create embed object for webhook
            print(user)
            embed = DiscordEmbed(title=user[0], description=bio, color=242424)

            # add embed object to webhook
            webhook.add_embed(embed)

            webhook.execute()

            cursor.execute('''UPDATE bios SET bio=? WHERE name=?''',(bio,user[0]))
            connection.commit()
        sleep(1)

    sleep(1)
