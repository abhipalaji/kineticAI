from flask import Blueprint, render_template, request, jsonify
from core.api_client import generate_ai_response

ad_writer_bp = Blueprint("ad_writer", __name__)


# PAGE ROUTE
@ad_writer_bp.route("/ad-writer")
def ad_writer_page():
    return render_template("ad_writer.html")


# API ROUTE
@ad_writer_bp.route("/api/generate-ad", methods=["POST"])
def generate_ad():

    data = request.get_json()

    product = data.get("product", "")
    audience = data.get("audience", "")
    platform = data.get("platform", "Instagram")
    tone = data.get("tone", "Persuasive")

    if not product.strip():

        return jsonify({
            "error": "Product is required"
        }), 400

    system_prompt = f"""
You are an elite direct-response copywriter.

Your job is to create HIGH-CONVERTING ad copy.

RULES:
- Write emotional hooks
- Use persuasive psychology
- Create urgency
- Make it engaging
- Include strong CTA
- Keep it platform optimized
- Make copy premium quality

PLATFORM:
{platform}

TONE:
{tone}

Return:
1. Headline
2. Main Ad Copy
3. CTA
4. Bonus Hook Variations
"""

    user_prompt = f"""
Create a high-converting advertisement.

PRODUCT:
{product}

TARGET AUDIENCE:
{audience}
"""

    result = generate_ai_response(system_prompt, user_prompt)

    return jsonify({
        "result": result
    })