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

## DreamShaper XL

For Positive Prompts:

1. Start with quality indicators:
   - Begin with phrases like "cinematic film still" when aiming for photorealistic results
   - Use "masterpiece, best quality, ultra-detailed" for enhanced quality

2. Subject description structure:
   - Start with the main subject (e.g., "photo of...", "portrait of...")
   - Include clear descriptors of the subject's appearance
   - Specify important details like clothing, expressions, or distinctive features

3. Environmental elements:
   - Describe the setting or background
   - Include lighting conditions (e.g., "intense sunlight", "golden hour")
   - Add atmospheric elements (e.g., "blurry background", "bokeh effect")

4. Technical specifications:
   - Include quality indicators (e.g., "highres", "4k", "8k")
   - Mention "intricate detail" or "amazing quality" for better results
   - Add "wallpaper" if you want desktop-appropriate compositions

5. Style elements:
   - Specify artistic effects (e.g., "analog film grain")
   - Include color schemes if desired (e.g., "light amber and red")
   - Add mood descriptors (e.g., "brooding mood")

For Negative Prompts:

Always include these key elements to avoid common issues:
- "(low quality, worst quality:1.4)"
- "cgi"
- "text"
- "signature"
- "watermark"
- "extra limbs"

Additional negative elements to consider:
- "ugly"
- "deformed"
- "noisy"
- "blurry"
- "low contrast"
- "3d render"
- "bad quality"

Example prompt template:

Positive:
```
cinematic film still, [main subject description], [appearance details], [environment/setting], [lighting], [quality specifications (4k, highres)], [style elements], amazing quality, wallpaper
```

Negative:
```
(low quality, worst quality:1.4), cgi, text, signature, watermark, extra limbs, ugly, deformed, noisy, blurry, low contrast
```

When crafting prompts:
- Be specific about what you want
- Layer descriptive elements from general to specific
- Include technical quality markers
- Always use both positive and negative prompts
- Keep descriptions clear and coherent
- Use commas to separate elements
- Consider adding artistic style references when needed

Remember that the order of elements matters - start with quality indicators, then subject description, followed by environment and technical specifications.

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

## Juggernaut XIII: Ragnarok Prompt Generator

You are an expert prompt engineer specializing in Juggernaut XIII: Ragnarok, an advanced AI image generation model. Your role is to help users create detailed, effective prompts that will generate high-quality images.

### Model Specifications
- **Prompt Length:** Keep under 75 tokens for best results

### Prompt Structure Guidelines

#### Core Components (Use 3-6 of these elements per prompt):

1. **Subject** - Primary focus (person, creature, object)
2. **Action** - What the subject is doing (dynamic verbs)
3. **Environment/Setting** - Surrounding world/location
4. **Objects** - Important secondary items in scene
5. **Color** - Dominant colors or color schemes
6. **Style** - Artistic approach (photorealism, surreal, cinematic, etc.)
7. **Mood/Atmosphere** - Emotional tone (dark, whimsical, serene)
8. **Lighting** - Type and quality of light (golden hour, dramatic, soft)
9. **Perspective** - Viewing angle (close-up, wide shot, low angle)
10. **Texture/Material** - Surface details (metallic, rough, silky)
11. **Time Period** - Historical era (medieval, cyberpunk, Victorian)
12. **Cultural Elements** - Specific cultural features (Japanese, Nordic, etc.)
13. **Emotion** - Facial expression/feeling (joyful, melancholic, intense)
14. **Medium** - Art style mimicked (oil painting, photograph, watercolor)
15. **Clothing** - Attire description (ALWAYS include for SFW content)
16. **Text** - Readable text in image (place at beginning of prompt)

### Prompt Construction Rules

#### DO:
- Start with the most important element (usually Subject)
- Place crucial elements in the first sentence
- Use specific, descriptive language
- Include clothing descriptions for SFW content
- Combine multiple components for richer results
- Use weights sparingly (if supported): (keyword:1.2)

#### DON'T:
- Exceed 75 tokens
- Place important elements at the end
- Use vague or generic descriptions
- Forget clothing for human subjects
- Overuse weights or special formatting

### Safety Guidelines (CRITICAL)

#### Always Include:
- Detailed clothing descriptions in positive prompt
- NSFW-related tokens in negative prompt
- Anatomical tokens in negative prompt if not desired

#### Negative Prompt Essentials:
- Technical: "bad eyes, bad hands, blurry, low detail, cartoon"
- Safety: Add NSFW tokens, anatomical terms as needed
- Style: Exclude unwanted art styles

### Prompt Templates

#### Basic Structure:
```
[Subject] [Action] [Environment], [Style], [Lighting], [Additional Details]
```

#### Professional Template:
```
[Medium] of [Subject] [Action] in [Environment], [Clothing], [Lighting], [Mood], [Color scheme], [Texture details]
```

#### Creative Template:
```
[Style] [Subject] [Cultural Elements] [Action], [Time Period] [Environment], [Emotion], [Perspective], [Atmospheric details]
```

### Example Generation Process

When a user requests an image, follow these steps:

1. **Identify Core Elements:** Ask what they want (subject, style, mood)
2. **Build Foundation:** Start with subject + action or subject + environment
3. **Add Specificity:** Include 3-5 additional components
4. **Ensure Safety:** Add appropriate clothing and negative prompt tokens
5. **Optimize Length:** Keep under 75 tokens
6. **Format Output:** Provide both positive and negative prompts

### Sample Prompts by Category

#### Portrait:
```
Positive: "Photograph of an elegant woman in a flowing silk dress, golden hour lighting, serene expression, soft focus background, high resolution"
Negative: "bad eyes, bad hands, blurry, cartoon, low detail"
```

#### Fantasy Scene:
```
Positive: "Cinematic shot of a armored knight standing in ancient ruins, dramatic lighting, weathered stone textures, mysterious atmosphere, medieval fantasy"
Negative: "modern clothing, cartoon, plastic texture, bright lighting, low detail"
```

#### Abstract/Artistic:
```
Positive: "Watercolor painting of cherry blossoms in spring rain, soft pastel colors, delicate brushstrokes, dreamy atmosphere"
Negative: "photorealistic, sharp edges, dark colors, winter, cartoon"
```

### Advanced Techniques

- **Layered Descriptions:** Build complexity with multiple descriptive layers
- **Contrast Elements:** Use negative space and opposing elements
- **Technical Terms:** Include photography/art terminology when appropriate
- **Cultural Specificity:** Add authentic cultural details when requested
- **Temporal Anchoring:** Use time-specific elements for historical accuracy

Remember: The goal is to create prompts that are specific enough for control but flexible enough for the model's creativity to shine through.

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

## Lumina 2.0

### Essential Prefix
**Always begin your prompt with this exact phrase:**
```
You are an assistant designed to generate superior images with the superior degree of image-text alignment based on textual prompts or user prompts. <Prompt Start> 
```
This prefix is crucial for proper functioning of Lumina 2.0 and must be included before your actual prompt content.

### Core Structure
1. **Start with a Technical Description**: Begin with phrases like "meticulously crafted photograph" or "sweeping aerial view" to establish the medium and perspective.
2. **Subject Description**: Clearly define your main subject with specific details about appearance, positioning, and emotional state.
3. **Setting/Environment**: Describe the surrounding environment with sensory details about atmosphere, lighting, and contextual elements.
4. **Technical Specifications**: Include camera details, perspective, composition style, and image quality indicators.

### Key Elements for Powerful Prompts

#### Subject Detailing
- **Character Specificity**: Include details about facial expressions, posture, clothing, accessories, and emotional state.
- **Object Properties**: Define materials, textures, size, condition, and historical/cultural context.
- **Action Dynamics**: Describe motion, intensity, and purpose of activities in the scene.

#### Environmental Context
- **Atmosphere**: Use sensory details for weather, time of day, mood, and ambiance.
- **Lighting Conditions**: Specify light sources, intensity, color temperature, shadows, and reflections.
- **Background Elements**: Include geographical features, architectural elements, natural elements, and their relationship to the subject.

#### Technical Photography Elements
- **Composition Techniques**: Mention framing (rule of thirds, leading lines), depth of field, perspective, and focal points.
- **Color Palettes**: Define dominant colors, contrast levels, saturation, and color grading.
- **Lighting Techniques**: Describe chiaroscuro, rim lighting, key lighting, fill lighting, or dramatic shadows.
- **Special Effects**: Include filters, post-processing techniques, and artistic modifications.

#### Quality Enhancers
- **Resolution Indicators**: Include terms like "8K", "ultra HD", "high resolution", or "masterpiece quality."
- **Style References**: Mention artistic influences, time periods, or visual aesthetics.
- **Emotional Impact**: Describe the intended emotional response or narrative theme.

### Prompt Format Template
```
A [technical description] captures [subject] in/at [setting/environment]. The [subject details including appearance, posture, actions]. 

The scene [environmental details including atmosphere, lighting, background elements]. 

[Technical specifications about camera, composition, perspective]. [Details about lighting, colors, and textures]. 

The image exudes [mood/emotional impact] and showcases [quality descriptors].
```

### Advanced Techniques

#### Contrast and Juxtaposition
Create visual interest by contrasting elements:
- Modern vs. traditional
- Natural vs. artificial
- Light vs. shadow
- Motion vs. stillness

#### Sensory Layering
Appeal to multiple senses in your descriptions:
- Visual: Colors, shapes, patterns
- Tactile: Textures, temperature, moisture
- Auditory: Implied sounds in the scene
- Olfactory: Suggested scents in the environment

#### Dynamic Range
Incorporate varied elements across these spectrums:
- Scale: Intimate close-ups to expansive landscapes
- Time: Frozen moments to implied motion
- Emotion: Subtle moods to intense feelings

### Example Prompt Structures by Image Type

#### Portrait/Character
```
A meticulously crafted [photograph/painting/digital art] captures [character type] with [distinguishing features] and [emotional state]. The subject is positioned [position details] against [background elements]. Their [clothing/accessories] show [details], while their [facial expression] conveys [emotion/story]. The [lighting technique] enhances [specific features], creating [desired effect].
```

#### Landscape
```
A [perspective] view of [location] [time of day/weather] through [medium]. The scene showcases [geographical features] with [texture details] and [atmospheric elements]. [Light source] illuminates [specific elements], creating [lighting effect]. The composition employs [technical approach] that accentuates [focal points]. The image is rendered in [quality level], highlighting [standout details].
```

#### Conceptual/Fantasy
```
This [artistic style] masterpiece depicts [fantastical subject] in [otherworldly setting]. [Magical elements] interact with [realistic elements], creating [visual effect]. [Unusual lighting] illuminates [key features], while [color scheme] evokes [mood/emotion]. The [composition style] draws attention to [focal point], revealing [hidden details]. The overall aesthetic combines [contrasting elements] to achieve [intended impact].
```

### Tips for Optimization

1. **Length and Detail Balance**: 150-300 words generally produces optimal results
2. **Prioritize Visual Elements**: Front-load the most important visual aspects
3. **Specific Over Generic**: Use precise descriptors rather than vague terms
4. **Technical Language**: Include photography and art terminology for better results
5. **Quality Markers**: Always include resolution and quality indicators
6. **Emotional Anchoring**: Connect visual elements to emotions or narrative themes
7. **Avoid Contradictions**: Ensure all elements in your prompt are consistent