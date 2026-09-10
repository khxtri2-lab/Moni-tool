#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
𝐀ɴɪsʜ 𝐋ᴀᴜɴᴄʜᴇʀ — 𝐏ʏᴅʀᴏɪᴅ 3 𝐄ᴅɪᴛɪᴏɴ
"""

import sys
import os
import requests
import tempfile
import runpy

# 👇 TERA RAW URL
RAW_URL = "https://raw.githubusercontent.com/khxtri2-lab/Moni-tool/refs/heads/main/JACK.py"

BOLD_SERIF = {
    'A':'𝐀','B':'𝐁','C':'𝐂','D':'𝐃','E':'𝐄','F':'𝐅','G':'𝐆','H':'𝐇',
    'I':'𝐈','J':'𝐉','K':'𝐊','L':'𝐋','M':'𝐌','N':'𝐍','O':'𝐎','P':'𝐏',
    'Q':'𝐐','R':'𝐑','S':'𝐒','T':'𝐓','U':'𝐔','V':'𝐕','W':'𝐖','X':'𝐗',
    'Y':'𝐘','Z':'𝐙',
}
SMALL_CAPS = {
    'a':'ᴀ','b':'ʙ','c':'ᴄ','d':'ᴅ','e':'ᴇ','f':'ꜰ','g':'ɢ','h':'ʜ',
    'i':'ɪ','j':'ᴊ','k':'ᴋ','l':'ʟ','m':'ᴍ','n':'ɴ','o':'ᴏ','p':'ᴘ',
    'q':'ǫ','r':'ʀ','s':'s','t':'ᴛ','u':'ᴜ','v':'ᴠ','w':'ᴡ','x':'x',
    'y':'ʏ','z':'ᴢ',
}

def A(text):
    out = []
    for word in text.split(' '):
        if not word:
            out.append('')
            continue
        first = word[0].upper()
        rest = word[1:].lower()
        styled = BOLD_SERIF.get(first, first)
        styled += ''.join(SMALL_CAPS.get(c, c) for c in rest)
        out.append(styled)
    return ' '.join(out)


def main():
    if sys.version_info[:2] != (3, 11):
        print(f"\n✖ {A('Python 3.11 required')}. You have {sys.version_info.major}.{sys.version_info.minor}\n")
        sys.exit(1)

    print(f"✅ {A('Python 3.11 detected')}")
    print(f"⬇  {A('Downloading ANISH Checker')}...\n")

    try:
        r = requests.get(RAW_URL, timeout=20)
        if r.status_code != 200 or not r.text.strip():
            raise Exception(f"Download failed: HTTP {r.status_code}")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
            f.write(r.text)
            temp_path = f.name

        print(f"▶  {A('Running ANISH Checker')}...\n")
        runpy.run_path(temp_path, run_name="__main__")

    except Exception as e:
        print(f"❌ {A('Failed')}: {e}")

if __name__ == "__main__":
    main()
