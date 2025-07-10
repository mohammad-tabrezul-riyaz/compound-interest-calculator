import streamlit as st

st.set_page_config(page_title="Compound Interest Calculator", page_icon="📈")
st.title("📈 Compound Interest Calculator")

# Input
P = st.number_input("🪙 Principal (₹)", min_value=0.0, format="%.2f")
R = st.number_input("📈 Rate of Interest (%)", min_value=0.0)
T = st.number_input("⏳ Time (in years)", min_value=0.0)
frequency = st.selectbox("🔁 Compounded", ["Annually", "Half-Yearly", "Quarterly", "Monthly", "Daily"])

# Frequency mapping
freq_map = {
    "Annually": 1,
    "Half-Yearly": 2,
    "Quarterly": 4,
    "Monthly": 12,
    "Daily": 365
}
n = freq_map[frequency]

# Calculate
if P > 0 and R > 0 and T > 0:
    A = P * (1 + R/(100*n))**(n*T)
    CI = A - P

    st.markdown(f"### 💰 Final Amount: ₹{A:,.2f}")
    st.markdown(f"### 🧮 Interest Earned: ₹{CI:,.2f}")
else:
    st.info("👆 Enter all values to see the result")
