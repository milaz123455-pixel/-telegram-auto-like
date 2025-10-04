from telethon import TelegramClient
from telethon.tl.functions.messages import AddReactionRequest
import asyncio

# قيمك الحقيقية مدمجة
api_id = 21623709
api_hash = '10413d2349501407662294ae7662a04c'
phone = '+963985648307'

async def main():
    client = TelegramClient('milaz', api_id, api_hash)
    await client.start(phone=phone)
    print("Logged in successfully! 🚀")
    
    # غير 'durov' لقناة حقيقية إذا عايز (مثل اسم قناتك بدون @)
    channel = 'durov'  # تجربة مع قناة بافل دوروف
    likes_count = 0
    async for message in client.iter_messages(channel, limit=3):  # 3 منشورات للتجربة السريعة
        try:
            await client(AddReactionRequest(peer=channel, msg_id=message.id, reaction=[{'_': 'ReactionEmoji', 'emoticon': '👍'}]))
            likes_count += 1
            print(f"Liked message ID: {message.id}")
            await asyncio.sleep(1)  # تأخير صغير عشان ما يفشلش
        except Exception as e:
            print(f"Error on message {message.id if 'message' in locals() else 'unknown'}: {e}")
    
    print(f"Total likes completed: {likes_count} ✅")
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
