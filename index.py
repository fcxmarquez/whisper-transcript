import os
from dotenv import load_dotenv
import whisper
from whisper.utils import get_writer
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Use environment variables
model_size = os.getenv("MODEL_SIZE", "medium")
audio_file = os.getenv("AUDIO_FILE")

model = whisper.load_model(model_size)
result = model.transcribe(audio_file)

# Extract the name of the recording without extension
audio_name = Path(audio_file).stem

# Create the output directory using the requested structure
output_directory = f"./transcripts/{audio_name}/{model_size}"
os.makedirs(output_directory, exist_ok=True)

# Save as a TXT file without any line breaks
no_breaks_path = os.path.join(output_directory, "transcription_no_breaks.txt")
with open(no_breaks_path, "w", encoding="utf-8") as txt:
    txt.write(result["text"])

# Save as a TXT file with hard line breaks
txt_writer = get_writer("txt", output_directory)
txt_writer(result, audio_file)

print(f"Transcriptions saved in {output_directory}")