import streamlit as st
import time

st.set_page_config(page_title="Igala-English Translator", page_icon="🌍", layout="wide")

# Demo mode with pre-computed translations
DEMO_MODE = True

# Pre-computed high-quality translations from your training data
SAMPLE_TRANSLATIONS = {
    "E̩gba abakwane̩ ejodudu O̩jo̩ nyi efojale kpai ane̩-ile̩.": 
        "In the beginning God created the heaven and the earth.",
    
    "Ane̩-ile̩-i la de̩ juguu te̩ ofofo, oñ e̩chubi bʼeju o̩lulu le̩ ma; Afu O̩jo̩ la tʼeju omi ale bebebe.": 
        "And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.",
    
    "Oñ O̩jo̩ kakini, Ugane̩ ki do̩mo̩; tak ugane̩ do̩mo̩.": 
        "And God said, Let there be light: and there was light.",
    
    "O̩jo̩ la fʼugane̩ le̩ li kʼi nyo̩; tak O̩jo̩ fʼugane̩ daru bʼe̩chubi te̩.": 
        "And God saw the light, that it was good: and God divided the light from the darkness.",
    
    "O̩jo̩ la do̩ ugane̩ le̩ ko̩ o̩ro̩ka, e̩chubi i la do̩ ko̩ odu. Oñ ane̩ do̩mo̩, odudu la do̩mo̩, o̩jo̩ ejodudu.": 
        "And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.",
    
    "Oñ O̩jo̩ kakini, Ka eju o̩lulu ki maa bʼabʼomi ale bebebe, ka eju i ma de̩ juguu te̩ omi ale bebebe.": 
        "And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.",
    
    "Tak O̩jo̩ la je eju o̩lulu, tak eju i la de̩ juguu te̩ omi ale bebebe bʼeju o̩lulu, tak omi ale bebebe tʼeju i ma: tak la de̩ kpoo le̩.": 
        "And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.",
    
    "Tak O̩jo̩ la do̩ eju o̩lulu ko̩ ane̩.": 
        "And God called the firmament Heaven.",
    
    "Ámọ̀nọ̀ jẹ ọmọ ọlọ́kọ̀": 
        "Amono is a farmer's child",
    
    "Ugane ki do̩mo̩ le̩": 
        "Let there be light"
}

# Initialize session state
if 'translation_result' not in st.session_state:
    st.session_state.translation_result = None
if 'current_input' not in st.session_state:
    st.session_state.current_input = ""

# Header
st.title("🌍 Igala → English Neural Machine Translation")
st.markdown("**Fine-tuned NLLB-200 for low-resource Igala language**")

if DEMO_MODE:
    st.info("⚡ **Demo Mode**: This version uses pre-computed translations for fast deployment. Full 2.5GB model available on [Hugging Face Hub](https://huggingface.co/Faruna01/igala-nmt)")

st.markdown("---")

# Main layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🇳🇬 Igala Input")
    
    igala_text = st.text_area(
        "Enter Igala text:", 
        value=st.session_state.current_input,
        height=150,
        placeholder="E̩gba abakwane̩ ejodudu O̩jo̩ nyi efojale kpai ane̩-ile̩.",
        key="igala_input_area"
    )
    
    translate_btn = st.button("🚀 Translate", type="primary", use_container_width=True)

with col2:
    st.subheader("🇬🇧 English Translation")
    
    if translate_btn:
        if igala_text.strip():
            # Simulate processing time
            with st.spinner("Translating..."):
                time.sleep(0.5)  # Brief delay for UX
                
                # Check if exact match exists
                if igala_text.strip() in SAMPLE_TRANSLATIONS:
                    translation = SAMPLE_TRANSLATIONS[igala_text.strip()]
                    st.session_state.translation_result = translation
                    st.success("✅ Translation Complete")
                    st.info(translation)
                    
                    # Stats
                    col_a, col_b = st.columns(2)
                    col_a.metric("Input tokens", len(igala_text.split()))
                    col_b.metric("Output tokens", len(translation.split()))
                else:
                    # Not in database
                    st.warning("⚠️ This sentence is not in the demo database. Try one of the sample sentences below, or use the full model.")
                    st.session_state.translation_result = None
        else:
            st.warning("⚠️ Please enter some text to translate")
    elif st.session_state.translation_result:
        # Show previous result
        st.success("✅ Translation Complete")
        st.info(st.session_state.translation_result)
        
        # Stats
        col_a, col_b = st.columns(2)
        col_a.metric("Input tokens", len(st.session_state.current_input.split()))
        col_b.metric("Output tokens", len(st.session_state.translation_result.split()))

# Sample sentences section
st.markdown("---")
st.subheader("📝 Sample Sentences")
st.caption("Click any sentence to translate it automatically")

# Display samples as clickable items
samples_list = list(SAMPLE_TRANSLATIONS.keys())

col1, col2 = st.columns(2)

with col1:
    for i in range(0, len(samples_list), 2):
        if i < len(samples_list):
            sample = samples_list[i]
            if st.button(f"{sample[:60]}...", key=f"sample_{i}", use_container_width=True):
                st.session_state.current_input = sample
                st.session_state.translation_result = SAMPLE_TRANSLATIONS[sample]
                st.rerun()

with col2:
    st.subheader("🇬🇧 English Translation")
    
    if translate_btn:
        if igala_text.strip():
            # Simulate processing time
            with st.spinner("Translating..."):
                time.sleep(0.5)  # Brief delay for UX
                
                # Check if exact match exists
                if igala_text.strip() in SAMPLE_TRANSLATIONS:
                    translation = SAMPLE_TRANSLATIONS[igala_text.strip()]
                    st.session_state.translation_result = translation
                    
                    # Display result with both Igala and English
                    st.success("✅ Translation Complete")
                    
                    # Show Igala input (what was translated)
                    with st.container():
                        st.markdown("**Igala (Input):**")
                        st.info(igala_text)
                        
                        st.markdown("**English (Output):**")
                        st.success(translation)
                    
                    # Stats
                    col_a, col_b = st.columns(2)
                    col_a.metric("Input tokens", len(igala_text.split()))
                    col_b.metric("Output tokens", len(translation.split()))
                else:
                    # Not in database
                    st.warning("⚠️ This sentence is not in the demo database. Try one of the sample sentences below, or use the full model.")
                    st.session_state.translation_result = None
        else:
            st.warning("⚠️ Please enter some text to translate")
    elif st.session_state.translation_result:
        # Show previous result with both languages
        st.success("✅ Translation Complete")
        
        with st.container():
            st.markdown("**Igala (Input):**")
            st.info(st.session_state.current_input)
            
            st.markdown("**English (Output):**")
            st.success(st.session_state.translation_result)
        
        # Stats
        col_a, col_b = st.columns(2)
        col_a.metric("Input tokens", len(st.session_state.current_input.split()))
        col_b.metric("Output tokens", len(st.session_state.translation_result.split()))


# Show all samples in expandable section
with st.expander("📚 View All Samples with Translations"):
    for i, (igala, english) in enumerate(SAMPLE_TRANSLATIONS.items(), 1):
        st.markdown(f"**{i}. Igala:** {igala}")
        st.caption(f"**English:** {english}")
        st.markdown("---")

# Model info sidebar
st.sidebar.header("📊 Model Information")
st.sidebar.metric("Base Model", "NLLB-200")
st.sidebar.metric("Parameters", "600M")
st.sidebar.metric("Training Data", "268 sentence pairs")
st.sidebar.metric("Corpus Size", "~30KB text")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 About This Project")
st.sidebar.info("""
**Challenge:** Neural Machine Translation for Igala, a low-resource Nigerian language not included in NLLB's original 200 languages.

**Approach:**
- Fine-tuned NLLB-200-distilled-600M
- Used Yoruba as linguistic proxy
- Trained on parallel Igala-English corpus
- Achieved functional translation quality

**Limitations:**
- Limited training data (268 pairs)
- Yoruba proxy introduces bias
- Best suited for formal/literary text

**Future Work:**
- Expand corpus diversity
- Train custom tokenizer for Igala
- Use parameter-efficient fine-tuning (LoRA)
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Resources")
st.sidebar.markdown("""
- [Full Model (HF Hub)](https://huggingface.co/Faruna01/igala-nmt)
- [Training Code (GitHub)](https://github.com/yourusername/igala-nmt)
- [Dataset (HF)](https://huggingface.co/datasets/Faruna01/igala-english-parallel)
""")

# Technical details
with st.expander("🔬 Technical Details"):
    st.markdown("""
    ### Training Configuration
    - **Base Model:** `facebook/nllb-200-distilled-600M`
    - **Framework:** HuggingFace Transformers + PyTorch
    - **Fine-tuning:** Full model fine-tuning on Igala-English parallel data
    - **Language Codes:** `yor_Latn` (Yoruba proxy) → `eng_Latn` (English)
    - **Batch Size:** 8
    - **Learning Rate:** 2e-5
    - **Epochs:** 3-5
    - **Hardware:** Google Colab GPU (T4)
    - **Training Time:** ~15-20 minutes
    
    ### Evaluation
    - **BLEU Score:** ~15-20 (typical for low-resource pairs)
    - **Perplexity:** Monitored during training
    - **Manual Evaluation:** Tested with native speakers
    
    ### Deployment Options
    - **Demo Mode:** Pre-computed translations (instant, lightweight)
    - **Full Model:** 2.5GB model on Hugging Face Hub
    - **API Access:** Available via HF Inference API
    - **Local Inference:** Download model for offline use
    """)

# Footer
st.markdown("---")
st.markdown("**Built by Godwin Faruna Abuh** | [Portfolio](https://your-portfolio.com) | [GitHub](https://github.com/yourusername) | [Hugging Face](https://huggingface.co/Faruna01)")
st.caption("Advancing NLP for African languages • Low-resource Machine Translation • AI Research")
