import MeCab
from wordcloud import WordCloud

data = open("data.txt","rb").read()
text = data.decode('utf-8')

mecab = MeCab.Tagger("-ochasen")
node = mecab.parseToNode(text)

data_text = []

while node:
    word = node.surface
    hinnsi = node.feature.split(",")[0]
    if hinnsi in ["動詞","副詞","形容詞","名詞"]:
        data_text.append(word)
    else:
        print("|{0}|の品詞は{1}だから追加しない".format(node.surface,node.feature.split(",")[0]))
        print("-"*35)
    node = node.next

text = ' '.join(data_text)
#除外ワード
stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']
wordcloud = WordCloud(font_path='/System/Library/Fonts/ヒラギノ明朝 ProN.ttc',width=480, height=300,background_color='white',stopwords=set(stop_words))
# テキストからワードクラウドを生成する。
wordcloud.generate(text)
# ファイルに保存する。
wordcloud.to_file('wordcloud.png')