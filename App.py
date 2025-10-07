# app.py (Test minimal — XAUUSD / BTC simple chart)
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import date

st.set_page_config(page_title="Test XAU/BTC", layout="wide")
st.title("Test — XAU/USD & BTC/USD Quick Chart")

symbol = st.selectbox("Pilih asset:", ["XAUUSD=X", "BTC-USD"])
start = st.date_input("Mulai dari", value=date(2020, 1, 1))
end = st.date_input("Sampai", value=date.today())

if st.button("Load data & Chart"):
    with st.spinner("Mengambil data..."):
        df = yf.download(symbol, start=start, end=end, progress=False)
    if df.empty:
        st.error("Gagal ambil data. Coba interval/periode lain atau upload CSV.")
    else:
        df = df.reset_index()
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name="price"))
        fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df.tail(5))
