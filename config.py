import os

telegram_token = os.environ.get("TELEGRAM_TOKEN", "")
allowed_telegram_usernames = []
new_dialog_timeout = 3600
enable_message_streaming = True
return_n_generated_images = 1
image_size = "1024x1024"
n_chat_modes_per_page = 5
help_group_chat_video_path = None

models = {
    "available_text_models": ["gpt-4o-mini"],
    "info": {
        "gpt-4o-mini": {
            "name": "GPT-4o Mini",
            "description": "Fast and smart model.",
            "scores": {"Speed": 5, "Intelligence": 4},
            "price_per_1000_input_tokens": 0.00015,
            "price_per_1000_output_tokens": 0.0006,
            "vision": True
        },
        "gpt-image-1": {
            "price_per_1_image": 0.04
        },
        "whisper": {
            "price_per_1_min": 0.006
        }
    }
}

chat_modes = {
    "general": {
        "name": "💬 General Assistant",
        "welcome_message": "Hi! How can I help you today?",
        "parse_mode": "html"
    }
}
