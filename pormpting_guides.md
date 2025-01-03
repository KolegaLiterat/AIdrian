# Background
I'm using different models to generate graphics, and all of them have different prompting rules to follow. That's why I decided to create a library of guides.

Here I will publish tested prompting guides that work for me. All of them were generated using Perplexity with additional resources (links, documents, tests).

This can be used as an instruction for LLMs (I use Claude to generate prompts based on images or simple descriptions).

## Flux1Dev

**Important!** Flux does not need a negative prompt, but it needs a guidance node in ComfyUI!

### **1. Be Specific and Descriptive**
- Clearly describe the main subject of the image, including its appearance, position, and any actions it is performing.
  - Example: *"A futuristic cityscape with towering skyscrapers made of glass and steel, glowing neon signs in various languages, and flying cars zipping through the air."*
- Include details about the environment or background to provide context.
  - Example: *"Set during a rainy evening with reflections on wet streets and a dramatic cloudy sky."*

### **2. Use Natural Language**
- Write prompts as if explaining your vision to a human artist. Flux.1 Dev responds well to narrative-style prompts rather than fragmented keywords.
  - Example: *"A serene forest clearing at dawn, with golden sunlight filtering through the trees, illuminating a small wooden cabin surrounded by wildflowers."*

### **3. Specify Artistic Style and Tone**
- Define the desired artistic style (e.g., photorealistic, surreal, cartoonish) and tone (e.g., vibrant, dark, whimsical).
  - Example: *"Photorealistic digital art in 8K resolution, with vibrant colors and cinematic lighting."*
- Mention specific influences or genres if applicable.
  - Example: *"In the style of Art Nouveau with intricate floral patterns."*

### **4. Include Technical Details**
- For photorealistic images, specify camera settings or tools to emulate real-world photography.
  - Example: *"Shot on a DSLR camera with a wide-angle lens, f/2.8 aperture, shallow depth of field."*
- Add lighting details such as time of day, shadows, or effects like volumetric rays.
  - Example: *"Soft morning light with long shadows and subtle lens flare effects."*

### **5. Blend Concepts Creatively**
- Combine multiple ideas or themes for unique outputs.
  - Example: *"A medieval knight in futuristic armor standing on a floating island surrounded by waterfalls and glowing crystals."*
- Use juxtaposition for striking visuals.
  - Example: *"A robotic dragon perched on the ruins of an ancient castle under a stormy sky."*

### **6. Leverage Text Integration**
- If text is part of your image, describe its placement, style, and content explicitly.
  - Example: *"A glowing neon sign reading 'Welcome to Neo-Tokyo' in bold Japanese kanji, placed above a bustling street market."*
- Flux.1 excels at rendering clear text within images when prompted correctly.

### **7. Organize Your Prompt Logically**
- Break down complex prompts into smaller sections focusing on:
  - Subject
  - Environment
  - Style and tone
  - Lighting and effects
- Avoid chaotic phrasing or excessive keywords that can confuse the model.
  - Correct: *"A lone astronaut walking on a red desert planet under a starry sky with two moons visible in the distance."*
  - Incorrect: *"Astronaut red desert stars moons sky walking alone."*

### **8. Experiment and Iterate**
- Start with a base prompt and refine it iteratively based on output quality.
  - Initial Prompt: *"A dragon in flight over a mountain range at sunset."*
  - Refined Prompt: *"A majestic dragon with golden scales soaring over snow-capped mountains at sunset, with dramatic clouds and warm orange hues in the sky."*
- Test variations in phrasing or additional details to achieve desired results.

### **9. Avoid Common Mistakes**
- Do not use prompt weights (e.g., `(object:1.5)`) as Flux.1 Dev does not support them. Instead, use natural language emphasis like "with focus on."
- Avoid vague descriptors like "cool," "nice," or "beautiful," which lack specificity.


## Stable Diffiusion 3.5

**Important!** Negative prompt is not necessary for SD3.5, but helps refine images.

### **1. Structure Your Prompt**
To create high-quality images, follow these guidelines:
- **Be specific and descriptive**: Use vivid adjectives and clear nouns.
- **Define the subject**: Clearly state the main focus of the image.
  - Example: *“An image of a futuristic cityscape with flying cars under a neon-lit sky.”*
- **Include details about composition**: Specify framing (e.g., close-up, wide-angle), perspective (e.g., bird’s-eye view), and layout.
- **Mention style and medium**: Indicate artistic or photographic styles (e.g., watercolor painting, photorealistic, surrealism).
- **Describe lighting and mood**: Examples include "soft ambient light," "dramatic shadows," or "vibrant sunset hues."
- **Use keywords for quality**: Add terms like "4K," "8K," or "highly detailed" to emphasize resolution.

### **2. Use Negative Prompts**
Negative prompts help refine outputs by excluding unwanted elements. For example:
- *“Exclude cluttered backgrounds, low resolution, or blurry effects.”*
This ensures the focus remains on the desired elements.

### **3. Optimize Text in Images**
When incorporating text into images:
- Use **double quotes** for clarity (e.g., “Welcome to the Future”).
- Keep text concise for better rendering.
- Specify placement if necessary (e.g., “Text centered at the top”).