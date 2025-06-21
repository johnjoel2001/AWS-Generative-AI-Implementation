# from flask import Blueprint, request, jsonify, render_template
# from .bedrock_client import generate_text
# from .filters import is_safe
# from .usage_log import log_usage

# main = Blueprint("main", __name__)

# @main.route("/")
# def home():
#     return {"message": "Welcome to the Bedrock Text Gen API"}
# from flask import redirect


# @main.route("/ui")
# def web_ui():
#     return render_template("index.html")

# @main.route("/generate", methods=["POST"])
# def generate():
#     data = request.get_json()
#     prompt = data.get("prompt", "")
#     style = data.get("style", "default")

#     if not prompt.strip():
#         return jsonify({"error": "Prompt is required"}), 400

#     if not is_safe(prompt):
#         return jsonify({"error": "Inappropriate content detected."}), 403

#     try:
#         full_prompt = generate_prompt_template(prompt, style)
#         output = generate_text(full_prompt)
#         log_usage(prompt, style, output)
#         return jsonify({"result": output}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# def generate_prompt_template(prompt, style):
#     if style == "email":
#         return f"Write a professional email about: {prompt}"
#     elif style == "poem":
#         return f"Write a short poetic verse on: {prompt}"
#     elif style == "summary":
#         return f"Summarize this text in 3 sentences: {prompt}"
#     else:
#         return prompt

from flask import Blueprint, request, jsonify, render_template, redirect
from .bedrock_client import generate_text
from .filters import is_safe
from .usage_log import log_usage

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return redirect("/ui")  # Redirect root to UI

@main.route("/ui")
def web_ui():
    return render_template("index.html")  # Load the web frontend

@main.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    style = data.get("style", "default")

    if not prompt.strip():
        return jsonify({"error": "Prompt is required"}), 400

    if not is_safe(prompt):
        return jsonify({"error": "Inappropriate content detected."}), 403

    try:
        full_prompt = generate_prompt_template(prompt, style)
        output = generate_text(full_prompt)
        log_usage(prompt, style, output)
        return jsonify({"result": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_prompt_template(prompt, style):
    if style == "email":
        return f"Write a professional email about: {prompt}"
    elif style == "poem":
        return f"Write a short poetic verse on: {prompt}"
    elif style == "summary":
        return f"Summarize this text in 3 sentences: {prompt}"
    else:
        return prompt
