import os
import whisper
import tempfile
from flask import current_app
from werkzeug.utils import secure_filename


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

        # Load the model (consider moving this outside the function if possible)
        model = whisper.load_model(current_app.config.get("WHISPER_MODEL", "base"))

        # Transcribe the audio file
        result = model.transcribe(temp_file_path)

        # Delete the temporary file
        os.unlink(temp_file_path)

        return {"transcription": result["text"]}
    except Exception as e:
        current_app.logger.error(f"Transcription error: {str(e)}")
        return {"error": "An error occurred during transcription"}, 500
    finally:
        # Ensure temporary file is deleted even if an exception occurs
        if "temp_file_path" in locals() and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
