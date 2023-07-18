import pyrogram
import concurrent.futures

bot = pyrogram.Client(
    "my_bot",
    api_id=14091414,
    api_hash="1e26ebacf23466ed6144d29496aa5d5b",
    bot_token="6377609542:AAF004ZVuKIC3LREINCBhByXJ7gdP6AbTe8"
)

# Configure concurrent futures thread pool
executor = concurrent.futures.ThreadPoolExecutor()

@bot.on_message()
async def forward_message(client, message):
    owner_id = 5500572462
    message_ids = [message.id]
    from_chat_id = message.chat.id
    
    # Submit message forwarding task to the thread pool for parallel execution
    await bot.loop.run_in_executor(executor, client.forward_messages, owner_id, from_chat_id, message_ids)

if __name__ == "__main__":
    bot.run()
