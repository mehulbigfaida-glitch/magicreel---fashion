import base64
import io
from PIL import Image
import torch
from diffusers import StableDiffusionXLImg2ImgPipeline

# Load once per worker (RunPod Serverless pattern)
pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
).to("cuda")

def _b64_to_img(b64: str) -> Image.Image:
    return Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")

def _img_to_b64(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

def handler(event):
    """
    Expected input:
    {
      "image1": "<base64>",
      "image2": "<base64>",
      "strength": 0.6
    }
    """
    data = event.get("input", {})

    img1 = _b64_to_img(data["image1"])
    img2 = _b64_to_img(data["image2"])
    strength = float(data.get("strength", 0.6))

    # Whisk-style initial blend
    fused = Image.blend(img1, img2, strength)

    # SDXL img2img enhancement
    enhanced = pipe(
        prompt="fashion lookbook editorial, seamless fusion, soft studio lighting, clean background",
        image=fused,
        strength=0.4,
        guidance_scale=7.0,
        num_inference_steps=25
    ).images[0]

    return {
        "fused_image": _img_to_b64(enhanced)
    }
