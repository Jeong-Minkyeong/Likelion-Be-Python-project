from googleapiclient.discovery import build

class VideoId:

    # APIkey로 미리 bulid
    def __init__(self, APIKey):
        self.DEVELOPER_KEY=APIKey
        YOUTUBE_API_SERVICE_NAME='youtube'
        YOUTUBE_API_VERSION='v3'
        self.youtube=build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=self.DEVELOPER_KEY)

    def getVideoId(self):
        
        # 원하는 영상 videoid받기
        search = input("원하는 영상의 videoId를 입력해주세요 : ")
        return(search)