import youtube1
import youtube2
import wc

# 시작 파일

#영상 videoID 가져오기
APIKey = input("API 키를 입력해주세요 : ")
videoId = youtube1.VideoId(APIKey)
videoIdList = videoId.getVideoId()

#videoID 사용해서 댓글 크롤링 후 csv파일로 저장
comments = youtube2.CommentsCollection(APIKey, videoIdList)
comments.getComments()

# csv파일 읽어와서 전처리 후 wc 생성
wordcloud=wc.MakeWordCloud()
wordcloud.getWordCloud()