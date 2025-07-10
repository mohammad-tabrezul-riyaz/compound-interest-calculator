 import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Investment Calculator", page_icon="📈")
st.title("📈 Investment Calculator (Compound + SIP)")

# 🔹 User Inputs
st.header("💰 Investment Inputs")
P = st.number_input("🪙 One-Time Investment (₹)", min_value=0.0, format="%.2f")
sip = st.number_input("💸 Monthly SIP (₹)", min_value=0.0, format="%.2f")
R = st.number_input("📈 Annual Interest Rate (%)", min_value=0.0)
T = st.number_input("⏳ Time (in years)", min_value=0.0)
frequency = st.selectbox("🔁 Compounding Frequency", ["Annually", "Half-Yearly", "Quarterly", "Monthly", "Daily"])

# 🔁 Frequency Mapping
freq_map = {
    "Annually": 1,
    "Half-Yearly": 2,
    "Quarterly": 4,
    "Monthly": 12,
    "Daily": 365
}
n = freq_map[frequency]
monthly_rate = R / (12 * 100)

# ✅ Run Calculation
if R > 0 and T > 0 and (P > 0 or sip > 0):
    # One-Time Investment
    A_lump = P * (1 + R/(100*n))**(n*T)

    # SIP Calculation
    total_months = int(T * 12)
    A_sip = sip * (((1 + monthly_rate) ** total_months - 1) / monthly_rate) * (1 + monthly_rate)

    # Totals
    total_invested = P + sip * total_months
    total_final = A_lump + A_sip
    total_interest = total_final - total_invested

    # 💬 Display Results
    st.markdown(f"### 💼 Final Value: ₹{total_final:,.2f}")
    st.markdown(f"### 💸 Total Invested: ₹{total_invested:,.2f}")
    st.markdown(f"### 💰 Interest Earned: ₹{total_interest:,.2f}")

    # 📊 Yearly Growth Graph
    years = list(range(0, int(T)+1))
    lump_values = [P * (1 + R/(100*n))**(n*y) for y in years]
    sip_values = [
        sip * (((1 + monthly_rate) ** (y * 12) - 1) / monthly_rate) * (1 + monthly_rate) for y in years
    ]
    combined_values = [l + s for l, s in zip(lump_values, sip_values)]

    # 📈 Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, lump_values, label="📦 One-Time", color='green', linewidth=2, marker='o')
    ax.plot(years, sip_values, label="💸 Monthly SIP", color='blue', linewidth=2, marker='s')
    ax.plot(years, combined_values, label="📊 Total Growth", color='black', linestyle='--', linewidth=2)

    ax.set_title("Investment Growth Over Time", fontsize=14)
    ax.set_xlabel("Years")
    ax.set_ylabel("Amount (₹)")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()
    st.pyplot(fig)

else:
    st.info("👆 Enter valid inputs to calculate and visualize your investment growth.")
       
 
