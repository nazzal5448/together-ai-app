from together import Together
import os
import dotenv

dotenv.load_dotenv()
api = os.getenv("TOGETHER_API_KEY")


def generate(prompts:list[str]):
    
    client = Together(api_key=api)
    json_responses = []
    for i, prompt in enumerate(prompts):
        if i == 0:
            WIDTH = 1080
            HEIGHT = 1072
        else:
            WIDTH = 1200
            HEIGHT = 624

        response = client.images.generate(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell-Free",
            width=WIDTH,
            height=HEIGHT,
            steps=4,
            n=1,
            response_format="b64_json",
            stop=[]
        )
        json_responses.append(response.data[0].b64_json)
    return json_responses


if __name__ == "__main__":
    import base64
    from PIL import Image
    from io import BytesIO
    responses = generate(["A linkedin style flowchart of how ai agents are made."])
    
    for i, response in enumerate(responses):
        # Decode the base64 string
        image_data = base64.b64decode(response)
        image = Image.open(BytesIO(image_data))
        image.save(f"output_image_{i}.png")