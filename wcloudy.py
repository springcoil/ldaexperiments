import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from os import path
# join tweets to a single string
d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'data/corpus.txt')).read()

stopwords = STOPWORDS.copy()
stopwords.add("and")
stopwords.add("or")
stopwords.add("s")
stopwords.add("ADVICE")
stopwords.add("ANALYTICS")
stopwords.add("WISH")
stopwords.add("GO")
stopwords.add("etc")
stopwords.add("don")
stopwords.add("PHD")
stopwords.add("t")
stopwords.add("one")
stopwords.add("WISH")
stopwords.add("BIG")
stopwords.add("also")
stopwords.add("need")
stopwords.add("particular")


wc = WordCloud(max_font_size=50, max_words=1000, stopwords=stopwords, margin=10, 
               random_state=3).generate(text)

plt.imshow(wc)
plt.axis('off')
plt.savefig('my_analysis_wordcloud_corpus2.png', dpi=300)
plt.show()