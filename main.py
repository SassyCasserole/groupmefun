import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import OrderedDict
with open(r"C:\Users\Mordoc\Downloads\00001\16563334\message.json", encoding='utf-8') as f:

    messages = json.load(f)



keywords2 = ['fuck',
            'shit',
            'pussy',
            'crap',
            'ass',
            'dick',
            'penis',
            'balls'
        ]
keywords = ['eric', 'bru', 'ryan','mcd','evan','felipe','papito','cas','cass','pla','joe','plazek','rauert']
'''
all_text = ''
for message in messages:
    text = message['text']
    if text:
        text = text.lower()
        for keyword in keywords:
            if keyword in text:
                all_text += text

wordcloud = WordCloud(width=2000, height=1500, max_font_size=200, max_words=100, background_color="white").generate(all_text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
'''

word_freq = dict()

for message in messages:

    if message['text']:
        for word in message['text'].split():
            w = word.strip().strip(r'!()-[]{};:\,<>./?@#$%^&*_~')
            try:
                count = word_freq[w]
            except KeyError:
                word_freq[w] = 1
            else:
                word_freq[w] = count + 1

word_rank = []
word_frequency = []

with open('groupme.csv', 'w+', encoding='utf-8') as f:
    for key, value in word_freq.items():
        word_rank.append(key)
        word_frequency.append(value)
        f.write(str(key))
        f.write(',')
        f.write(str(value))
        f.write('\n')

sorted_word_freq = OrderedDict(reversed(sorted(word_freq.items())), key=lambda t: t[1], reverse=True)

limited_word_freq = dict()
count = 0
minim = 1
for key, value in sorted_word_freq.items():
    print(value)
    if isinstance(value, int):
        if value > minim:
            if key in keywords2:
                limited_word_freq.update({key: value})
                count += 1
                if count > 20000:
                    break

print(limited_word_freq)