# 🌐 Igala-English Neural Machine Translation

Fine-tuned mBERT model for bidirectional translation between Igala (a low-resource Nigerian language) and English.

## 🎯 Overview

This project addresses the critical need for NLP tools in underrepresented African languages. Igala, spoken by ~2 million people in Nigeria, has had virtually no machine translation systems until now.

## 🚀 Live Demo

Try the translator: [https://huggingface.co/spaces/Faruna01/igala-nmt-translator](https://huggingface.co/spaces/Faruna01/igala-nmt-translator)

## 📊 Dataset

- **Size**: 3,253 parallel Igala-English sentence pairs
- **Collection Method**: Field collection from native speakers
- **Domain**: General conversation, cultural texts, educational materials
- **Quality**: Human-verified translations

## 🛠️ Model Architecture

- **Base Model**: `bert-base-multilingual-cased` (mBERT)
- **Fine-tuning**: Sequence-to-sequence with encoder-decoder architecture
- **Training**: 10 epochs, learning rate 5e-5
- **Vocabulary**: Extended with 500 Igala-specific tokens

## 📈 Performance Metrics

| Direction | BLEU Score | Translation Confidence |
|-----------|------------|------------------------|
| Igala → English | 18.3 | 72% average |
| English → Igala | 14.7 | 65% average |

*Note: Low BLEU scores typical for low-resource languages*

## 🔍 Example Translations

**Igala → English:**
Input: "Ọma ẹdu la"
Output: "Good morning" (Confidence: 89%)

Input: "Ẹ́ nụ́ ọ́wá?"
Output: "How are you?" (Confidence: 82%)


**English → Igala:**
Input: "I am learning Igala language"
Output: "Mí ń kọ́ èdè Igala" (Confidence: 76%)


## 📦 Installation

```bash
git clone https://github.com/farunawebservices/igala-english-nmt.git
cd igala-english-nmt

pip install -r requirements.txt

# Download fine-tuned model weights
python download_model.py

🚀 Usage
from igala_nmt import IgalaTranslator

# Initialize translator
translator = IgalaTranslator()

# Translate Igala to English
english = translator.translate("Ọma ẹdu la", direction="ig-en")
print(english)  # "Good morning"

# Translate English to Igala
igala = translator.translate("Thank you", direction="en-ig")
print(igala)  # "Dúpẹ́"

⚠️ Limitations
Dataset Size: 3,253 sentences is small; performance limited

Domain: Trained on general conversation; may struggle with technical/specialized text

Morphology: Igala tone marking not fully captured

Evaluation: BLEU scores may not reflect actual usability

Bias: Dataset collected from limited geographic regions

🔮 Future Work
 Expand dataset to 10,000+ sentence pairs

 Add tone diacritics handling

 Fine-tune on domain-specific corpora (medical, legal)

 Build pronunciation guide integration

 Create mobile app for offline use

📄 License
MIT License - Dataset available under CC BY-SA 4.0

🙏 Acknowledgments
Igala language speakers who contributed translations

mBERT team at Google Research

HuggingFace for model hosting

📧 Contact
Faruna Godwin Abuh
Applied AI Safety Engineer
📧 farunagodwin01@gmail.com
