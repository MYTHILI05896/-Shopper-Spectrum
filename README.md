er Segmentation and Product Recommendations in E-Commerce

# 🛍️ Shopper Spectrum

**Shopper Spectrum** is an AI-powered Streamlit web application for analyzing customer behavior and recommending similar products based on historical transaction data. It combines:

- 🎯 **Customer Segmentation** using RFM (Recency, Frequency, Monetary) analysis + K-Means Clustering  
- 🤖 **Product Recommendation System** using cosine similarity between product descriptions

> Built using Python, Streamlit, and Machine Learning — ready for production and GitHub deployment.

---

## 🚀 Live Demo

Run the app locally with:

```bash
streamlit run app/streamlit_app.py
```

> Or deploy it to [Streamlit Cloud](https://streamlit.io/cloud) for public access.

---

## 📂 Project Structure

```
- shopper-spectrum/
  ├── app/
  │   └── streamlit_app.py              # 📱 Streamlit front-end
  ├── data/
  │   ├── online_retail.csv             # 📦 Raw dataset
  │   └── cleaned_data.csv              # ✅ Cleaned dataset used by the app
  ├── models/
  │   ├── kmeans_model.pkl              # 🎯 Trained K-Means clustering model
  │   ├── scaler.pkl                    # 📊 StandardScaler for RFM features
  │   └── product_similarity.pkl        # 🤖 Cosine similarity matrix for products
  ├── notebooks/
  │   ├── 01_data_cleaning.ipynb
  │   ├── 02_rfm_clustering.ipynb
  │   ├── 03_product_similarity.ipynb
  │   └── 04_recommendation_system.ipynb
  ├── requirements.txt
  └── README.md                         # 📘 This file
```

---

## 📊 Features

### 🔁 Product Recommender

- Uses **cosine similarity** between product descriptions
- Recommends **Top 5** similar products for any selected item

### 👤 RFM Segmentation

- Predicts customer segment using:
  - **Recency**: Days since last purchase
  - **Frequency**: Number of transactions
  - **Monetary**: Total spend
- K-Means clustering assigns customers to behavior-based groups

### ⚙️ Machine Learning Models

- Models trained in Jupyter Notebooks (`notebooks/`)
- Stored as `.pkl` files and tracked via **Git LFS** for large file support

---

## 📦 Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/-Shopper-Spectrum.git
cd -Shopper-Spectrum/shopper-spectrum
```

### 2️⃣ Create a virtual environment

```bash
python3 -m venv ../.venv
source ../.venv/bin/activate
```

### 3️⃣ Install required packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app/streamlit_app.py
```

---

## 🛠️ Technologies Used

- **Python 3.12+**
- **Pandas, NumPy, Scikit-learn, Joblib**
- **Streamlit** (for interactive UI)
- **Git LFS** for storing large `.pkl` model files
- **Matplotlib / Seaborn** for visualization in notebooks

---



## 🧪 How It Works

1. The app loads trained models and preprocessed data from `models/` and `data/`.
2. You can:
   - **Get Product Recommendations** based on a selected item
   - **Predict Customer Segment** based on manual RFM inputs
3. The models are trained offline using Jupyter notebooks inside the `notebooks/` folder.

---

## ✅ Example Outputs

### 🎯 RFM Segment Prediction
```
Input:
  Recency = 5, Frequency = 15, Monetary = 500.0

Output:
  Cluster 2 (High Value Customer)
```

### 🔁 Product Recommendations
```
Input Product:
  "WHITE HANGING HEART T-LIGHT HOLDER"

Output:
  - GIN + TONIC DIET METAL SIGN
  - RED HANGING HEART T-LIGHT HOLDER
  - WASHROOM METAL SIGN
  - LAUNDRY 15C METAL SIGN
  - GREEN VINTAGE SPOT BEAKER
```

---

## 🧾 License

MIT License © 2025 — Mythili N  
You are free to use, distribute, and adapt this project for personal or educational purposes.

---

## 🙌 Acknowledgements

- 📊 Dataset Source: [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
- 🎈 Streamlit for their awesome open-source web framework
- 🤝 GitHub & Git LFS for seamless model tracking

---

## ✉️ Contact

Feel free to connect or raise issues on GitHub!  
📧 m9808262@gmail.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/mythili-n-2a7038369?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )
