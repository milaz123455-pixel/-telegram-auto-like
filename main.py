from telethon import TelegramClient
import asyncio
import time  # للتأخير

# قيمك الحقيقية
api_id = 21623709
api_hash = '10413d2349501407662294ae7662a04c'
phone = '+963985648307'

async def main():
    client = TelegramClient('milaz', api_id, api_hash)
    await client.start(phone=phone)
    print("Logged in successfully! 🚀")
    
    # الـ3 جروبات (أسماء بدون t.me/، غيرها لو لازم)
    groups = ['vIpMeNAx', 'BNGXXXXX', 'blrxcommunity']
    
    # الـ3 رسائل المحددة
    messages = [
        '/like 9621632878',
        '/like 6964225068',
        '/like 10519956884'
    ]
    
    total_sent = 0
    for group in groups:
        print(f"Starting to send to group: {group}")
        for msg in messages:
            try:
                await client.send_message(group, msg)
                total_sent += 1
                print(f"Sent '{msg}' to {group} ✅")
                await asyncio.sleep(60)  # تأخير دقيقة (60 ثانية) بين الرسائل داخل الجروب
            except Exception as e:
                print(f"Error sending '{msg}' to {group}: {e}")
        
        print(f"Finished group {group}. Moving to next...")  # بعد كل جروب، انتقل للتاني بدون تأخير إضافي (لو تبي تأخير بين الجروبات، أضف time.sleep(60) هون)
    
    print(f"Total messages sent: {total_sent} out of 9 ✅ – Will repeat in 24 hours!")
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
