# AI Video Generation Tool - Report

## Objective
The objective of this project was to create an AI-based application that generates videos by scraping trending news articles, generating scripts, and creating videos with text overlays and images.

## Steps Followed

1. **Scraping Trending News Articles**
   - Used the NewsAPI to fetch top trending news articles.
   - Implemented in `scraper.py`.
   - Fetched article titles, descriptions, and URLs.

2. **Script Generation**
   - Used OpenAI GPT-3 API to generate short scripts based on the news topics.
   - Implemented in `script_generator.py`.
   - The script is designed to be 30-60 seconds long.

3. **Video Generation**
   - Used `moviepy` and `Pillow` libraries to create videos.
   - Implemented in `video_generator.py`.
   - Videos include text overlays of the script and relevant images.
   - Images are fetched from URLs (sample Unsplash images used).

4. **Pipeline Orchestration**
   - Implemented in `main.py`.
   - Orchestrates scraping, script generation, and video creation.
   - Saves generated videos in the `output/` directory.

## Deliverables
- Source code files: `scraper.py`, `script_generator.py`, `video_generator.py`, `main.py`
- Generated videos saved in the `output/` directory.
- This report explaining the steps followed.

## Future Improvements
- Integrate image search APIs (e.g., Unsplash, Pexels) to fetch relevant images dynamically.
- Enhance script generation with more context and creativity.
- Add audio narration to videos.
- Improve video styling and transitions.
- Deploy as a web application with user interface.

## Usage
- Set environment variables for API keys: `NEWSAPI_KEY` and `OPENAI_API_KEY`.
- Install dependencies from `requirements.txt`.
- Run `python main.py` to generate videos.
