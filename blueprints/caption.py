from flask import Blueprint, render_template, request, jsonify
from core.api_client import generate_ai_response

caption_bp = Blueprint("caption", __name__)


@caption_bp.route("/caption")
def caption_page():
    return render_template("caption.html")


@caption_bp.route("/api/generate-caption", methods=["POST"])
def generate_caption():

    data = request.get_json()

    topic = data.get("topic", "")
    platform = data.get("platform", "Instagram")

    if not topic.strip():
        return jsonify({
            "error": "Topic is required"
        }), 400

    system_prompt = """
You are a viral social media caption expert.

Generate:
- engaging captions
- hashtags
- emojis
- hooks
"""

    user_prompt = f"""
Generate captions for:

Topic:
{topic}

Platform:
{platform}
"""

    result = generate_ai_response(system_prompt, user_prompt)

    return jsonify({
        "result": result
    })