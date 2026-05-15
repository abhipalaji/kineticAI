from flask import Blueprint, render_template, request, jsonify
from core.api_client import generate_ai_response

enhancer_bp = Blueprint("enhancer", __name__)


@enhancer_bp.route("/enhancer")
def enhancer_page():
    return render_template("enhancer.html")


@enhancer_bp.route("/api/enhance-prompt", methods=["POST"])
def enhance_prompt():

    data = request.get_json()

    prompt = data.get("prompt", "")
    tone = data.get("tone", "Professional")
    category = data.get("category", "General")

    if not prompt.strip():
        return jsonify({
            "error": "Prompt is required"
        }), 400

    system_prompt = f"""
You are an elite AI Prompt Engineer.

Transform weak prompts into powerful prompts.

CATEGORY:
{category}

TONE:
{tone}

Make prompts:
- detailed
- structured
- professional
- actionable
- clear

Return ONLY the enhanced prompt.
"""

    user_prompt = f"""
Enhance this prompt:

{prompt}
"""

    result = generate_ai_response(system_prompt, user_prompt)

    return jsonify({
        "result": result
    })