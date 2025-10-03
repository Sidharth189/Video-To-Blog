from typing_extensions import TypedDict
from utils.transcript_fetch import fetch_transcript
from utils.summary_generation import summary_generation
from utils.blog_generate import blog_generation

class State(TypedDict,total=False):
    video_id:str
    transcript:str
    summary:str
    blog:str

def FetchTranscript(state:State):
    transcript=fetch_transcript(state['video_id'])
    return {'transcript':f'{transcript}'}

def SummaryGenerate(state:State):
    summary=summary_generation(state['transcript'])
    return {'summary':f'{summary}'}

def BlogGenerate(state:State):
    blog=blog_generation(state['summary'])
    return {'blog':f'{blog}'}



