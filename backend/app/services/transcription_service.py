import os
import whisper
import tempfile
import torch
from flask import current_app, abort
from werkzeug.utils import secure_filename
from pathlib import Path


def get_device():
    if torch.cuda.is_available():
        return "cuda"
    elif hasattr(torch.version, "hip") and torch.version.hip is not None:
        return "rocm"
    else:
        return "cpu"


def transcribe_audio(file):
    try:
        # Get the file extension
        _, file_extension = os.path.splitext(secure_filename(file.filename))

        # Create a temporary file with the correct extension
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=file_extension
        ) as temp_file:
            file.save(temp_file)
            temp_file_path = temp_file.name

        # Check if CUDA is available and set the device
        device = get_device()
        current_app.logger.info(f"Using device: {device}")

        if device == "cuda":
            current_app.logger.info(f"CUDA device: {torch.cuda.get_device_name(0)}")
        elif device == "rocm":
            current_app.logger.info("Using ROCm for AMD GPU")
        else:
            current_app.logger.info("Using CPU")

        # Load the model with the specified device
        model_name = current_app.config.get("WHISPER_MODEL", "base")
        current_app.logger.info(f"Using Whisper model: {model_name}")

        try:
            model = whisper.load_model(model_name).to(device)
        except ValueError as e:
            if "is not a valid model name" in str(e):
                current_app.logger.error(f"Invalid Whisper model: {model_name}")
                abort(400, description=f"Invalid Whisper model: {model_name}")
            raise

        # Transcribe the audio file
        result = model.transcribe(temp_file_path)

        return {"transcription": result["text"]}
    except Exception as e:
        current_app.logger.error(f"Transcription error: {str(e)}")
        abort(500, description="An error occurred during transcription")
    finally:
        # Ensure temporary file is deleted even if an exception occurs
        if "temp_file_path" in locals() and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

# The save_transcription function has been removed
