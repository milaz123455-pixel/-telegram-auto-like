import asyncio
from telethon import TelegramClient

# إعدادات الجلسة
api_id = 234950140766
api_hash = '10413d2349501407662294ae7662a04c'
session_file = 'session/milaz.session'

# الرسائل المطلوبة
messages = [
    '/like 9621632878',
    '/like 6964225068',
    '/like 10519956884'
]

# الكروبات المطلوبة
groups = [
    'https://t.me/vIpMeNAx',
    'https://t.me/BNGXXXXX',
    'https://t.me/blrxcommunity',
    'https://t.me/ActionFF_bin'
]

async def send_to_group(client, group):
    for msg in messages:
        await client.send_message(group, msg)
        print(f'Sent "{msg}" to {group}')
        await asyncio.sleep(180)  # 3 دقائق بين كل رسالة داخل نفس الكروب

async def main():
    async with TelegramClient(session_file, api_id, api_hash) as client:
        for group in groups:
            await send_to_group(client, group)

if __name__ == '__main__':
    asyncio.run(main())
