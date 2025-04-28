import openai
import os

# Initialize OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')
openai.api_key = OPENAI_API_KEY

def generate_script(topic):
    """
    Generates a short script based on the given topic using OpenAI GPT-3.
    """
    prompt = f"Write a short script for a 30-60 second video about the following topic:\n\n{topic}\n\nScript:"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None,
        )
        script = response.choices[0].text.strip()
        return script
    except Exception as e:
        print(f"Error generating script: {e}")
        return ""

if __name__ == "__main__":
    sample_topic = "The impact of climate change on global weather patterns"
    print("Generated Script:\n")
    print(generate_script(sample_topic))
