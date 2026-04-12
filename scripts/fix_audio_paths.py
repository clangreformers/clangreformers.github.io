import re
with open('_includes/shuowen-600-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_text = re.sub(
    r"onclick=\"new Audio\('/assets/audio/shuowen/([^']+)\.mp3'\)\.play\(\)\"",
    r"onclick=\"new Audio(encodeURI('/assets/audio/shuowen/\1.mp3')).play()\"",
    text
)

with open('_includes/shuowen-600-list.html', 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Applied encodeURI to all audio tags to prevent path resolving errors.")
