import streamlit as st
from utils.data_fetcher import fetch_okx_data
from strategies.hma_strategy import generate_signals
from utils.notifier import send_wechat
import pandas as pd

def main():
    # 获取数据
    df = fetch_okx_data()
    
    # 生成信号
    signals = generate_signals(df)
    
    # 展示信号
    st.title("加密货币交易信号")
    st.write("最新K线数据：")
    st.line_chart(df['close'])
    
    # 发送通知
    if signals:
        latest_signal = signals[-1]
        msg = f"交易信号: {latest_signal[0]} 价格: {latest_signal[1]}"
        send_wechat(msg)
        st.success(f"已发送微信通知: {msg}")

if __name__ == "__main__":
    main()