# Thought Summarizer

A simple Flask web app that analyzes your thoughts using free AI models.

## Features

- **Thought Analysis:**  
  - Enter a thought and get the 3 main ideas (summarized using a transformer model).
  - Get the overall feeling (sentiment analysis).

## How It Works

- Uses [HuggingFace Transformers](https://huggingface.co/transformers/) for:
  - Summarization (`facebook/bart-large-cnn`)
  - Sentiment analysis (`distilbert-base-uncased-finetuned-sst-2-english`)
- All logic is contained in a single Flask file (`app.py`).
- No API keys required; all processing is local and free.

## Setup Instructions

1. **Copy the files to a folder:**  
   Place `app.py`, `requirements.txt`, and this `README.md` in the same directory.

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open your browser** and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage

1. Enter a thought in the textarea and click "Analyze".
2. The app will display:
   - The 3 main ideas extracted from your thought.
   - The overall feeling (positive/negative/neutral) with a confidence score.

## Notes

- The first run may take a while as models are downloaded.
- For best results, use clear, concise thoughts or longer text.

## File Structure

- `app.py` — Main Flask application.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.

---

Made by [alex-t-reed](https://github.com/alex-t-reed)
