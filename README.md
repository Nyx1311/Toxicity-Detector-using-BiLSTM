Toxicity Detector using BiLSTM

A deep learning model to classify the degree of toxicity in user comments using a **Bidirectional LSTM (BiLSTM)** network.  
This project aims to automatically detect toxic, offensive, or harmful language in text, making online communities safer.

---

## ✨ Features
- Preprocessing pipeline for raw text (cleaning, tokenization, padding).
- Word embeddings for rich semantic representation.
- **BiLSTM-based classifier** for sequence modeling.
- Trained on labeled comment datasets for toxicity detection.
- Supports multiple levels of toxicity classification (toxic, severe toxic, obscene, threat, insult, identity hate).

---

## ⚙️ Tech Stack
- **Python 3**
- **TensorFlow / Keras**
- **BiLSTM (Bidirectional Long Short-Term Memory)**
- **NumPy, Pandas** for data handling
- **Matplotlib / Seaborn** for visualization
- **Streamlit** for deployment as a simple web app


---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Nyx1311/Toxicity-Detector-using-BiLSTM.git
cd Toxicity-Detector-using-BiLSTM
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
jupyter notebook Comment_Toxicity_using_BiLSTM.ipynb
```

### 4. Run the web app

```bash
streamlit run toxicity_app_streamlit.py
```

---

## 📊 Results

* Achieved strong accuracy on multi-label toxicity classification.
* BiLSTM captures context from both directions, improving prediction quality compared to vanilla LSTM.

*(Insert confusion matrix, accuracy/loss plots here.)*

---

## 📌 Future Improvements

* Integrate pre-trained embeddings (e.g., GloVe, fastText).
* Explore Transformer-based models (BERT, RoBERTa).
* Deploy a production-ready API.

---

## 🧑‍💻 Author

Developed by **[Nyx1311](https://github.com/Nyx1311)**.

`

