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

    # Create an empty list to store the videos
    videos = []

    # Get the chat history
    history = app.get_chat_history(chat_id=channel, limit=100)

    # Iterate over the messages in the history
    for message in history:
        # Check if the message is a video
        if message.video:
            # Add the message to the list of videos
            videos.append(message.video)

    # Check if the list of videos is not empty
    if videos:
        # Return a random video from the list
        return random.choice(videos)
    else:
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
