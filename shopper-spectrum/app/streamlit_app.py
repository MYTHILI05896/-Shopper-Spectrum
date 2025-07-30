import streamlit as st
import pandas as pd
import joblib

# Load models (with correct relative paths)
@st.cache_resource
def load_models():
    kmeans = joblib.load("models/kmeans_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    product_similarity = pd.read_pickle("models/product_similarity.pkl")
    return kmeans, scaler, product_similarity

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data.csv")
    return df

# Recommend similar products
def get_recommendations(product_name, similarity_matrix, top_n=5):
    if product_name not in similarity_matrix.columns:
        return pd.Series()
    similar_scores = similarity_matrix[product_name].sort_values(ascending=False)[1:top_n+1]
    return similar_scores

# Predict RFM cluster
def predict_rfm_cluster(kmeans, scaler, recency, frequency, monetary):
    input_data = pd.DataFrame([[recency, frequency, monetary]], columns=["Recency", "Frequency", "Monetary"])
    input_scaled = scaler.transform(input_data)
    cluster = kmeans.predict(input_scaled)[0]
    return cluster

# ------------------ Streamlit UI ------------------

st.set_page_config(page_title="🛍️ Shopper Spectrum", layout="wide")
st.title("🛍️ Shopper Spectrum: Customer Segmentation & Product Recommender")

# Load all resources
kmeans, scaler, similarity_df = load_models()
df = load_data()

# Tabs for app features
tab1, tab2 = st.tabs(["🔁 Product Recommendation", "👤 RFM Segment Predictor"])

# ---------- Tab 1: Product Recommendation ----------
with tab1:
    st.header("🔁 Product Recommendation")

    product_list = list(similarity_df.columns)
    selected_product = st.selectbox("Select a product to get recommendations:", product_list)

    if st.button("Get Recommendations"):
        recommendations = get_recommendations(selected_product, similarity_df)

        if not recommendations.empty:
            st.subheader("🧠 Top 5 Recommendations:")
            for i, (item, score) in enumerate(recommendations.items(), start=1):
                st.write(f"{i}. **{item}** — Similarity Score: `{score:.2f}`")
        else:
            st.warning("Sorry, no recommendations found for the selected product.")

# ---------- Tab 2: RFM Predictor ----------
with tab2:
    st.header("👤 Customer Segmentation (RFM)")

    recency = st.number_input("Recency (days since last purchase):", min_value=0)
    frequency = st.number_input("Frequency (number of orders):", min_value=0)
    monetary = st.number_input("Monetary (total spend):", min_value=0.0, format="%.2f")

    if st.button("Predict Customer Segment"):
        cluster = predict_rfm_cluster(kmeans, scaler, recency, frequency, monetary)
        st.success(f"🧬 This customer belongs to **Cluster {cluster}**.")

st.markdown("---")
st.caption("📊 Built with Streamlit | Shopper Spectrum © 2025")
