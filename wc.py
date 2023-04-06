from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt

class MakeWordCloud:
    def getWordCloud(self):
        
        # 뭐.. 로딩중 같은거?ㅎㅎ
        print ('-'*20)

        # 파일 읽기
        with open('data.csv', 'r', encoding='utf-8') as f:
            data = f.read()

        okt = Okt()

        # 명사태깅
        OKT_Noun = okt.nouns(data)
        words = [n for n in OKT_Noun if len(n) > 1] # 단어의 길이가 1개인 것은 제외

        #불용어 제거 (불용어 사전 만들고 싶으면 쓰세용)
        # stop_words = ['존나', '어쩔']
 
        # 빈도 수 세기
        counts = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 collection타입의 데이터를 구함

        #wc 생성
        wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
        gen = wc.generate_from_frequencies(counts)
        plt.figure()
        plt.imshow(gen)
        wc.to_file('result.png')
        plt.show()