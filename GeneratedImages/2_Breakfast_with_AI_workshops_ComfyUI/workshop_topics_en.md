# Topics

1. Hardware Requirements for Running ComfyUI
	1. **Amateur Applications.** ComfyUI can run even on older GeForce cards. It's not efficent, but it works!
	2. **It's important not to get caught up in the loading bar simulator.** Long image generation times don't encourage experimentation and creation of new materials.
	3. **Commercial and semi-professional applications require NVIDIA cards, preferably from the RTX 30xx series and up.** This is due to the architecture - only from these cards onward did the company introduce solutions supporting generative artificial intelligence.
	4. **VRAM is crucial, but RAM shouldn't be neglected either.** With 8 GB VRAM, you can work on small processes, but more complex ones require more memory - professionally, you need about 12 GB VRAM. For RAM, 32 GB is considered standard. Why? Models are first loaded into RAM, then transferred to the graphics card. ComfyUI can move models between memories to offload the card when a model is no longer needed.
	5. **NVIDIA's dominance stems from using Compute Unified Device Architecture technology.** This is a way to facilitate work with the graphics card, allowing parallel creation of different image fragments. Large tasks are divided into smaller parts and executed in parallel.
	6. **CUDA is not available on Macs and AMD cards.** For Macs, I've read about implementations where ComfyUI generated images in less than 2 minutes, but these were M3 Max processors with large amounts of RAM.
	7. **The graphics card needs care, especially when working with image generation.** Maintaining a reasonable temperature allows for less wear on the card and ensures it will last longer.
	8. **When calculating costs related to image generation, various factors must be considered** - from electricity prices to hardware depreciation.

2. Where to Get ComfyUI?
	1. **The best way is to use the official [repository](https://github.com/comfyanonymous/ComfyUI).** Just download and extract the repository.
	2. **I also recommend checking out [Stability Matrix](https://github.com/LykosAI/StabilityMatrix).** It's a very good interface that makes using local image generation tools easier. Many things can be handled with just one click.
	3. **What to choose? ComfyUI or SD Web UI?** It depends on your needs. ComfyUI allows for great control over the image generation process - you actually have to design this process. This has its advantages. SD Web UI is a simple interface, ready to use right after downloading the model, but it's very rarely updated.

3. Where to Get Models?
	1. **Currently, there are two good places: [Hugging Face](https://huggingface.co/) and [CivitAI](https://civitai.com/).** Models are stored in both places - sometimes a model is in one place but not in the other. You need to search.
	2. **CivitAI is particularly popular.** It's even integrated with Stability Matrix - you need to provide an API key there and can easily download models.
	3. **Model card, important information.** Before downloading a model, it's necessary to check the following things:
		1. **What kind of model it is.** A `Checkpoint` contains everything - you download one file and can start working. This means the checkpoint already includes CLIP, which is responsible for prompt interpretation, and VAE.
		2. **Which base model it was trained on.** Crucial from the perspective of LoRA and control networks.
		3. **What's the recommended resolution.** You need to use what the creators specify, otherwise the images will be of poor quality.
		4. **What kind of prompt the model uses.** This can be natural language or tags. Additionally, check if it requires a negative prompt. The way of writing prompts depends on how the data used for training the model was described.
		5. **What settings should be used to generate images.** This concerns the sampler, as well as the so-called `Clip Skip`. This is one of the model training parameters, often set to `2`, which means that when interpreting the prompt, the model focuses on the general concept rather than details. This is not a variable that improves quality! You can't unscrew a size 10 bolt with a size 8 wrench.
		6. **Whether the creators recommend using a specific VAE.** VAE, or `Variational Auto Encoder`, is responsible for creating the image based on an abstract layer generated in the graphics card memory. Sometimes during model training, significant VAE skewing occurs, and then creators recommend using the base model's VAE.
		7. **What's the license.** Good luck with this one, it's still the Wild West. For example, some models are trained on images from popular movies and anime series. You can summon a specific character using a certain phrase in the prompt.
		8. **How to configure the sampler.** The sampler in ComfyUI is responsible for image generation, and model creators often present settings that allow achieving the best quality.
	4. **LoRAs are also available on CivitAI.** LoRA (`Low-Rank Adaptation`) is a small fragment of a model specially trained to bias the attention of a larger model. LoRAs affect the final work result, which is why there are LoRAs for nice hands, legs, or specific presentation styles. Using LoRA requires using a specific keyword in the prompt!
	5. **Models are placed in a specific directory in ComfyUI.** The structure is self-descriptive.

4. **ComfyUI Manager is an excellent tool for controlling which packages are installed.** This should be downloaded to ComfyUI by default - I can't imagine working without it.
	1. **It greatly facilitates work with node packages in ComfyUI.** It simply downloads data from the GitHub repository, unpacks, and installs it. It also throws errors!
	2. **The packages contain nodes that often perform the same functions and can conflict with each other.** If you're using a specific node, sometimes you need to ensure that connected nodes are from the same package. The user is informed about the problem, and the workflow won't execute.
	3. **You can also write nodes yourself.** I did and still do this, adding my own lines of code to this chaos. Claude handles node writing well, but you need to help it by adding some documentation hints.

5. **Developing a Basic Workflow**
	1. **To generate an image:** Checkpoint -> Prompt -> Sampler -> Image.
	2. **Generating an image using control networks.** First, a presentation of what control networks are available and what their effects look like.
	3. **Elements used in the created workflow:**
		1. **Model:** [DreamSharperXL](https://civitai.com/models/112902/dreamshaper-xl)
		2. **LoRA:** [FLUX-style Lora for SDXL](https://civitai.com/models/625636?modelVersionId=700770)
		3. **Depth ControlNet:** [ControlNet SDXL](https://huggingface.co/ckpt/controlnet-sdxl-1.0/blob/main/control-lora-depth-rank256.safetensors)
		4. **Packages:** [ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack), [ComfyUI-yanc](https://github.com/ALatentPlace/ComfyUI_yanc)

# Additional Information

## Hardware I Use

| At home                                                      | At work (lowest spec)                                          |  
| ------------------------------------------------------------ | -------------------------------------------------------------- | 
| i7 14700KF 3.4 GHz<br>64 GB RAM DDR5<br>RTX 4080 Super 16 GB | Ryzen 9 5950X 3.4 GHz<br>32 GB RAM DDR4<br>RTX 2070 Super 8 GB | 

## Prompt Examples

| Natural Language                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Tags |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| A sophisticated urban loft interior bathed in deep cherry red lighting. The main focus is a plush burgundy velvet sofa with metallic chrome legs catching reflections from subtle neon art installations. The space features polished concrete floors contrasting with luxurious textiles, while dramatic shadows cast by modern sculptural lighting fixtures create pockets of intrigue. Shot in a cinematic style with emphasis on depth and dimension, resembling a high-end fashion editorial. The atmosphere is moody yet refined, with precise highlights accentuating the interplay between soft and hard surfaces throughout the contemporary space. | establishing shot, confident young woman portrait, dramatic graphic novel illustration with detailed crosshatching, intricate ink work and lineart, elegant pose on wooden chair, long flowing hair with styled bangs, graceful facial expression, ornate floral backdrop with organic patterns, high contrast black and white with midnight blue accents, soft rim lighting casting dramatic shadows, complex background details, warm gradients, style by Moebius, ligne claire technique, intricate 8K detail     |

## Models to Show

[EpicRealism](https://civitai.com/models/277058?modelVersionId=1346244), [Pony](https://civitai.com/models/257749?modelVersionId=290640), [DreamShaper](https://civitai.com/models/4384?modelVersionId=128713), [Flux](https://civitai.com/models/618692?modelVersionId=691639).

## Transform Based Model vs Diffusion Based Model

*Diffusion* models generate content by removing unnecessary noise. In each step, they begin to extract a more concrete image from chaos based on the used prompt. Link to [video](https://github.com/nathannlu/aperture).

## Sampler. Element Description

| Element Name                   | Description                                                                                                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Seed                           | A number that controls the initial randomness of image generation.<br>Using the same seed guarantees similar images.                                                                                             |
| Steps                          | The number of steps AI takes in creating the image.<br>Usually, more steps mean a better image.                                                                                                                 |
| CFG (Classifier Free Guidance) | Determines how closely the model follows the prompt.<br>Higher value means stronger adherence to the prompt, but this doesn't automatically mean better quality!                                                 |
| Sampler Name                   | Algorithms used in image generation.<br>**Euler**: Fast, most commonly used. **DPM++**: slower but creates higher quality images. **DDIM**: Good when composition consistency needs to be maintained             |
| Scheduler                      | Controls how chaos is removed from the image.<br>**Normal**: Standard, most commonly used. **Karras**: Focuses on details. **Linear**: Focuses on maintaining composition consistency.                           |
| Denoise                        | Determines how much of the original image is preserved in `image2image` generation                                                                                                                              |

## Training Prompts

### Woman on Bridge

#### Prompt +

```
cinematic analog film still, masterpiece, best quality, portrait of an elegant woman standing on an ornate stone bridge, natural pose, casual elegant clothing, soft afternoon sunlight, historic European architecture, weathered stone textures, river below, film grain, muted vintage colors, Kodak Portra 400 style, depth of field, nostalgic atmosphere, intricate details, 8k, amazing quality
```

#### Prompt -

```
(low quality, worst quality:1.4), cgi, text, signature, watermark, extra limbs, ugly, deformed, noisy, blurry, low contrast, oversaturated, modern elements, digital looking, heavy grain, overexposed
```

### Dog on Beach

#### Prompt +

```
masterpiece, best quality, pastel art sketch, black dog standing majestically on sandy beach, soft ocean waves background, gentle morning light, fluffy fur details, serene expression, playful pose, coastal atmosphere, seabirds in sky, pastel color palette, soft artistic strokes, traditional media, watercolor paper texture, detailed fur rendering, amazing quality
```

#### Prompt -

```
(low quality, worst quality:1.4), cgi, text, signature, watermark, extra limbs, ugly, deformed, noisy, blurry, low contrast, photorealistic, digital art, harsh lines, anatomically incorrect, cartoon style, oversaturated colors
```