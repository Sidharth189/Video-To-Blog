# Video-To-Blog
================

A Python-based project that converts video content into blog posts using Large Language Models (LLMs) and natural language processing techniques.

## Description
This project utilizes the YouTube Transcript API to fetch video transcripts, which are then summarized and used to generate blog posts. The blog generation process involves prompting an LLM to create a 1000-1500 word blog post based on the summary.

## Prerequisites
* Python 3.8+
* `youtube_transcript_api` library
* `langchain` library
* `langgraph` library
* `dotenv` library
* A `.env` file with the necessary environment variables (e.g., API keys)

## Installation
1. Clone the repository: `git clone https://github.com/your-username/video-to-blog.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Create a `.env` file with the necessary environment variables
4. Load the environment variables: `python -m dotenv load_dotenv`

## Usage
To generate a blog post from a video, simply invoke the `graph` object with the video URL:
```python
from video_to_blog.src.workflow import graph

video_id = 'https://www.youtube.com/watch?v=iWS9ogMPOI0'
blog_post = graph.invoke({'video_id': video_id})['blog']
print(blog_post)
```
This will fetch the video transcript, generate a summary, and create a blog post based on the summary.

## API Documentation
The project uses the following APIs:

* YouTube Transcript API: `youtube_transcript_api`
* Langchain API: `langchain`
* Langgraph API: `langgraph`

## Testing
To test the project, you can use the following example:
```python
from video_to_blog.src.workflow import graph

video_id = 'https://www.youtube.com/watch?v=iWS9ogMPOI0'
blog_post = graph.invoke({'video_id': video_id})['blog']
print(blog_post)
```
This will test the entire workflow, from fetching the video transcript to generating the blog post.

## Deployment
To deploy the project, you can use a cloud platform such as AWS or Google Cloud. You will need to:

1. Create a cloud function or API endpoint
2. Install the required libraries and dependencies
3. Load the environment variables
4. Invoke the `graph` object with the video URL

Note: This project is for demonstration purposes only and may require additional setup and configuration for production use.