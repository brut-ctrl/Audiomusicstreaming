#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
C_PLAY=False
Y_PLAY=False
STREAM=os.environ.get("STREAM_URL", "https://t.me/punyamipan/1073")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
regex_ = r"http.*"
match_ = re.match(regex_,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[-1]
elif STREAM.startswith("https://t.me/punyamipan"):
    try:
        msg_id=STREAM.split("/", 4)[4]
        finalurl=int(msg_id)
        Y_PLAY=True
    except:
        finalurl="http://stream.denger.in:8888/dmi"
        print("Unable to fetch youtube playlist, starting Denger.in FM")
        pass
elif match_:
    finalurl=STREAM 
else:
    C_PLAY=True
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '712147852 1408440765 1944787421 1820831401 1945910995 1909021805 1605366945 1880475785')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '7363937'))
    CHAT = int(os.environ.get("CHAT", "-1001356822547"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001356822547")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    CPLAY=C_PLAY
    YPLAY=Y_PLAY
    SHUFFLE=bool(os.environ.get("SHUFFLE", True))
    DELETE_HISTORY=bool(os.environ.get("DELETE_HISTORY", True))
    LIMIT=int(os.environ.get("LIMIT", 1500))
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 90))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "eb4072cd0e4a2bb3ca7044a2e7218582")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1934836631:AAH-Tx_V9assxs-7r4FGs_Dq-vGKSdFTd0Y")     
    SESSION = os.environ.get("SESSION_STRING", "BQA59OUEm6HjmJ98leLripho9oBGdzu8oDAFfe2rH_slx1gf4YhrZGS8hpXMQNNEdQyXBrTuBVVoJGDKaalUs3HAxdMiBnsf-Opp5I0HxJ2MPGHqx_-1xsvz2M_X_PYIZ8fXMMSbKsGBSVUuqoxRjRIuKaJS4AfXyARkxLb0pGGSmZJyU3lMWisFnA1g1ll2mCjOhPX9adv2kc4k7g1IM7TqQhrune0vBfcRVKAfJh7yXHRkDXKrJpN00TH5EcwJC0KZEyW9R7-YksPiixFzjWr6X-NbhwkcBbfDaLCjQMmKHYjP2zwUyU0w65hpMQkG2F0L9qExvCeclHaFmPxtuhrvc-sZ3QA")
    playlist=[]
    msg = {}
    CONV = {}

