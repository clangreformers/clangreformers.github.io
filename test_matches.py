import re

with open('_includes/shuowen-600-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<span style="font-size: 2em; font-family: \'Kaiti\', serif;">([^<]+)</span>', text)
print('Total characters:', len(matches))
print('First 10:', matches[:10])
