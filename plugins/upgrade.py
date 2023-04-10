"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 50GB
	Price Rs 10  ind   per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 75GB
	Price Rs 20  ind   per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 200GB
	Price Rs 100 ind per Month
	
	
	Pay Using Upi I'd ```enpatamilan007@okicici```
	
	After Payment Send Screenshots Of 
        Payment To Admin @ridzy96"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ridzy96")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 50GB
	Price Rs 10  ind   per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 75GB
	Price Rs 20  ind   per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 200GB
	Price Rs 100 ind per Month
	
	
	Pay Using Upi I'd ```enpatamilan007@okicici```
	
	After Payment Send Screenshots Of 
        Payment To Admin https://t.me/ridzy96"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ridzy96")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
