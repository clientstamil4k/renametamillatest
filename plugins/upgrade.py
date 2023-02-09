"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 10  ind /🌎 0$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 50  ind /🌎 1$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 90-100  ind /🌎 2$  per Month
	
	
	Pay Using Upi I'd ```22610001340940@icici```
	
	After Payment Send Screenshots Of 
        Payment To Admin @KUSHALHK"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/KUSHALHK")], 
        			[InlineKeyboardButton("Paytm",url = "https://fypmoney.in/add/cfmer.22610001340940@icici"),
        			InlineKeyboardButton("Paytm",url = "https://fypmoney.in/add/cfmer.22610001340940@icici")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 10  ind /🌎 0$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 50  ind /🌎 1$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 90-100  ind /🌎 2$  per Month
	
	
	Pay Using Upi I'd ```22610001340940@icici```
	
	After Payment Send Screenshots Of 
        Payment To Admin @KUSHALHK"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/KUSHALHK")], 
        			[InlineKeyboardButton("Paytm",url = "https://fypmoney.in/add/cfmer.22610001340940@icici"),
        			InlineKeyboardButton("Paytm",url = "https://fypmoney.in/add/cfmer.22610001340940@icici")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
