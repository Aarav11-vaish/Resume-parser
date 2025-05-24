import re
import nltk
from pdfminer.high_level import extract_text as pdfminer_extract_text
from summa import summarizer
from fuzzywuzzy import fuzz

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Regex patterns
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
URL_REG = re.compile(r'http[s]?://\S+')
HYPERLINK_REG = re.compile(r'https?://\S+')

# Reserved institution keywords
RESERVED_WORDS = [
    'school', 'college', 'univers', 'academy', 'faculty', 'institute', 'faculdades',
    'schola', 'schule', 'lise', 'lyceum', 'lycee', 'polytechnic', 'kolej', 'ünivers', 'okul',
]

# Shortened skills list for demo; use your full list in practice
SKILLS_DB = [
    'python', 'java', 'c++', 'javascript', 'sql', 'html', 'css', 'react', 'nodejs',
    'machine learning', 'deep learning', 'data science', 'django', 'flask', 'tensorflow'
]

# --- Extractor Functions ---

def extract_text_from_pdf(pdf_path):
    try:
        return pdfminer_extract_text(pdf_path)
    except Exception as e:
        print("Error extracting PDF:", e)
        return ""

def extract_phone_number(text):
    phone = re.findall(PHONE_REG, text)
    if phone:
        number = ''.join(phone[0])
        if len(number) < 16:
            return number
    return None

def extract_emails(text):
    return re.findall(EMAIL_REG, text)

def extract_urls(text):
    return re.findall(URL_REG, text)

def extract_hyperlinks(text):
    return re.findall(HYPERLINK_REG, text)

def extract_skills(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [w.lower() for w in nltk.word_tokenize(text) if w.isalpha() and w.lower() not in stop_words]
    ngrams = list(map(' '.join, nltk.everygrams(tokens, 2, 3)))
    found = set()

    for token in tokens + ngrams:
        if token in SKILLS_DB:
            found.add(token)
    return found

def extract_education(text):
    education = set()
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
                org = ' '.join(c[0] for c in chunk.leaves())
                for keyword in RESERVED_WORDS:
                    if fuzz.partial_ratio(keyword.lower(), org.lower()) > 80:
                        education.add(org)
    return education

def summarize_text(text):
    return summarizer.summarize(text)
