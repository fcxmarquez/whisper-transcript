from flask import Blueprint, request, jsonify
from app.services.transcription_service import transcribe_audio

bp = Blueprint("api", __name__)


@bp.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if file:
        result = transcribe_audio(file)
        return jsonify(result)
