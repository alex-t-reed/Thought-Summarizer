from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Load pipelines (will download models if not present)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def index():
    thought = ""
    summary = []
    feeling = ""
    if request.method == "POST":
        action = request.form.get("action")
        if action == "analyze":
            thought = request.form.get("thought", "")
            if thought.strip():
                summary = extract_main_ideas(thought)
                feeling = analyze_feelings(thought)
    return render_template(
        "index.html",
        thought=thought,
        summary=summary,
        feeling=feeling
    )

def extract_main_ideas(text, n=3):
    # Dynamically set max_length/min_length for better accuracy
    input_len = len(text.split())
    if input_len < 20:
        max_length = min(20, input_len)
        min_length = max(5, input_len // 2)
    else:
        max_length = min(60, int(input_len * 0.7))
        min_length = max(15, int(input_len * 0.3))
    # Ensure valid values
    max_length = max(max_length, min_length + 1)
    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )[0]['summary_text']
    # Split summary into sentences, pick up to n
    ideas = [s.strip() for s in summary.split('.') if s.strip()]
    return ideas[:n]

def analyze_feelings(text):
    results = sentiment(text)
    # Return the most common label
    label = results[0]['label']
    score = results[0]['score']
    return f"{label} ({score:.2f})"

if __name__ == "__main__":
    app.run(debug=True)
