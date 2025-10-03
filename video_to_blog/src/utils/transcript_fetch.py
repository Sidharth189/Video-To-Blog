from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(url):
    video_id=url.split("watch?v=")[1]
    
    yt_api=YouTubeTranscriptApi()
    transcript=yt_api.fetch(video_id)
    
    transcript_text=""
    for snippet in transcript:
        transcript_text+=snippet.text

    return transcript_text
