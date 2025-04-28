import os
from moviepy.editor import TextClip, ImageClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image
import requests
from io import BytesIO

def download_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def create_text_clip(text, duration, fontsize=40, color='white', size=(1280, 720)):
    txt_clip = TextClip(text, fontsize=fontsize, color=color, size=size, method='caption', align='center')
    txt_clip = txt_clip.set_duration(duration)
    return txt_clip

def create_image_clip(image, duration, size=(1280, 720)):
    img_clip = ImageClip(image).set_duration(duration)
    img_clip = img_clip.resize(newsize=size)
    return img_clip

def generate_video(script, image_urls, output_path='output/video.mp4'):
    """
    Generates a video with text overlays and images based on the script.
    script: str - The script text to display.
    image_urls: list - List of image URLs to include in the video.
    output_path: str - Path to save the generated video.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Split script into sentences for text clips
    sentences = [s.strip() for s in script.split('.') if s.strip()]
    duration_per_sentence = max(2, 30 // len(sentences))  # Approximate duration per sentence

    clips = []
    for i, sentence in enumerate(sentences):
        text_clip = create_text_clip(sentence + '.', duration_per_sentence)
        if i < len(image_urls):
            img = download_image(image_urls[i])
            if img:
                img_clip = create_image_clip(img, duration_per_sentence)
                composite = CompositeVideoClip([img_clip, text_clip.set_position('center')])
                clips.append(composite)
            else:
                clips.append(text_clip)
        else:
            clips.append(text_clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    sample_script = "Climate change is affecting global weather patterns. Extreme weather events are becoming more frequent. It is important to take action now."
    sample_images = [
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "https://images.unsplash.com/photo-1462331940025-496dfbfc7564",
        "https://images.unsplash.com/photo-1500534623283-312aade485b7"
    ]
    generate_video(sample_script, sample_images)
