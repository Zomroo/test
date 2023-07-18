from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# Initialize your bot using Pyrogram
api_id = 14091414
api_hash = '1e26ebacf23466ed6144d29496aa5d5b'
bot_token = '6377609542:AAF004ZVuKIC3LREINCBhByXJ7gdP6AbTe8'

app = Client('my_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a function to get a random video from the channel
def get_random_video_from_channel():
    # Specify the channel username or id
    channel = '-1001226899835'

    # Get the messages from the channel
    messages = app.search_messages(chat_id=channel, filter='video', limit=100)

    # Check if the list of messages is not empty
    if messages.total_count > 0:
        # Get a random message from the messages
        random_message = random.choice(messages.messages)

        # Check if the random message is a video
        if random_message.video:
            # Return the random video
            return random_message.video

    # Return None if no videos are available
    return None

# Handler for /start command
@app.on_message(filters.command('start'))
def start_command(client, message):
    # Create an inline keyboard
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Get Random Video", callback_data='get_video')]
    ])

    # Send a message with the inline keyboard
    client.send_message(
        chat_id=message.chat.id,
        text="Click the button to get a random video:",
        reply_markup=keyboard
    )

# Handler for inline keyboard button
@app.on_callback_query()
def button_click(client, query):
    if query.data == 'get_video':
        # Get a random video from the channel
        video = get_random_video_from_channel()

        if video:
            # Forward the video to the user without quoting
            client.send_video(
                chat_id=query.message.chat.id,
                video=video.file_id,
                caption=video.caption
            )
        else:
            # Send an error message if no videos are available
            client.send_message(
                chat_id=query.message.chat.id,
                text="Sorry, no videos are available at the moment."
            )

        # Answer the callback query to remove the loading state on the button
        query.answer()

# Start the bot
app.run()
