import os
import time
import requests
import shutil
from flask import Flask, request, send_from_directory, render_template 
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter

app = Flask(__name__)


def delete_old_files():
    folder = 'files/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def get_subtitles(url):
    try:
        delete_old_files()
        if not url.startswith("https://www.youtube.com/") and not url.startswith("https://youtu.be/"):
            return ("Send me youtube vedio URL", 401)
        r = requests.get(url)
        if "Video unavailable" in r.text:
            return ("URL is invalid", 401)

        #downlod subtitle
        transcript = YouTubeTranscriptApi.get_transcript(url.split("=")[1])
        formatter = SRTFormatter()
        caption = formatter.format_transcript(transcript)
        with open(f'files/vedio.srt', 'w') as the_file:
            the_file.write(caption)
        subtitle_file = "files/vedio.srt"
        return (subtitle_file, 200, caption)
    except Exception as ex: 
        return (f"Server error: Somthing went wrong:  {ex}", 501)


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        url = request.form['yturl']
        res_data = get_subtitles(url)
        caption = res_data[2]#.replace("\n", "<br/>")
        # caption_for_html = res_data[2].replace("\n", "<br/>")
        if res_data[1]==200:
            return render_template('index.html', url=res_data[0], caption=caption)
        else:
            return render_template('index.html', error=res_data[0], code=res_data[1])
    else:
        return render_template('index.html')


@app.route('/download/<path:path>',methods = ['GET','POST'])
def get_files(path):
    try:
        return send_from_directory("files", path, as_attachment=True)
    except FileNotFoundError:
        return render_template('index.html', error=f"File Not Found : {path}"), 404

if __name__=="__main__":
    app.run()
