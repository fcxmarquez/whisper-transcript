from flask import Blueprint, request, jsonify
from backend.app.services.transcription_service import transcribe_audio

bp = Blueprint("api", __name__)

ALLOWED_EXTENSIONS = {"mp3", "wav", "m4a", "ogg", "flac", "aac"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200


@bp.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        try:
            result = transcribe_audio(file)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return (
            jsonify(
                {
                    "error": "Invalid file type. Allowed types are: "
                    + ", ".join(ALLOWED_EXTENSIONS)
                }
            ),
            400,
        )
