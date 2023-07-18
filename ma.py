from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_BOT_TOKEN' with your own values
api_id = '14091414'
api_hash = '1e26ebacf23466ed6144d29496aa5d5b'
bot_token = '6377609542:AAF004ZVuKIC3LREINCBhByXJ7gdP6AbTe8'


# Replace 'YOUR_CHANNEL_ID' with your database channel ID
channel_id = '-1001226899835'

# Create a Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Command handler for /start command
@app.on_message(filters.command("start"))
def start(bot, update):
    # Create an inline keyboard with a single button
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Get Random Video", callback_data='get_random_video')]
    ])

    # Send a message with the inline keyboard to the user
    bot.send_message(
        chat_id=update.chat.id,
        text="Click the button to get a random video.",
        reply_markup=keyboard
    )

# Callback handler for inline keyboard button
@app.on_callback_query()
def callback(bot, update):
    if update.data == 'get_random_video':
        # Get a random video from the database channel
        videos = bot.get_chat_history(chat_id=channel_id, limit=100).videos
        if videos:
            random_video = random.choice(videos)
            # Forward the random video to the user
            bot.forward_messages(
                chat_id=update.message.chat.id,
                from_chat_id=channel_id,
                message_ids=random_video.message_id
            )
        else:
            # Send an error message if there are no videos in the database channel
            bot.send_message(
                chat_id=update.message.chat.id,
                text="No videos found in the database channel."
            )

# Run the bot
app.run()
