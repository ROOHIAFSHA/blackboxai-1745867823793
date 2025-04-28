import scraper
import script_generator
import video_generator
import os

def main():
    # Step 1: Scrape trending news articles
    trending_news = scraper.get_trending_news()
    if not trending_news:
        print("No trending news found.")
        return

    for idx, article in enumerate(trending_news):
        print(f"Processing article {idx+1}: {article['title']}")

        # Step 2: Generate script based on article title and description
        topic = article['title'] + ". " + (article['description'] or "")
        script = script_generator.generate_script(topic)
        if not script:
            print("Failed to generate script.")
            continue

        # Step 3: Prepare image URLs (for simplicity, use article URL as placeholder)
        # In real implementation, fetch relevant images from APIs like Unsplash or Pexels
        image_urls = [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            "https://images.unsplash.com/photo-1462331940025-496dfbfc7564",
            "https://images.unsplash.com/photo-1500534623283-312aade485b7"
        ]

        # Step 4: Generate video
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        video_path = os.path.join(output_dir, f"video_{idx+1}.mp4")
        video_generator.generate_video(script, image_urls, output_path=video_path)

        print(f"Video saved to {video_path}")

if __name__ == "__main__":
    main()
