# LoRA Dataset Generator

This tool helps you generate captioned datasets for LoRA (Low-Rank Adaptation) training by using AI to automatically describe images. It supports both Ollama's local models and OpenAI's cloud-based models for generating captions.

Was really helpful during training LoRAs on CitivAI.

## Features

- **Automatic Caption Generation**: Use AI to create consistent captions for your training images
- **Multiple AI Providers**: Support for both Ollama (local) and OpenAI (cloud) models
- **Caption Types**: Generate detailed descriptive captions or simple tags
- **Interactive Mode**: User-friendly console interface for easy configuration
- **Batch Processing**: Process entire directories of images at once
- **Progress Tracking**: Visual progress indicators during processing

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Install the required dependencies:
   ```
   pip install pyyaml ollama openai python-dotenv
   ```

3. Set up your environment:
   - Copy `.env.template` to `.env` and add your API keys if using OpenAI
   - Place your images in the `images` directory
   - Customize `config.yaml` if needed (optional)

## Usage

### Interactive Mode (Recommended for beginners)

```bash
python create_lora_dataset.py --interactive
```

This launches a step-by-step console interface that guides you through the configuration process.

### Command Line Mode (Good for automation)

Basic usage with default settings:
```bash
python create_lora_dataset.py
```

Custom configuration example:
```bash
python create_lora_dataset.py --theme "Fantasy characters" --service ollama --model "gemma3:12b" --caption-type flux_captions
```

Using OpenAI (requires API key in .env or via parameter):
```bash
python create_lora_dataset.py --service open_ai --model "gpt-4o" --api-key "your_api_key_here"
```

### Available Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--theme` | Dataset theme/subject | "2D game item icons" |
| `--caption-type` | Type of captions to generate | "flux_captions" |
| `--service` | AI service to use (ollama/open_ai) | "ollama" |
| `--model` | AI model to use | "gemma3:12b" (ollama) or "gpt-4o" (OpenAI) |
| `--image-dir` | Directory containing images | "images" |
| `--output-dir` | Output directory for the dataset | "dataset" |
| `--config` | Path to configuration file | "config.yaml" |
| `--api-key` | OpenAI API key (alternative to .env) | None |
| `--interactive`, `-i` | Launch interactive mode | False |

## Caption Types

- **flux_captions**: Detailed captions that follow the flux formatting style, good for training stable diffusion models.
- **tag**: Simple comma-separated tags describing the image content, suitable for more basic models.

## Environment Variables

The following environment variables can be set in your `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key (required if using OpenAI services)

## Output

The tool will:
1. Process each image and generate a caption based on your settings
2. Save each caption as a text file with the same name as its corresponding image
3. Create a ZIP file named `dataset_ready.zip` containing all images and caption files
4. Clean up the temporary dataset directory

## Troubleshooting

- **No images found**: Make sure your images are placed in the correct directory and have `.jpg`, `.jpeg`, or `.png` extensions.
- **OpenAI API errors**: Check that your API key is correct and that you have sufficient credits.
- **Ollama errors**: Ensure the Ollama service is running and the specified model is installed.
