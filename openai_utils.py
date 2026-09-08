import openai

class ChatGPT:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    async def send_message(self, message, dialog_messages=[], chat_mode="general"):
        client = openai.AsyncOpenAI()
        response = await client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": message}]
        )
        answer = response.choices[0].message.content
        n_input_tokens = response.usage.prompt_tokens
        n_output_tokens = response.usage.completion_tokens
        return answer, (n_input_tokens, n_output_tokens), 0

    async def send_message_stream(self, message, dialog_messages=[], chat_mode="general"):
        client = openai.AsyncOpenAI()
        response = await client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": message}],
            stream=True
        )
        answer = ""
        async for chunk in response:
            if chunk.choices[0].delta.content:
                answer += chunk.choices[0].delta.content
                yield "not_finished", answer, (0, 0), 0
        yield "finished", answer, (0, 0), 0

async def transcribe_audio(audio_file):
    client = openai.AsyncOpenAI()
    transcript = await client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    return transcript.text

async def generate_images(prompt, n_images=1, size="1024x1024"):
    client = openai.AsyncOpenAI()
    response = await client.images.generate(
        prompt=prompt,
        n=n_images,
        size=size
    )
    import requests
    image_bytes = []
    for image_data in response.data:
        res = requests.get(image_data.url)
        image_bytes.append(res.content)
    return image_bytes
