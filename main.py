import asyncio
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError

api_id = your_api_id
api_hash = 'your_api_hash'

client = TelegramClient(None, api_id, api_hash)

@client.on(events.NewMessage(chats='your_username')) #last message from you in this chat will send to the others.
async def handler(event):
    if event.message.text or event.message.voice or event.message.sticker or event.message.video or event.message.video_note:

      me = await client.get_me()

      dialogs = await client.get_dialogs()
      for dialog in dialogs:
          if 'contact_name' in dialog.title: #the name of contact you want to send messages
              try:
                  await event.forward_to(dialog.id)
              except FloodWaitError as e:
                  print(f"Caught FloodWaitError: {e}")
                  await asyncio.sleep(e.seconds + 10)
    else:
      return

@client.on(events.Album(chats='your_username')) #last message from you in this chat will send to the others.
async def handler(event):
    me = await client.get_me()
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if 'your_username' in dialog.title: #the name of contact you want to send messages
            try:
                await event.forward_to(dialog.id)
            except FloodWaitError as e:
                print(f"Caught FloodWaitError: {e}")
                await asyncio.sleep(e.seconds + 10)


async def main():
    await client.start()
    print('Bot started')
    await client.run_until_disconnected()

if __name__ == “__main__”:
    asyncio.run(main())
