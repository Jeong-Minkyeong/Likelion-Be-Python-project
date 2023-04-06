import pandas
from googleapiclient.discovery import build
import warnings 
warnings.filterwarnings('ignore')

class CommentsCollection:
    def __init__(self, APIKey, VideoId):
        self.comments = list()
        self.api_obj = build('youtube', 'v3', developerKey=APIKey)
        self.video_id = VideoId
    
    def getComments(self):

        #commentThreads로 댓글 가져오기
        response_1 = self.api_obj.commentThreads().list(part='snippet', videoId=self.video_id, maxResults=100).execute()

        while response_1:
            for item in response_1['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                self.comments.append([comment])
        
            if 'nextPageToken' in response_1:
                response_1 = self.api_obj.commentThreads().list(part='snippet', videoId=self.video_id, pageToken=response_1['nextPageToken'], maxResults=100).execute()
            else:
                break
        

        # csv 파일로 변환
        df = pandas.DataFrame(self.comments)
        df.to_csv('data.csv', header=['comment'], index=None)


        # videos로 영상 정보 가져오기
        response_2 = self.api_obj.videos().list(part='snippet, statistics', id = self.video_id).execute()

        print("영상 제목: ",  response_2['items'][0]['snippet']['title'])    
        print("영상 설명: ",  response_2['items'][0]['snippet']['description'])
        print("채널명: ",    response_2['items'][0]['snippet']['channelTitle'])
        print("조회수: ",  response_2['items'][0]['statistics']['viewCount'])

        return 
    
  