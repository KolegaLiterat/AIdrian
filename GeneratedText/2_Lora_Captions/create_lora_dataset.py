import yaml
import os
import ollama
from shutil import copyfile
import zipfile
from openai import OpenAI
import base64
import argparse
import logging
from typing import Dict, List, Optional, Any
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def setup_logging() -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Create a LoRA dataset with AI-generated captions')
    
    parser.add_argument('--theme', type=str, default="2D game item icons",
                        help='Theme of the dataset (default: "2D game item icons")')
    parser.add_argument('--caption-type', type=str, choices=['flux_captions', 'tag'], 
                        default="flux_captions", help='Type of caption to generate')
    parser.add_argument('--service', type=str, choices=['ollama', 'open_ai'], 
                        default="ollama", help='Service to use for image description')
    parser.add_argument('--model', type=str, default="gemma3:12b", 
                        help='Model to use (default: "gemma3:12b" for Ollama, "gpt-4o" for OpenAI)')
    parser.add_argument('--image-dir', type=str, default="images", 
                        help='Directory containing images (default: "images")')
    parser.add_argument('--output-dir', type=str, default="dataset", 
                        help='Output directory for the dataset (default: "dataset")')
    parser.add_argument('--config', type=str, default="config.yaml", 
                        help='Path to configuration file (default: "config.yaml")')
    parser.add_argument('--api-key', type=str, 
                        help='OpenAI API key (only needed for open_ai service)')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Launch interactive console GUI mode')
    
    return parser.parse_args()

def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from a YAML file or create default if not exists."""
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            logging.warning(f"Failed to load config file: {e}. Using default configuration.")
    
    # Default configuration
    default_config = {
        "dataset_theme": "2D game item icons",
        "caption_type": "flux_captions",
        "description_service": "ollama",
        "ollama_model": "gemma3:12b",
        "openai_model": "gpt-4o",
        "image_directory": "images",
        "output_directory": "dataset"
    }
    
    return default_config

def load_prompts(filename: str) -> Dict[str, str]:
    """Load prompts from a YAML file."""
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        logging.error(f"Prompts file {filename} not found.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error loading prompts: {e}")
        sys.exit(1)

def load_image_files(file_path: str) -> List[str]:
    """Load image files from the specified directory."""
    if not os.path.exists(file_path):
        logging.error(f"Image directory {file_path} does not exist.")
        return []
    
    images = []
    for file in os.listdir(file_path):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            images.append(file)
    
    return images

def encode_image(image_path: str) -> Optional[str]:
    """Encode image to base64 string."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        logging.error(f"Failed to encode image {image_path}: {e}")
        return None

def save_description(file_path: str, description: str) -> bool:
    """Save description to a text file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(description)
        return True
    except Exception as e:
        logging.error(f"Failed to save description to {file_path}: {e}")
        return False

def copy_image_to_dataset(source_path: str, target_dir: str) -> bool:
    """Copy image to the dataset directory."""
    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        filename = os.path.basename(source_path)
        target_path = os.path.join(target_dir, filename)
        
        copyfile(source_path, target_path)
        return True
    except Exception as e:
        logging.error(f"Failed to copy image {source_path} to {target_dir}: {e}")
        return False

def zip_dataset(dataset_dir: str, output_zip: str = 'dataset_ready.zip') -> bool:
    """Zip the dataset directory."""
    try:
        if not os.path.exists(dataset_dir):
            raise ValueError("Dataset directory does not exist.")
        
        with zipfile.ZipFile(output_zip, 'w') as zipf:
            for file in os.listdir(dataset_dir):
                file_path = os.path.join(dataset_dir, file)
                zipf.write(file_path, file)
        
        logging.info(f"Dataset zipped successfully to {output_zip}")
        return True
    except Exception as e:
        logging.error(f"Failed to zip dataset: {e}")
        return False

def cleanup_dataset(dataset_dir: str) -> bool:
    """Clean up the dataset directory."""
    try:
        if os.path.exists(dataset_dir):
            for file in os.listdir(dataset_dir):
                os.remove(os.path.join(dataset_dir, file))
            logging.info(f"Dataset directory {dataset_dir} cleaned up")
            return True
        return False
    except Exception as e:
        logging.error(f"Failed to clean up dataset directory: {e}")
        return False

def describe_image_using_ollama(prompt: str, model: str, image_path: str) -> Optional[str]:
    """Use the Ollama API to describe the image."""
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [image_path]
                }
            ]
        )
        return response.message.content
    except Exception as e:
        logging.error(f"Ollama API error: {e}")
        return None

def describe_image_using_gpt(prompt: str, model: str, image_path: str, api_key: str) -> Optional[str]:
    """Use the OpenAI API to describe the image."""
    try:
        decoded_image = encode_image(image_path)
        if not decoded_image:
            return None
            
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpeg;base64,{decoded_image}"},
                    },
                ]},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return None

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_validated_input(prompt_text, options=None, default=None, allow_empty=False):
    """Get user input with validation against a list of options."""
    while True:
        if default and options:
            display_options = [f"[{opt}]" if opt == default else opt for opt in options]
            input_prompt = f"{prompt_text} ({'/'.join(display_options)}): "
        elif default:
            input_prompt = f"{prompt_text} [{default}]: "
        elif options:
            input_prompt = f"{prompt_text} ({'/'.join(options)}): "
        else:
            input_prompt = f"{prompt_text}: "
            
        user_input = input(input_prompt).strip()
        
        if not user_input:
            if allow_empty:
                return ""
            elif default:
                return default
            else:
                print("Input cannot be empty. Please try again.")
                continue
                
        if options and user_input not in options:
            print(f"Invalid input. Please choose from: {', '.join(options)}")
            continue
            
        return user_input

def get_directory_input(prompt_text, default=None, must_exist=True):
    """Get a directory path from the user with validation."""
    while True:
        if default:
            user_input = input(f"{prompt_text} [{default}]: ").strip()
            if not user_input:
                user_input = default
        else:
            user_input = input(f"{prompt_text}: ").strip()
            
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
            
        if must_exist and not os.path.exists(user_input):
            create_it = get_validated_input(
                f"Directory '{user_input}' does not exist. Create it?", 
                options=["y", "n"], 
                default="y"
            )
            if create_it.lower() == "y":
                try:
                    os.makedirs(user_input, exist_ok=True)
                    print(f"Created directory: {user_input}")
                    return user_input
                except Exception as e:
                    print(f"Error creating directory: {e}")
                    continue
            else:
                continue
        
        return user_input

def interactive_menu(config):
    """Interactive console GUI for configuring the dataset generation."""
    clear_screen()
    print("=" * 60)
    print("      LoRA Dataset Generator - Interactive Console GUI")
    print("=" * 60)
    print("\nWelcome! This interface will guide you through setting up your dataset.\n")
    
    # Theme selection
    theme = get_validated_input(
        "What is the theme of your dataset?",
        default=config.get("dataset_theme", "2D game item icons")
    )
    
    # Caption type selection
    caption_type = get_validated_input(
        "What type of captions do you want to generate?",
        options=["flux_captions", "tag"],
        default=config.get("caption_type", "flux_captions")
    )
    
    # Service selection
    service = get_validated_input(
        "Which AI service would you like to use?",
        options=["ollama", "open_ai"],
        default=config.get("description_service", "ollama")
    )
    
    # Model selection based on service
    if service == "ollama":
        model = get_validated_input(
            "Which Ollama model would you like to use?",
            default=config.get("ollama_model", "gemma3:12b")
        )
    else:  # open_ai
        model = get_validated_input(
            "Which OpenAI model would you like to use?",
            default=config.get("openai_model", "gpt-4o")
        )
        
        # API key for OpenAI - check environment first
        env_api_key = os.getenv("OPENAI_API_KEY", "")
        if env_api_key:
            print(f"Using OpenAI API key from environment variables: {'*' * 10 + env_api_key[-5:] if env_api_key else 'Not found'}")
            api_key = env_api_key
        else:
            api_key = get_validated_input(
                "Enter your OpenAI API key (or set OPENAI_API_KEY in .env file)",
                default=""
            )
            if not api_key:
                print("WARNING: OpenAI API key is required for the OpenAI service.")
                api_key = get_validated_input("Please enter your OpenAI API key (required)")
    
    # Directory selection
    image_dir = get_directory_input(
        "Enter the directory containing your images",
        default=config.get("image_directory", "images"),
        must_exist=True
    )
    
    output_dir = get_directory_input(
        "Enter the output directory for the dataset",
        default=config.get("output_directory", "dataset"),
        must_exist=False
    )
    
    # Confirmation
    clear_screen()
    print("=" * 60)
    print("      Configuration Summary")
    print("=" * 60)
    print(f"Dataset Theme: {theme}")
    print(f"Caption Type: {caption_type}")
    print(f"AI Service: {service}")
    print(f"Model: {model}")
    if service == "open_ai":
        print(f"API Key: {'*' * 10 + api_key[-5:] if api_key else 'Not provided'}")
    print(f"Image Directory: {image_dir}")
    print(f"Output Directory: {output_dir}")
    print("=" * 60)
    
    proceed = get_validated_input("Do you want to proceed with this configuration?", 
                                  options=["y", "n"], default="y")
    
    if proceed.lower() != "y":
        print("Configuration cancelled. Exiting...")
        sys.exit(0)
    
    # Return the configuration as a dictionary
    config_dict = {
        "dataset_theme": theme,
        "caption_type": caption_type,
        "description_service": service,
        "model": model,
        "image_directory": image_dir,
        "output_directory": output_dir
    }
    
    if service == "open_ai":
        config_dict["openai_api_key"] = api_key
    
    return config_dict

def show_progress_menu(total_images, current_image, image_name, status):
    """Display a simple progress menu during processing."""
    clear_screen()
    print("=" * 60)
    print("      LoRA Dataset Generator - Processing")
    print("=" * 60)
    print(f"Processing image {current_image} of {total_images}: {image_name}")
    print(f"Status: {status}")
    
    # Create a simple progress bar
    progress = int((current_image / total_images) * 50)
    print("\n[" + "#" * progress + " " * (50 - progress) + f"] {int((current_image / total_images) * 100)}%\n")
    
    # This function is primarily to display information, so we don't need user input here
    # The actual processing is handled by the main function
    return

def main() -> None:
    """Main function to process images and create a LoRA dataset."""
    setup_logging()
    args = parse_arguments()
    
    # Load config
    config = load_config(args.config)
    
    # If interactive mode is requested, use the console GUI
    if args.interactive:
        config_data = interactive_menu(config)
        dataset_theme = config_data["dataset_theme"]
        caption_type = config_data["caption_type"]
        description_service = config_data["description_service"]
        image_dir = config_data["image_directory"]
        output_dir = config_data["output_directory"]
        model = config_data["model"]
        api_key = config_data.get("openai_api_key", "")
    else:
        # Use command-line arguments or config file (as before)
        dataset_theme = args.theme or config.get("dataset_theme")
        caption_type = args.caption_type or config.get("caption_type")
        description_service = args.service or config.get("description_service")
        image_dir = args.image_dir or config.get("image_directory")
        output_dir = args.output_dir or config.get("output_directory")
        
        # Model selection based on service
        if description_service == "ollama":
            model = args.model or config.get("ollama_model")
        else:  # open_ai
            model = args.model or config.get("openai_model")
        
        # API key handling for OpenAI - check environment first
        env_api_key = os.getenv("OPENAI_API_KEY", "")
        api_key = args.api_key or env_api_key or ""
        
        if not api_key:
            logging.error("OpenAI API key is required for the open_ai service. Please set OPENAI_API_KEY in your .env file or provide it with --api-key.")
            sys.exit(1)
    
    # Validate API key for OpenAI
    if description_service == "open_ai" and not api_key:
        logging.error("OpenAI API key is required for the open_ai service.")
        sys.exit(1)
    
    # Load prompts and images
    prompts = load_prompts("prompts.yaml")
    images = load_image_files(image_dir)

    if len(images) == 0:
        logging.error(f"No images found in the directory '{image_dir}'. Exiting...")
        return

    # Process each image
    logging.info(f"Found {len(images)} images. Starting processing...")
    
    for idx, image in enumerate(images, 1):
        file_path = os.path.join(image_dir, image)
        caption = None
        
        # Show progress menu in interactive mode
        if args.interactive:
            show_progress_menu(len(images), idx, image, "Generating caption...")
        
        # Generate caption based on service and caption type
        if description_service == "ollama":
            if caption_type == "flux_captions":
                caption = describe_image_using_ollama(
                    prompts["flux_captions"].format(dataset_theme=dataset_theme, filename=image),
                    model, file_path
                )
            elif caption_type == "tag":
                caption = describe_image_using_ollama(
                    prompts["tag"].format(dataset_theme=dataset_theme, filename=image),
                    model, file_path
                )
        elif description_service == "open_ai":
            if caption_type == "flux_captions":
                caption = describe_image_using_gpt(
                    prompts["flux_captions"].format(dataset_theme=dataset_theme, filename=image),
                    model, file_path, api_key
                )
            elif caption_type == "tag":
                caption = describe_image_using_gpt(
                    prompts["tag"].format(dataset_theme=dataset_theme, filename=image),
                    model, file_path, api_key
                )
        
        if caption:
            caption_path = os.path.join(output_dir, os.path.splitext(image)[0] + ".txt")
            
            # Show progress menu in interactive mode
            if args.interactive:
                show_progress_menu(len(images), idx, image, "Saving caption and image...")
                
            if save_description(caption_path, caption):
                copy_image_to_dataset(file_path, output_dir)
        else:
            if args.interactive:
                show_progress_menu(len(images), idx, image, "ERROR: Failed to generate caption!")
                input("Press Enter to continue...")
            logging.warning(f"Failed to generate caption for {image}")
    
    # Create zip and cleanup
    if args.interactive:
        show_progress_menu(len(images), len(images), "", "Creating ZIP file...")
        
    if zip_dataset(output_dir):
        cleanup_dataset(output_dir)
        
        if args.interactive:
            clear_screen()
            print("=" * 60)
            print("      LoRA Dataset Generator - Complete")
            print("=" * 60)
            print("\nDataset creation completed successfully!")
            print(f"The dataset has been saved to: dataset_ready.zip")
            print("\nThank you for using the LoRA Dataset Generator.")
            input("\nPress Enter to exit...")
        else:
            logging.info("Dataset creation completed successfully!")

if __name__ == "__main__":
    main()