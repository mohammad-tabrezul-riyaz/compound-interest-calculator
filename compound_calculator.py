import streamlit as st
import matplotlib.pyplot as plt

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

# Calculate and Display
if P > 0 and R > 0 and T > 0:
    A = P * (1 + R/(100*n))**(n*T)
    CI = A - P

    st.markdown(f"### 💰 Final Amount: ₹{A:,.2f}")
    st.markdown(f"### 🧮 Interest Earned: ₹{CI:,.2f}")

    # 📈 Generate Growth Data
    time_range = list(range(0, int(T)+1))
    growth = [P * (1 + R/(100*n))**(n*t) for t in time_range]

    # 📊 Plot
    fig, ax = plt.subplots()
    ax.plot(time_range, growth, marker='o', color='green')
    ax.set_title("📊 Compound Interest Growth Over Time")
    ax.set_xlabel("Years")
    ax.set_ylabel("Amount (₹)")
    ax.grid(True)

    st.pyplot(fig)

else:
    st.info("👆 Enter all values to see the result")
