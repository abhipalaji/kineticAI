from flask import Blueprint, render_template, request, jsonify
from core.api_client import generate_ai_response

blogger_bp = Blueprint("blogger", __name__)


@blogger_bp.route("/blogger")
def blogger_page():
    return render_template("blogger.html")


@blogger_bp.route("/api/generate-blog", methods=["POST"])
def generate_blog():

    data = request.get_json()

    topic = data.get("topic", "")
    tone = data.get("tone", "Professional")

    if not topic.strip():
        return jsonify({
            "error": "Topic is required"
        }), 400

    system_prompt = f"""
You are an expert blog writer.

Write:
- SEO optimized blogs
- engaging content
- detailed structure
- headings
- introduction
- conclusion

Tone:
{tone}
"""

    user_prompt = f"""
Write a detailed blog about:

{topic}
"""

    result = generate_ai_response(system_prompt, user_prompt)

    return jsonify({
        "result": result
    })