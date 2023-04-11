import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Creater :- <a href='https://t.me/ridzy96'>🦋𝘾𝙧𝙚𝙖𝙩𝙤𝙧🦋</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- HEROKU\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/ridzy96'>OWNER</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/ridzy96'>**RIDZY**</a> ❤️",quote=True)
