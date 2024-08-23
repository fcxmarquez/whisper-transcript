import os
import whisper
from whisper.utils import get_writer
from pathlib import Path
from flask import current_app
from werkzeug.utils import secure_filename


def transcribe_audio(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    model = whisper.load_model(current_app.config["MODEL_SIZE"])
    result = model.transcribe(filepath)

    audio_name = Path(filename).stem
    output_directory = f"./transcripts/{audio_name}/{current_app.config['MODEL_SIZE']}"
    os.makedirs(output_directory, exist_ok=True)

    no_breaks_path = os.path.join(output_directory, "transcription_no_breaks.txt")
    with open(no_breaks_path, "w", encoding="utf-8") as txt:
        txt.write(result["text"])

    txt_writer = get_writer("txt", output_directory)
    txt_writer(result, filepath)

    return {"transcription": result["text"], "output_directory": output_directory}
