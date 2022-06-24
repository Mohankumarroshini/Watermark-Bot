# (c) @AbirHasan2005

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID", 12345))
	API_HASH = os.environ.get("API_HASH")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", 1359080430)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("OWNER_ID", 1964362058))
	CAPTION = "By @TamilBots"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "WaterMarkProRoBot")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
Hɪ, I ᴀᴍ Vɪᴅᴇᴏ Wᴀᴛᴇʀᴍᴀʀᴋ Aᴅᴅᴇʀ Bᴏᴛ!

Hᴏᴡ ᴛᴏ Aᴅᴅᴇᴅ Wᴀᴛᴇʀᴍᴀʀᴋ ᴛᴏ ᴀ Vɪᴅᴇᴏ?

Usᴀɢᴇ: Fɪʀsᴛ Sᴇɴᴅ ᴀ JPG Iᴍᴀɢᴇ/ʟᴏɢᴏ, ᴛʜᴇɴ sᴇɴᴅ ᴀɴʏ ᴠɪᴅᴇᴏ. ʙᴇᴛᴛᴇʀ ᴀᴅᴅ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴏ ᴀ ᴍᴘ𝟺 ᴏʀ ᴍᴋᴠ ᴠɪᴅᴇᴏ.

Nᴏᴛᴇ: I ᴄᴀɴ ᴏɴʟʏ ᴘʀᴏᴄᴇss ᴏɴᴇ ᴠɪᴅᴇᴏ ᴀᴛ ᴀ ᴛɪᴍᴇ. As ᴍʏ sᴇʀᴠᴇʀ ᴀs ʜᴇʀᴏᴋᴜ, ᴍʏ ʜᴇᴀʟᴛʜ ɪs ɴᴏᴛ ɢᴏᴏᴅ. ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ɪssᴜᴇs ᴡɪᴛʜ Aᴅᴅɪɴɢ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴏ ᴀ Vɪᴅᴇᴏ, ᴛʜᴇɴ ᴘʟᴇᴀsᴇ ʀᴇᴘᴏʀᴛ ᴀᴛ Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.

Dᴇsɢɪɴᴇᴅ ʙʏ @TamilBots


"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
