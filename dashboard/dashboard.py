import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


# Load data
file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")
try:
    df = pd.read_csv(file_path)
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['year'] = df['order_purchase_timestamp'].dt.year
    df['month'] = df['order_purchase_timestamp'].dt.month
except Exception as e:
    st.warning("Data tidak ditemukan atau gagal dimuat.")
    df = pd.DataFrame()

# Title
st.title("Dashboard Analisis Penjualan")

if not df.empty:
    try:
        # Filter untuk produk paling banyak dibeli
        year_selected_product = st.sidebar.selectbox("Pilih Tahun (Produk)", sorted(df['year'].unique(), reverse=True), key="year_product")
        month_selected_product = st.sidebar.selectbox("Pilih Bulan (Produk)", sorted(df['month'].unique()), key="month_product")
        df_filtered_product = df[(df['year'] == year_selected_product) & (df['month'] == month_selected_product)]

        # Produk paling banyak dibeli
        if not df_filtered_product.empty:
            product_counts = df_filtered_product['product_category_name'].value_counts().head(10)
            top_product = product_counts.idxmax()
            st.subheader(f"Top 10 Produk Paling Banyak Dibeli pada {month_selected_product}-{year_selected_product}")
            fig, ax = plt.subplots()
            product_counts.plot(kind='bar', ax=ax, color='skyblue')
            ax.set_ylabel("Jumlah Pembelian")
            st.pyplot(fig)
            st.write(f"Produk terlaris pada {month_selected_product}-{year_selected_product} adalah **{top_product}** dengan jumlah pembelian tertinggi.")
        else:
            st.warning(f"Tidak ada data untuk produk pada {month_selected_product}-{year_selected_product}.")
    except Exception as e:
        st.warning("Terjadi kesalahan saat menampilkan data produk.")
    
    try:
        # Filter untuk metode pembayaran
        year_selected_payment = st.sidebar.selectbox("Pilih Tahun (Pembayaran)", sorted(df['year'].unique(), reverse=True), key="year_payment")
        month_selected_payment = st.sidebar.selectbox("Pilih Bulan (Pembayaran)", sorted(df['month'].unique()), key="month_payment")
        df_filtered_payment = df[(df['year'] == year_selected_payment) & (df['month'] == month_selected_payment)]

        # Metode pembayaran paling sering digunakan
        if not df_filtered_payment.empty:
            payment_counts = df_filtered_payment['payment_type'].value_counts()
            top_payment = payment_counts.idxmax()
            st.subheader(f"Metode Pembayaran yang Paling Sering Digunakan pada {month_selected_payment}-{year_selected_payment}")
            fig, ax = plt.subplots()
            payment_counts.plot(kind='bar', ax=ax, color='lightcoral')
            ax.set_ylabel("Jumlah Penggunaan")
            st.pyplot(fig)
            st.write(f"Metode pembayaran yang paling sering digunakan pada {month_selected_payment}-{year_selected_payment} adalah **{top_payment}**.")
        else:
            st.warning(f"Tidak ada data untuk metode pembayaran pada {month_selected_payment}-{year_selected_payment}.")
    except Exception as e:
        st.warning("Terjadi kesalahan saat menampilkan data pembayaran.")
else:
    st.warning("Data tidak tersedia.")
