# AI Video Generation Tool

## Objective
Create an AI-based application that generates videos by scraping trending news articles.

## Project Overview
This project scrapes trending news articles or social media hashtags, generates a short script based on the topic, and creates 30-60 second videos with text overlays and images based on the script.

## Technologies and Libraries
- Python 3
- News scraping: `newsapi-python` or `requests` + `BeautifulSoup`
- Script generation: OpenAI GPT API or a simple custom script generator
- Video generation: `moviepy` for video editing and text overlays, `Pillow` for image processing
- Image sourcing: Unsplash API or Pexels API for relevant images
- Optional: Use generative AI video tools if available

## Project Structure
- `scraper.py`: Scrapes trending news articles or hashtags
- `script_generator.py`: Generates a short script from the topic
- `video_generator.py`: Creates videos with text overlays and images
- `main.py`: Orchestrates the pipeline
- `requirements.txt`: Python dependencies
- `report.md`: Report explaining the steps followed
- `output/`: Directory to save generated videos

## Implementation Plan
1. Implement `scraper.py` to fetch trending news articles or hashtags.
2. Implement `script_generator.py` to generate a short script from the scraped content.
3. Implement `video_generator.py` to create a 30-60 second video with text overlays and images.
4. Implement `main.py` to run the full pipeline.
5. Create `report.md` documenting the process and results.
6. Test the tool and generate sample videos.

## Follow-up Steps
- Install required Python packages.
- Run the tool to generate videos.
- Review and refine the script and video generation quality.

Please confirm if you approve this plan so I can proceed with implementation.
