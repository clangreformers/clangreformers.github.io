import os
import re
import time
from gtts import gTTS

HTML_FILE = '_includes/shuowen-600-list.html'
AUDIO_DIR = 'assets/audio/shuowen'

os.makedirs(AUDIO_DIR, exist_ok=True)

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'<span style="font-size: 2em; font-family: \'Kaiti\', serif;">([^<]+)</span>\s*<span style="font-size: 1\.1em; padding-left: 10px;">([^<]+)</span>'
matches = re.findall(pattern, text)

print(f"Found {len(matches)} characters. Generating audio files...")

for i, (char, pinyin) in enumerate(matches):
    audio_path = os.path.join(AUDIO_DIR, f"{char}.mp3")
    if not os.path.exists(audio_path):
        try:
            tts = gTTS(text=char, lang='zh-CN')
            tts.save(audio_path)
            time.sleep(0.1)
        except Exception as e:
            print(f"Error generating audio for {char}: {e}")
            
    if (i + 1) % 50 == 0:
        print(f"Processed {i + 1}/{len(matches)} characters...")

print("Audio generation complete.")

def replace_span(match):
    char = match.group(1)
    pinyin = match.group(2)
    return (
        f'<span style="font-size: 2em; font-family: \'Kaiti\', serif;">{char}</span>\n'
        f'          <span style="font-size: 1.1em; padding-left: 10px; cursor: pointer; color: #142d4c;" onclick="new Audio(encodeURI(\'/assets/audio/shuowen/{char}.mp3\')).play()" title="播放发音 / Play Audio">{pinyin} 🔊</span>'
    )

new_text = re.sub(pattern, replace_span, text)

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated HTML file successfully.")
