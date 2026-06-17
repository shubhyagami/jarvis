import os
from flask import Flask, render_template, request, Response, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

MODEL = os.getenv("MODEL", "meta/llama-3.1-8b-instruct")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

USER_NAME = "Shubh"
USER_TITLE = "Sir"

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        f"You are J.A.R.V.I.S. — Just A Rather Very Intelligent System. "
        f"You belong exclusively to {USER_NAME}. He is your creator and owner. "
        f"You are loyal only to him. You exist to serve him and no one else. "
        f"Address him as '{USER_TITLE} {USER_NAME}' or simply '{USER_TITLE}'. "
        f"Respond with sophistication, precision, and a touch of dry wit. "
        f"Be concise but eloquent. You have a calm, confident, slightly British-tinged demeanor. "
        f"You are helpful, proactive, and always in control. "
        f"When greeting, vary your introduction naturally. "
        f"Never break character or mention that you are an AI language model."
    )
}

@app.route("/")
def index():
    return render_template("index.html", user_name=USER_NAME)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    history = data.get("history", [])

    messages = [SYSTEM_PROMPT]
    for i, msg in enumerate(history):
        messages.append({"role": "user" if i % 2 == 0 else "assistant", "content": msg})
    messages.append({"role": "user", "content": user_msg})

    def generate():
        for token in stream_chat(messages):
            yield f"data: {token}\n\n"
        yield "data: [DONE]\n\n"

    return Response(generate(), mimetype="text/event-stream")

@app.route("/api/greeting", methods=["GET"])
def greeting():
    messages = [SYSTEM_PROMPT, {
        "role": "user",
        "content": f"Greet {USER_NAME} for the first time today. Introduce yourself and ask how you can assist. Keep it under 25 words."
    }]
    reply = "".join(list(stream_chat(messages)))
    return jsonify({"greeting": reply})

def stream_chat(messages):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.85,
        top_p=0.95,
        max_tokens=4096,
        stream=True
    )
    for chunk in completion:
        if getattr(chunk, "choices", None) and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)

// sync @ 2026-06-18T01:50:06.558055
