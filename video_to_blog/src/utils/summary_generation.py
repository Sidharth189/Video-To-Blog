from utils.llm import llm_call

def summary_generation(transcript):
    prompt=f'''Read the below given transcript carefully and generate appropriate title for the it with label TITLE 
            and generate a brief summary that points out important points from the transcript with label SUMMARY

          transcript: {transcript}
    '''
    summary=llm_call(transcript)
    return summary