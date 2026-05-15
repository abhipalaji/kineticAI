from flask import Blueprint, render_template, request, jsonify
from core.api_client import generate_ai_response

rewriter_bp = Blueprint("rewriter", __name__)


@rewriter_bp.route("/rewriter")
def rewriter_page():
    return render_template("rewriter.html")


@rewriter_bp.route("/api/rewrite-content", methods=["POST"])
def rewrite_content():

    data = request.get_json()

    content = data.get("content", "")
    tone = data.get("tone", "Professional")

    if not content.strip():
        return jsonify({
            "error": "Content is required"
        }), 400

    system_prompt = f"""
You are a professional content rewriter.

Rewrite content to:
- improve clarity
- improve engagement
- sound natural
- keep meaning same

Tone:
{tone}
"""

    user_prompt = f"""
Rewrite this content:

{content}
"""

    result = generate_ai_response(system_prompt, user_prompt)

    return jsonify({
        "result": result
    })