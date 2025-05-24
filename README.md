# 📄 Resume Parser with NLP

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?logo=flask)
![NLP](https://img.shields.io/badge/NLP-SpaCy/orange)

A Flask web application that extracts and analyzes information from PDF resumes using NLP techniques.

## 🌟 Features
- 📱 Extract contact details (phone numbers, emails)
- 🔗 Identify URLs and hyperlinks
- 🛠️ Detect skills and education history
- 📝 Generate text summaries
- 🌐 Simple web interface for uploads

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/resume-parser.git
cd resume-parser

# Set up virtual environment (recommended)
python -m venv venv

# Activate environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
resume-parser/
├── app.py                # Main application logic
├── extractors.py         # NLP extraction functions
├── templates/            # Frontend files
│   └── index.html        # Upload interface
├── static/               # CSS/JS assets (if any)
├── requirements.txt      # Dependencies
└── README.md            # This file
```
#Why Use a Virtual Environment?
-Virtual environments:

-Isolate project dependencies

-Prevent conflicts between projects

-Make dependency management easier

-Are essential for production deployments

-Always activate before working:
```
###bash
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```
##📌 Dependencies
-Flask (web framework)

-pdfminer.six (PDF text extraction)

-spaCy/regex (NLP processing)

-Other packages listed in requirements.txt
