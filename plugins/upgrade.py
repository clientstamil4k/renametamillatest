"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	⛩️INDIVIDUAL PLAN - FOR 1 MEMBER⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 5 GB💫
	💵Price Rs 10 or 0.5$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 20 or 1$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 20 GB💫
	💵Price Rs 30 or 1.5$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 50 or 2.5$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 100 GB💫
	💵Price Rs 100 or 5$ per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	
	⛩️TEAM PLANS - FOR 1 TO 4 MEMBERS⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 5 GB💫
	💵Price Rs 20 or 1$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 40 or 2$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 20 GB💫
	💵Price Rs 60 or 3$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 100 or 5$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 100 GB💫
	💵Price Rs 200 or 10$ per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	⚠️*********NOTE**********⚠️
	
	After Payment Send Screenshots Of 
        Payment To Admin @ridzy96
	
	⚠️*********NOTE**********⚠️"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ridzy96")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	
	⛩️INDIVIDUAL PLAN - FOR 1 MEMBER⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 5 GB💫
	💵Price Rs 10 or 0.5$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 20 or 1$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 20 GB💫
	💵Price Rs 30 or 1.5$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 50 or 2.5$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 100 GB💫
	💵Price Rs 100 or 5$ per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	
	⛩️TEAM PLANS - FOR 1 TO 4 MEMBERS⛩️
	
	🥉 Bronze Tier🥉 
	💫Daily  Upload  limit 5 GB💫
	💵Price Rs 20 or 1$ per Month💵
	
	🥈 Silver Tier 🥈 
	💫Daily  Upload  limit 10 GB💫
	💵Price Rs 40 or 2$ per Month💵
	
	🪙 Gold Tier 🪙 
	💫Daily  Upload  limit 20 GB💫
	💵Price Rs 60 or 3$ per Month💵
	
	✨ Platinum Tier ✨ 
	💫Daily  Upload  limit 40 GB💫
	💵Price Rs 100 or 5$ per Month💵
	
	💎 Diamond Tier 💎
	💫Daily  Upload  limit 100 GB💫
	💵Price Rs 200 or 10$ per Month💵
	
	Pay Using Upi I'd ```ruban.private@oksbi```
	
	
	⚠️*********NOTE**********⚠️
	
	After Payment Send Screenshots Of 
        Payment To Admin @ridzy96
	
	⚠️*********NOTE**********⚠️"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/ridzy96")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
