#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
𝐀ɴɪsʜ — 𝐃ᴜᴀʟ 𝐋ᴀᴜɴᴄʜᴇʀ (𝐏ʏᴅʀᴏɪᴅ 3 𝐄ᴅɪᴛɪᴏɴ)
User selects which tool to run.
"""

import sys
import os
import time
import requests
import tempfile
import runpy

# ============================================================
# 🔗 RAW URLs — dono same repo mein hain
# ============================================================
URL_SLOW = "https://raw.githubusercontent.com/khxtri2-lab/Moni-tool/refs/heads/main/JACK.py"
URL_FAST = "https://raw.githubusercontent.com/khxtri2-lab/Moni-tool/refs/heads/main/67.py"

# ============================================================
# 🎨 𝐀ɴɪsʜ 𝐅ᴏɴᴛ
# ============================================================
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

# ============================================================
# 🎨 𝐂ᴏʟᴏʀs
# ============================================================
INFERNO_RED = "\033[1;35m"
INFERNO_ORANGE = "\033[1;36m"
INFERNO_GOLD = "\033[1;33m"
W = "\033[1;37m"
RESET = "\033[0m"
B = "\033[1m"
GREEN = "\033[1;32m"
DIM = "\033[2;37m"

# ============================================================
# 🎬 𝐀ɴɪᴍᴀᴛᴇᴅ 𝐋ᴏᴀᴅᴇʀ
# ============================================================
def animated_loader(text, duration=1.2):
    frames = ["⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻", "⣽"]
    end_time = time.time() + duration
    i = 0
    styled = A(text)
    while time.time() < end_time:
        sys.stdout.write(f"\r{INFERNO_RED}{B}✦ {styled} {frames[i % len(frames)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{GREEN}{B}✓ {styled} {A('DONE')}!{RESET}\n")
    sys.stdout.flush()

# ============================================================
# 🎨 𝐔𝐈
# ============================================================
def _ui_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def _ui_brand():
    return f"""{INFERNO_RED}{B}
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│              {W}{A('ANISH')}{INFERNO_RED}                                       │
│          {W}{A('DUAL LAUNCHER')}{INFERNO_RED}   /   {W}{A('PREMIUM')}{INFERNO_RED}            │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
{RESET}"""

def _ui_section(title):
    return (
        f"{INFERNO_ORANGE}{B}╭─ {title.upper()} "
        f"{'─' * max(2, 54 - len(title))}╮{RESET}\n"
    )

# ============================================================
# 🚀 𝐃ᴏᴡɴʟᴏᴀᴅ + 𝐑ᴜɴ
# ============================================================
def download_and_run(url, tag):
    try:
        print(f"{INFERNO_ORANGE}{B}⬇ {A('Downloading')} {A(tag)}...{RESET}")
        r = requests.get(url, timeout=20)
        if r.status_code != 200 or not r.text.strip():
            raise Exception(f"HTTP {r.status_code}")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
            f.write(r.text)
            temp_path = f.name

        animated_loader(f"Running {tag}", 1.0)
        _ui_clear()
        runpy.run_path(temp_path, run_name="__main__")

    except Exception as e:
        print(f"{INFERNO_RED}{B}❌ {A('Failed')}: {e}{RESET}")

# ============================================================
# ▶ 𝐌ᴀɪɴ
# ============================================================
def main():
    if sys.version_info[:2] != (3, 11):
        print(f"\n{INFERNO_RED}{B}✖ {A('Python 3.11 required')}. You have {sys.version_info.major}.{sys.version_info.minor}{RESET}\n")
        sys.exit(1)

    _ui_clear()
    print(_ui_brand())
    print(_ui_section("Select Tool"))
    print(f"""{INFERNO_RED}{B}
│  {W}[1]  {A('MONI FILE')}  {DIM}(SLOW){RESET}{INFERNO_RED}{B}
│  {INFERNO_GOLD}[2]  {A('FAST FILE WITH POST')}  {DIM}(FAST){RESET}{INFERNO_RED}{B}
│
{INFERNO_ORANGE}{B}╰──────────────────────────────────────────────────────────────╯
{RESET}""")

    choice = input(f"{INFERNO_ORANGE}{B}╰─➤ {RESET}").strip()

    while choice not in ["1", "2"]:
        print(f"{INFERNO_RED}{B}  ✖ Invalid — enter 1 or 2{RESET}")
        choice = input(f"{INFERNO_ORANGE}{B}╰─➤ {RESET}").strip()

    if choice == "1":
        animated_loader("Loading MONI File", 0.8)
        download_and_run(URL_SLOW, "MONI File")
    else:
        animated_loader("Loading Fast File", 0.8)
        download_and_run(URL_FAST, "Fast File")

if __name__ == "__main__":
    main()
