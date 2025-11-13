import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = int(getenv("API_ID", 30604153))
API_HASH = getenv("API_HASH", "71847be8f73b2705146cea2669130232")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 5047224084))
OWNER_USERNAME = getenv("OWNER_USERNAME", "a4x_DarkOp")
BOT_USERNAME = getenv("BOT_USERNAME", "ShrutiMusic_bot")
BOT_NAME = getenv("BOT_NAME", "𝐒ʜʀᴜᴛɪ ✘ 𝙼ᴜsɪᴄ˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "𝐒ʜʀᴜᴛɪ ✘ ᴀꜱꜱɪꜱᴛᴀɴᴛ˼")

# ── Database & logging ─────────────────────────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1002821891474))

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ──────────────────────────────────────────────────────────────
COOKIE_URL = getenv("COOKIE_URL")  # required (paste link)
API_URL = getenv("API_URL")        # optional
API_KEY = getenv("API_KEY")        # optional
DEEP_API = getenv("DEEP_API")      # optional

# ── Hosting / deployment ───────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── Git / updates ──────────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ItsMeVishal0/VishalMusic.git")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")  # needed if repo is private

# ── Support links ──────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/joinnnnn4x")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/joinnnnn4x")

# ── Assistant auto-leave ───────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── Debug ──────────────────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ─────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ── Session strings (optional) ─────────────────────────────────────────────────
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Media assets ───────────────────────────────────────────────────────────────
START_VIDS = [
    "https://files.catbox.moe/7rie2i.mp4",
    "https://files.catbox.moe/j3ba3f.mp4",
    "https://files.catbox.moe/mfeisv.mp4",
    "https://files.catbox.moe/ot88at.mp4",
    "https://files.catbox.moe/bv29a4.mp4",
    "https://files.catbox.moe/pndpqt.mp4",
    "https://files.catbox.moe/tu8l7e.mp4",
    "https://files.catbox.moe/7ygvch.mp4",
    "https://files.catbox.moe/jh55tl.mp4",
]
STICKERS = [
    "CAACAgUAAyEFAASQje-AAAI92mkOFHmOlyKv0vEpoJE6S7ZInIuPAALbFQACSZmpVI0wvAnbSnk9HgQ",
    "CAACAgQAAyEFAASQje-AAAI92GkOFFx4j5i7GwlGsRbvXBaZbgquAAIoFQACir5JU9xIMA-J9yY7HgQ",
    "CAACAgQAAyEFAASQje-AAAI91mkOFEeMiZrau4LoUgHQAuhfVUNoAAJbHQACmKWIUVKzS9qKs-juHgQ",
    "CAACAgUAAyEFAASQje-AAAI91GkOFDevrsTZ_JzDdyHdsu2VhsvHAAJ2EwAC_xfYVo5iQw7a3JPfHgQ",
    "CAACAgUAAyEFAASQje-AAAI90mkOFCn95GwjE62nWBG2o9H-FK15AAJgFQACJ_uwVMGj96qQgd3hHgQ",
    "CAACAgQAAyEFAASQje-AAAI90GkOFCDWtQkvBiumJxSoedz0NqvLAAIzFAAC9ED4UX1Ta6URzlyIHgQ",
]
HELP_IMG_URL = "https://files.catbox.moe/ff3zcd.mp4"
PING_VID_URL = "https://files.catbox.moe/qp5hjb.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/jt1my5.mp4"
STATS_VID_URL = "https://files.catbox.moe/rkzssb.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ff3zcd.mp4"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/pa0sgh.mp4"
STREAM_IMG_URL = "https://files.catbox.moe/qp5hjb.mp4"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/jt1my5.mp4"
YOUTUBE_IMG_URL = "https://files.catbox.moe/jt1my5.mp4"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── Helpers ────────────────────────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = [
    "❤️", "💞", "🩷", "💋", "🌹", "💫", "💖", "✨", "💘", "💝",
    "💕", "💗", "💓", "💟", "❣️", "🌸", "🌼", "💐", "🪷", "🌺",
    "💎", "🌙", "🌟", "🌈", "🦋", "🥰", "😍", "😘", "😚", "😻",
    "🤍", "💛", "💚", "💙", "💜", "🖤", "🤎", "🩵", "🩶", "💏",
    "💑", "💍", "💌", "💎", "🌹", "💖", "💘", "💝", "💗", "💞",
    "❤️‍🔥", "❤️‍🩹", "💓", "💟", "💃", "🕺", "🎶", "🎵", "🎧", "💫",
    "✨", "🌈", "🌸", "🌺", "🌷", "🌼", "🍀", "🥂", "🍫", "🍓",
    "🍒", "🍑", "🫶", "🤗", "🤭", "🥹", "💃", "🎀", "💄", "💅",
    "🕊️", "🐦", "🌌", "🎇", "🎆", "🌠", "🪩", "🎉", "🎊", "🥳",
    "💞", "💖", "💘", "💝", "💗", "💓", "❤️", "💋", "🌹", "✨",
    "💫", "🌈", "🦋", "💟", "💍", "💎", "🌸", "🥰", "😍", "💌"
]

AYUV = [
    "💌✨ ʜᴇʟʟᴏ {0} 💞🦋\n\n🌹 ɪᴛ'ꜱ ᴍᴇ {1} 💖💫\n\n┏━━━━━━━━━━━━━━━⧫\n┃ 💫 ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴘʟᴀᴛꜰᴏʀᴍꜱ:\n┃ 🎵 ʏᴏᴜᴛᴜʙᴇ | ꜱᴘᴏᴛɪꜰʏ | ʀᴇꜱꜱᴏ | ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ | ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ 💌\n┃\n┃ 🔥 ᴜᴘᴛɪᴍᴇ : {2} 🌙\n┃ 💖 ꜱᴇʀᴠᴇʀ sᴛᴏʀᴀɢᴇ : {3} 💫\n┃ ⚡ ᴄᴘᴜ ʟᴏᴀᴅ : {4} 💞\n┃ 🩷 ʀᴀᴍ ᴄᴏɴsᴜᴍᴘᴛɪᴏɴ : {5} 🦋\n┃ 🌈 ᴜsᴇʀs : {6} 💌\n┃ 🕊️ ᴄʜᴀᴛs : {7} 💫\n┗━━━━━━━━━━━━━━━⧫\n\n💌 ᴅᴇᴠᴇʟᴏᴩᴇʀ ➪ [𓆩☠𓆪‌ٖٖٖٖٖٖٜٖٖٖٖ𝘼4𝙭🥀𝐃𝐀𝐑𝐊─⃛͢𓆪🇴𝐏𓆩☠𓆪‌ٖٖٖٖٖٖٜٖٖٖٖ](https://t.me/a4x_DarkOp) 🌹✨",

    "💖🌹 ʜɪ {0} 💫🦋\n\n✨ ɪ'ᴍ {1} 💞 ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ 🔥\n\n┏━━━━━━━━━━━━━━━⧫\n┃ 🌟 ꜰᴇᴀᴛᴜʀᴇꜱ:\n┃ 🎵 sᴜᴘᴇʀꜰᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ 💌\n┃ 🎶 ᴘʟᴀʏ ᴍᴜꜱɪᴄ & ᴠɪᴅᴇᴏ 💫\n┃ 🌈 ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ 🕊️\n┃ 🩷 24x7 ᴍᴜꜱɪᴄ ᴄʜɪʟʟ 💖\n┃ 💌 ɴᴏ ᴘʀᴏᴍᴏ 🌹\n┃\n┃ 🔥 ᴜᴘᴛɪᴍᴇ : {2} 💫\n┃ 💖 ꜱᴇʀᴠᴇʀ sᴛᴏʀᴀɢᴇ : {3} 🌈\n┃ ⚡ ᴄᴘᴜ ʟᴏᴀᴅ : {4} 💞\n┃ 🩷 ʀᴀᴍ ᴄᴏɴsᴜᴍᴘᴛɪᴏɴ : {5} 🦋\n┃ 🌹 ᴜsᴇʀs : {6} 💌\n┃ 🕊️ ᴄʜᴀᴛs : {7} 💫\n┗━━━━━━━━━━━━━━━⧫\n\n💌 ᴅᴇᴠᴇʟᴏᴩᴇʀ ➪ [𓆩☠𓆪‌ٖٖٖٖٖٖٜٖٖٖٖ𝘼4𝙭🥀𝐃𝐀𝐑𝐊─⃛͢𓆪🇴𝐏𓆩☠𓆪‌ٖٖٖٖٖٖٜٖٖٖٖ](https://t.me/a4x_DarkOp) 💖🌸",
]

# ── Runtime structures ─────────────────────────────────────────────────────────
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ── Minimal validation ─────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

if not COOKIE_URL:
    raise SystemExit("[ERROR] - COOKIE_URL is required.")

# Only allow these cookie link formats
if not re.match(r"^https://(batbin\.me|pastebin\.com)/[A-Za-z0-9]+$", COOKIE_URL):
    raise SystemExit("[ERROR] - Invalid COOKIE_URL. Use https://batbin.me/<id> or https://pastebin.com/<id>")
