import gradio as gr
import feedparser
import requests
from PIL import Image
from io import BytesIO

def get_thumbnails(channel_id):
    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        return ["No thumbnails found. Please check the channel ID."]

    thumbnails = []
    for entry in feed.entries[:12]:  # Limit to first 12 videos
        video_id = entry.yt_videoid
        title = entry.title
        thumb_url = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        try:
            response = requests.get(thumb_url)
            image = Image.open(BytesIO(response.content))
            image.title = title
            thumbnails.append(image)
        except:
            continue
    return thumbnails if thumbnails else ["Failed to fetch thumbnails."]

with gr.Blocks(title="YouTube Thumbnails Scraper") as app:
    gr.Markdown("## 🔍 YouTube Thumbnail Scraper\nEnter a **YouTube Channel ID** to fetch video thumbnails.")
    with gr.Row():
        channel_id_input = gr.Textbox(label="YouTube Channel ID", value="UCoa_TW1XDNOm1aY3JdfkApQ")
        run_button = gr.Button("Get Thumbnails")

    output_gallery = gr.Gallery(label="Thumbnails", columns=4, height="auto")

    run_button.click(fn=get_thumbnails, inputs=channel_id_input, outputs=output_gallery)

app.launch()
