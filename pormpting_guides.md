# Background
I'm using different models to generate graphics, and all of them have different prompting rules to follow. That's why I decided to create a library of guides.

Here I will publish tested prompting guides that work for me. All of them were generated using Perplexity with additional resources (links, documents, tests).

This can be used as an instruction for LLMs (I use Claude to generate prompts based on images or simple descriptions).


## Cheyenne

### 1. Master the Core Style Elements
- Start with the primary visual style indicators:
  - graphic novel
  - illustration
  - sketch
  - lineart
  - colored ink pencils
  - crosshatching
- Example: *"sketch, graphic novel illustration with heavy crosshatching and bold ink work"*

### 2. Build Composition Structure
- Begin with view specification:
  - establishing shot
  - candid view
  - low angle
  - dutch angle
- Add scene framing:
  - wide screen
  - full scene
  - multiple views
- Example: *"establishing shot, wide screen view of [subject], multiple viewing angles"*

### 3. Define Visual Quality and Detail Level
- Include technical specifications:
  - intricate
  - full of details
  - hyperdetailed
  - 8K
  - high quality
- Focus on detail areas:
  - complex background
  - detailed outfits
  - intricate patterns
- Example: *"intricate detailed scene in 8K quality, complex background full of cultural elements"*

### 4. Specify Color and Contrast
- Use the model's core palette:
  - High contrast
  - Black and grungy white
  - Midnight blue accents
  - Warm gradients
  - Limited palette
- Include lighting specifics:
  - strong rim lighting
  - hard shadows
  - dramatic lighting
- Example: *"High contrast illustration with midnight blue accents, stark black and grungy white, warm gradients in shadows"*

### 5. Add Artistic References
- Include specific artist styles when needed:
  - style by [artist name]
  - in the manner of [artist]
- Reference art movements:
  - art nouveau
  - ligne claire
  - western comics
- Example: *"style by Mike Mignola, western comics aesthetic with ligne claire technique"*

### 6. Layer Environmental Details
- Build complex backgrounds:
  - specific location elements
  - architectural details
  - natural elements
  - atmospheric effects
- Example: *"grassy landfields with traditional camp structures, complex native camp background full of cultural details"*

### 7. Incorporate Action and Movement
- Use dynamic descriptors:
  - motion trails
  - speed lines
  - impact frames
  - dramatic poses
- Example: *"dynamic action scene with speed lines and impact frames, dramatic pose emphasized by bold ink work"*

### 8. Essential Negative Prompts
Always include these core negative elements:
```
ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, watermark, grainy, signature, cut off, draft
```

Additional negatives by category:
- Quality negatives:
  ```
  worst quality, low quality, lowres
  ```
- Style negatives:
  ```
  photo, realistic, photography, 3d, cg, 3d render
  ```
- Unwanted elements:
  ```
  text, watermark, picture frame, border, nsfw, nude, bright, shiny, saturated
  ```

### 9. Prompt Structure Template
Use this order for complex prompts:
1. View/Composition
2. Subject description
3. Style specifications
4. Technical quality
5. Background/Environment
6. Lighting/Color
7. Artist references

Example complete prompt:
```
establishing shot, Cheyenne warrior in traditional garments, graphic novel illustration with heavy crosshatching, intricate 8K detail, complex native camp background with grassy landfields, high contrast black and white with midnight blue accents, style by [artist name], dramatic lighting with strong shadows
```

### 10. Advanced Techniques
- Combine multiple style elements:
  ```
  sketch, graphic novel, ink work, crosshatching
  ```
- Layer multiple lighting effects:
  ```
  strong rim lighting, hard shadows, dramatic contrast
  ```
- Stack multiple quality indicators:
  ```
  intricate, hyperdetailed, full of details, 8K
  ```

### 11. Common Mistakes to Avoid
- Don't mix conflicting styles
- Avoid overcrowding with too many artist references
- Don't use style weights or brackets
- Avoid generic quality terms without specifics
- Don't mix historical periods unless intentional

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

## Runway (Gen 3 Alpha)

### **Prompt Structures**

A well-structured prompt enhances the model's ability to generate accurate and creative outputs. Use the following structure:

**[camera movement]: [establishing scene]. [additional details].**

#### **Base Prompt Example**
- *Low angle static shot:* The camera is angled up at a woman wearing all orange as she stands in a tropical rainforest with colorful flora. The dramatic sky is overcast and gray.

#### **Tips for Effective Prompts**
- Focus on what *should* appear in the scene (e.g., "clear sky" instead of "sky with no clouds").
- Repeat or reinforce key ideas across sections to improve adherence (e.g., "hyperspeed" for fast camera movements).
- Keep prompts concise and specific.

### **Sample Prompts**

#### **Seamless Transitions**
- *Continuous hyperspeed FPV footage:* The camera seamlessly flies through a glacial canyon to a dreamy cloudscape.

#### **Camera Movement**
- *A glowing ocean at night time:* The camera starts with a macro close-up of a glowing jellyfish and then expands to reveal the entire ocean lit up with various glowing colors under a starry sky. 
  - *Camera Movement:* Begin with a macro shot of the jellyfish, then gently pull back and up to showcase the glowing ocean.

#### **Text Title Cards**
- *A title screen with dynamic movement:* The scene starts at a colorful paint-covered wall. Suddenly, black paint pours on the wall to form the word "Runway." The dripping paint is detailed and textured, centered, with superb cinematic lighting.

### **Keywords for Enhanced Outputs**

Incorporating relevant keywords into your prompts can refine the style, mood, and technical aspects of the generated video. Ensure that keywords align cohesively with your overall prompt.

#### **Camera Styles**
| Keyword               | Description                               |
|-----------------------|-------------------------------------------|
| Low angle             | Camera positioned below the subject       |
| High angle            | Camera positioned above the subject       |
| Overhead              | Directly above, bird’s-eye view           |
| FPV                   | First-person view                        |
| Hand held             | Gives a shaky, realistic feel            |
| Wide angle            | Captures a broad field of view           |
| Close up              | Focuses on a small detail or subject      |
| Macro cinematography  | Extreme close-up for intricate details    |
| Over the shoulder     | Perspective behind a character            |
| Tracking              | Follows the subject's movement           |
| Establishing wide     | Sets the scene context                   |
| 50mm lens             | Standard cinematic view                  |
| SnorriCam             | Fixed camera attached to a moving subject|
| Realistic documentary | Naturalistic, unpolished look            |
| Camcorder             | Retro home video style                   |

#### **Lighting Styles**
| Keyword           | Description                                |
|-------------------|--------------------------------------------|
| Diffused lighting | Soft, even light                          |
| Silhouette        | Subject appears as a dark shape           |
| Lens flare        | Light streaks caused by bright sources    |
| Back lit          | Light source behind the subject           |
| Side lit          | Light from one side                       |
| [color] gel lighting | Colored lighting effects               |
| Venetian lighting | Light filtered through blinds or slats    |

#### **Movement Speeds**
| Keyword      | Description                     |
|--------------|---------------------------------|
| Dynamic motion | Energetic and fast-paced      |
| Slow motion   | Slowed-down movements          |
| Hyperspeed    | Extremely fast movements       |
| Timelapse     | Compressed time visualization  |

#### **Movement Types**
| Keyword       | Description                     |
|---------------|---------------------------------|
| Grows         | Gradual expansion              |
| Emerges       | Gradual appearance             |
| Explodes      | Sudden burst                   |
| Ascends       | Moves upward                   |
| Undulates     | Wave-like motion               |
| Warps         | Distorted transformation       |
| Transforms    | Changes into something else    |
| Ripples       | Wave-like spreading effect     |
| Shatters      | Breaks apart                   |
| Unfolds       | Gradual opening                |
| Vortex        | Spiral motion                  |

#### **Style and Aesthetic**
| Keyword         | Description                      |
|-----------------|----------------------------------|
| Moody           | Dark, atmospheric tone          |
| Cinematic       | High-quality film style         |
| Iridescent      | Shimmering color effects        |
| Home video VHS  | Retro aesthetic                 |
| Glitchcore      | Digital glitches and distortions|

#### **Text Styles**
For text-based elements like title cards:
- Bold
- Graffiti
- Neon
- Varsity
- Embroidery

### **Experimentation Encouraged**

While this guide provides structured examples and keyword suggestions, experimentation is key to unlocking Gen-3 Alpha's full potential. Combine different styles, movements, and aesthetics to bring your unique vision to life!


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