# Video to Blog
## Description
Video to Blog is a Python-based project that utilizes natural language processing (NLP) and large language models (LLMs) to generate blog posts from video transcripts. The project leverages the YouTube Transcript API to fetch video transcripts and the LLaMA model to generate summaries and blog posts.

## Prerequisites
* Python 3.8+
* `youtube_transcript_api` library
* `langchain` library
* `langgraph` library
* `dotenv` library
* A `.env` file with the following environment variables:
	+ `GROQ_API_KEY` (for LLaMA model)
* A compatible LLaMA model (e.g., `llama-3.1-8b-instant`)

## Installation
1. Clone the repository: `git clone https://github.com/your-username/video_to_blog.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Create a `.env` file with the required environment variables
4. Run the project: `python video_to_blog/src/main.py`

## Usage
To generate a blog post from a video transcript, simply invoke the `graph` object with a `video_id`:
```python
video_id = 'https://www.youtube.com/watch?v=iWS9ogMPOI0'
print(graph.invoke({'video_id': video_id})['blog'])
```
This will fetch the video transcript, generate a summary, and then generate a blog post based on the summary.

## API Documentation
The project uses the following APIs:

* YouTube Transcript API: `youtube_transcript_api`
* LLaMA model: `langchain`

The `nodes` module defines the following functions:

* `FetchTranscript`: fetches a video transcript from the YouTube Transcript API
* `SummaryGenerate`: generates a summary from a transcript using the LLaMA model
* `BlogGenerate`: generates a blog post from a summary using the LLaMA model

## Testing
To test the project, you can use the following example:
```python
video_id = 'https://www.youtube.com/watch?v=iWS9ogMPOI0'
print(graph.invoke({'video_id': video_id})['blog'])
```
This will generate a blog post from the specified video transcript.

## Deployment
To deploy the project, you can use a Python web framework such as Flask or Django to create a RESTful API that accepts video IDs and returns generated blog posts.

### Example Deployment using Flask
```python
from flask import Flask, request, jsonify
from workflow import graph

app = Flask(__name__)

@app.route('/generate_blog', methods=['POST'])
def generate_blog():
    video_id = request.json['video_id']
    blog_post = graph.invoke({'video_id': video_id})['blog']
    return jsonify({'blog_post': blog_post})

if __name__ == '__main__':
    app.run(debug=True)
```
This example creates a Flask API that accepts a `video_id` in the request body and returns the generated blog post in the response.

Note: This project requires a compatible LLaMA model and a `.env` file with the required environment variables. Make sure to update the `requirements.txt` file and the `.env` file accordingly.