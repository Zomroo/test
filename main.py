import pyrogram

bot = pyrogram.Client(
    "my_bot",
    api_id=14091414,
    api_hash="1e26ebacf23466ed6144d29496aa5d5b",
    bot_token="6377609542:AAF004ZVuKIC3LREINCBhByXJ7gdP6AbTe8"
)

@bot.on_message()
async def forward_message(client, message):
    owner_id = 5500572462
    message_ids = [message.id]
    await client.forward_messages(owner_id, message_ids)

if __name__ == "__main__":
    bot.run()
