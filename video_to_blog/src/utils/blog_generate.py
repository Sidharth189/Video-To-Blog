from summary_generation import summary_generation
from llm import llm_call

def blog_generation(summary:str)->str:
    prompt=f''' You are a blog editor. Generate a blog about the below given TITLE which should include all the important points
            specified in the SUMMARY. Blog should contain 1000-1500 words.
            {summary}'''
    blog=llm_call(prompt)
    return blog
