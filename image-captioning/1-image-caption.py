# Install the transformers library 
# pip install transformers torch torchvision 
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Initialize the processor and model from Hugging Face
# https://huggingface.co/Salesforce/blip-image-captioning-base
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# image obtained from https://github.com/pytorch/vision/tree/main/gallery/assets
image = Image.open("assets/astronaut.jpg")

inputs = processor(image, return_tensors="pt")

outputs = model.generate(**inputs)
caption = processor.decode(outputs[0],skip_special_tokens=True)

print("Generated Caption:", caption)