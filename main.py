from telethon import TelegramClient
import asyncio
import time

api_id = 21623709
api_hash = '10413d2349501407662294ae7662a04c'
phone = '+963985648307'  # مش مستخدم دلوقتي

async def main():
    client = TelegramClient('milaz', api_id, api_hash)
    await client.start()  # يستخدم السيشن بدون كود SMS
    print("Logged in with session! 🚀")
    
    groups = ['vIpMeNAx', 'BNGXXXXX', 'blrxcommunity']
    messages = [
        '/like 9621632878',
        '/like 6964225068',
        '/like 10519956884'
    ]
    
    total_sent = 0
    for group in groups:
        print(f"Starting {group}")
        for msg in messages:
            try:
                await client.send_message(group, msg)
                total_sent += 1
                print(f"Sent '{msg}' to {group} ✅")
                await asyncio.sleep(60)  # دقيقة بين الرسائل
            except Exception as e:
                print(f"Error in {group}: {e}")
    
    print(f"Total sent: {total_sent}/9 ✅")
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
