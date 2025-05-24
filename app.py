from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tempfile
# to run this use source venv/Scripts/activate for a virtual environment
from extractors import (
    extract_text_from_pdf, extract_phone_number, extract_emails, extract_urls,
    extract_hyperlinks, extract_skills, extract_education, summarize_text
)

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files or request.files['resume'].filename == '':
        return jsonify({'success': False, 'message': 'No file uploaded'})

    file = request.files['resume']
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        file.save(tmp.name)
        pdf_text = extract_text_from_pdf(tmp.name)

    if not pdf_text:
        return jsonify({'success': False, 'message': 'Could not extract text from PDF'})

    result = {
        'success': True,
        'phone_number': extract_phone_number(pdf_text),
        'emails': extract_emails(pdf_text),
        'urls': extract_urls(pdf_text),
        'hyperlinks': extract_hyperlinks(pdf_text),
        'skills': list(extract_skills(pdf_text)),
        'education': list(extract_education(pdf_text)),
        'summary': summarize_text(pdf_text)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
