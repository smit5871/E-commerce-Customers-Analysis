import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Page Config (Design)
# -----------------------------
st.set_page_config(
    page_title="Customer Spending Predictor",
    page_icon="💰",
    layout="centered"
)

# -----------------------------
# Load trained model
# -----------------------------
with open("ecommerce_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# App Title
# -----------------------------
st.markdown(
    "<h1 style='text-align:center;'>💰 Customer Spending Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; font-size:16px;'>Predict <b>Yearly Amount Spent</b> based on customer behavior</p>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# User Inputs (SLIDERS)
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    avg_session_length = st.slider(
        "Avg. Session Length (minutes)",
        0.0, 40.0, 20.0, 0.1
    )

    time_on_app = st.slider(
        "Time on App (minutes)",
        0.0, 25.0, 12.0, 0.1
    )

with col2:
    time_on_website = st.slider(
        "Time on Website (minutes)",
        0.0, 45.0, 22.0, 0.1
    )

    length_of_membership = st.slider(
        "Length of Membership (years)",
        0.0, 10.0, 5.0, 0.1
    )


# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Yearly Amount Spent", use_container_width=True):

    input_data = np.array([[
        avg_session_length,
        time_on_app,
        time_on_website,
        length_of_membership
    ]])

    prediction = model.predict(input_data)[0]

    # -----------------------------
    # Conditional Styling
    # -----------------------------
    if prediction < 0:
        st.error(
            f"🔴 **Predicted Yearly Amount Spent:** ₹ {prediction:,.2f}"
        )
    else:
        st.success(
            f"🟢 **Predicted Yearly Amount Spent:** ₹ {prediction:,.2f}"
        )

    # -----------------------------
    # Input Summary (Attractive)
    # -----------------------------
    with st.expander("📊 View Input Summary"):
        st.write(f"- **Avg. Session Length:** {avg_session_length} minutes")
        st.write(f"- **Time on App:** {time_on_app} minutes")
        st.write(f"- **Time on Website:** {time_on_website} minutes")
        st.write(f"- **Length of Membership:** {length_of_membership} years")