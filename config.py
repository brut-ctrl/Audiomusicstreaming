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
        finalurl="https://youtu.be/Y56n7K5I_Kw"
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
    CHAT = int(os.environ.get("CHAT", "-1001367572547"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001325382108")
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
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "Y")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 60))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "eb4072cd0e4a2bb3ca7044a2e7218582")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1934836631:AAH-Tx_V9assxs-7r4FGs_Dq-vGKSdFTd0Y")     
    SESSION = os.environ.get("SESSION_STRING", "BQCcYMV8PUNNKt3C-yZqUazB3KBcKzYa9h5WbivUkwiRCfiO4u9pViVrbNBXj4J4vtKrNN6q-HlwryIpXuE011KUoGS2UEdJvS-3LfnJpqWfsxaziDKImYaCMEG7bZ2g4SjHr_-RjLjfxYrZr4tZST6rn99vBcExQzWV7Dz7RQY2flRHGxROtA94li1_T4DufW1TNFgJSRbbXWnUWJ381bbfWSF_vt6fht8cxgc4J0wwYeSAEAqSTY5ZAztj3YbymSXcNj9fcI4KkKRxfHwUYQtwPNGLHEZFlgM7vGDm-b8lmkk5f0pJ0eik0GcmQS0-fGtW6UTokGonLLkcoh0qStuzc-sZ3QA")
    playlist=[]
    msg = {}
    CONV = {}

