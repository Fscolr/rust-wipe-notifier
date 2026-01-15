import requests
import vk_api
import os
import sys
from datetime import datetime

# 📢 Сообщение о вайпе (ЗАМЕНИ IP и Discord ссылку!)
message = """
🗑️ ВАЙП НА RAST! 🗑️

✅ Карта обновлена
⚡️ Свежий лут по всей карте  
🎮 IP: ТВОЙ.СЕРВЕР.IP:28015
📱 Discord: discord.gg/ТВОЯ_ССЫЛКА

Залетайте скорее! 🔥
"""

print(f"🚀 [{datetime.now()}] Отправляем уведомления...")

# 1️⃣ DISCORD Webhook
if os.getenv('DISCORD_WEBHOOK'):
    try:
        discord_data = {
            "content": message,
            "username": "RAST Wipe Bot 🗑️",
            "avatar_url": "https://i.imgur.com/rust_logo.png"
        }
        response = requests.post(os.getenv('DISCORD_WEBHOOK'), json=discord_data)
        print(f"✅ Discord: {response.status_code}")
    except Exception as e:
        print(f"❌ Discord: {e}")

# 2️⃣ TELEGRAM Bot
if os.getenv('TELEGRAM_TOKEN') and os.getenv('TELEGRAM_CHAT_ID'):
    try:
        tg_url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage"
        tg_data = {
            'chat_id': os.getenv('TELEGRAM_CHAT_ID'),
            'text': message,
            'parse_mode': 'Markdown'
        }
        response = requests.post(tg_url, data=tg_data)
        print(f"✅ Telegram: {response.status_code}")
    except Exception as e:
        print(f"❌ Telegram: {e}")

# 3️⃣ VK Группа
if os.getenv('VK_TOKEN') and os.getenv('VK_GROUP_ID'):
    try:
        vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
        vk = vk_session.get_api()
        vk.wall.post(
            owner_id=int(os.getenv('VK_GROUP_ID')),
            from_group=1,
            message=message
        )
        print("✅ VK: Отправлено!")
    except Exception as e:
        print(f"❌ VK: {e}")

print("🎉 ВСЕ уведомления отправлены!")
sys.exit(0)
