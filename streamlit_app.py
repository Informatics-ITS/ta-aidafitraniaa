import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re

# Normalisasi 
alay_dict = {
    "gk": "tidak", "ga": "tidak", "ngga": "tidak", "nggak": "tidak", "tdk": "tidak",
    "tak": "tidak", "bgt": "banget", "bgtu": "banget", "sm": "sama", "syg": "sayang",
    "jg": "juga", "udh": "sudah", "tp": "tapi", "dr": "dari", "dgn": "dengan",
    "aja": "saja", "km": "kamu", "aq": "aku", "trs": "terus", "yg": "yang", 
    "trus": "terus", "t'rus": "terus", "tlah": "telah", "t'lah": "telah", "kan": "akan",
    "tuk": "untuk", "slalu": "selalu", "s'lalu": "selalu", "ku": "aku", "skrg": "sekarang",
    "bsk": "besok", "blm": "belum", "lg": "lagi"
}

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)       # hapus tanda baca
    text = re.sub(r'\d+', '', text)           # hapus angka
    text = text.lower()                       # ubah ke lowercase
    words = text.split()
    words = [alay_dict.get(w, w) for w in words]  # normalisasi alay
    return ' '.join(words)

# Load model & tokenizer
@st.cache_resource
def load_model():
    model_path = "final_best_model_fold_4"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

tokenizer, model = load_model()
label_map = {0: 'senang', 1: 'sedih', 2: 'tenang', 3: 'marah'}

# UI Streamlit
st.title("🎶 Klasifikasi Emosi Lagu Indonesia")
text = st.text_area("Masukkan lirik lagu:", height=200)

if st.button("Prediksi Emosi"):
    if text.strip() == "":
        st.warning("Tolong masukkan lirik terlebih dahulu.")
    else:
        cleaned_text = clean_text(text)

        st.markdown("### 🔍 Hasil Preprocessing Lirik")
        st.code(cleaned_text)

        # Tokenisasi dan prediksi
        inputs = tokenizer(cleaned_text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)
            pred = torch.argmax(probs, dim=1).item()
            pred_label = label_map[pred]

        # Hasil prediksi saja (tanpa penjelasan)
        st.markdown("### 🔮 Hasil Prediksi Emosi")
        st.success(f"✅ **Prediksi Emosi: {pred_label}**")
