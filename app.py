from flask import Flask
import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    filters,
    MessageHandler,
)
from pytube import YouTube  
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
load_dotenv()

app = Flask(__name__)



@app.route('/')
def home():
    return  "Hello, World!"

if __name__=="__main__":
    app.run(port=5200, debug=True)
