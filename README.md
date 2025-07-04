# 🎯 YouTube Thumbnail Scraper

This is a simple Gradio-based web application that allows users to fetch and display the latest thumbnails from any public YouTube channel using its **Channel ID**.

---

## 🚀 Features

- 🔍 Fetches up to 12 recent thumbnails from a given YouTube channel
- 🖼️ Displays thumbnails in a clean, scrollable gallery
- ⚡ Fast and lightweight interface powered by [Gradio](https://www.gradio.app/)
- 🛠️ Error handling for invalid or empty channel IDs

---

## 📦 Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt
```
## 🏁 How to Run
Clone the repository:

```bash
git clone https://github.com/afianaseem/Youtube_Thumbnail_Scraper.git
cd Youtube_Thumbnail_Scraper
```
Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Launch the app:

```bash
python app.py
```
A browser window will open with the app. Enter a valid YouTube Channel ID to get thumbnails.

## 🛠️ Tech Stack
Python 3.8+
Gradio
Feedparser
Pillow
Requests

## 📁 Project Structure
```bash
Youtube_Thumbnail_Scraper/
│
├── app.py               # Main application file
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```
## 🤖 Notes
Only publicly accessible YouTube channels will return thumbnails.
Uses YouTube's public RSS feed and static thumbnail URLs
