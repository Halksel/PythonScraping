import MeCab
import re
from gensim.models import word2vec
import logging

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

bindata = open('kokoro.txt.sjis', 'rb').read()
text = bindata.decode('shift_jis')

text = re.split(r'\-{5,}', text)[2]
text = re.split(r'底本：', text)[0]
text = text.replace('｜', '')
text = text.replace('　', '')
text = re.sub(r'《.+?》', '', text)
text = re.sub(r'［＃.+?］', '', text)
text = text.strip()

result = []
m = MeCab.Tagger()

lines = text.split('\r\n')

for line in lines:
    keywords = m.parse(line)
    rs = []
    for row in keywords.split('\n'):
        word = row.split('\t')[0]
        if word == 'EOS':
            break
        else:
            pos = row.split('\t')[1].split(',')[0]
            if pos == '名詞':
                rs.append(word)
    rl = (' '.join(rs)).strip()
    result.append(rl)

wakati_file = 'kokoro.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(result))

data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('kokoro.model')
print('ok')
