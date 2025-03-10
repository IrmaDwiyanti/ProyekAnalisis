import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

<<<<<<< HEAD
# Load data
file_path = "main_data.csv"
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
=======
# Load data dari CSV
file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")
data = pd.read_csv(file_path)

# Pastikan kolom yang diperlukan ada dalam dataset
expected_columns = {"Kategori Produk", "Jumlah Pembelian", "Metode Pembayaran", "Jumlah Transaksi", "Kota", "Jumlah Pelanggan", "Provinsi"}
if not expected_columns.issubset(data.columns):
    st.error("Dataset tidak memiliki semua kolom yang diperlukan.")
    st.stop()

# Judul Dashboard
st.title('Dashboard Penjualan dan Pelanggan')

# Menampilkan data utama dalam bentuk tabel
st.subheader('Data Kategori Produk, Metode Pembayaran, Kota, dan Provinsi')
st.dataframe(data)

# Menambahkan filter pada sidebar untuk memilih metode pembayaran
st.sidebar.header("Filter Berdasarkan Metode Pembayaran")
metode_pembayaran = st.sidebar.selectbox("Pilih Metode Pembayaran", ["Semua"] + data["Metode Pembayaran"].dropna().unique().tolist())

# Mengambil data berdasarkan metode pembayaran yang dipilih
if metode_pembayaran != "Semua":
    data_filtered = data[data["Metode Pembayaran"] == metode_pembayaran]
else:
    data_filtered = data

# Menampilkan data yang telah difilter berdasarkan metode pembayaran
st.subheader(f'Filter Data dengan Metode Pembayaran: {metode_pembayaran}')
st.dataframe(data_filtered)

# Menampilkan statistik deskriptif
st.subheader('Statistik Deskriptif')
st.write(data_filtered.describe())

# Grafik Kategori Produk Berdasarkan Jumlah Pembelian
st.subheader('Grafik Kategori Produk Berdasarkan Jumlah Pembelian')
fig1, ax1 = plt.subplots()
sns.barplot(x='Kategori Produk', y='Jumlah Pembelian', data=data_filtered, ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
ax1.set_title('Kategori Produk Berdasarkan Jumlah Pembelian')
st.pyplot(fig1)

# Grafik Metode Pembayaran Berdasarkan Jumlah Transaksi
st.subheader('Grafik Metode Pembayaran Berdasarkan Jumlah Transaksi')
fig2, ax2 = plt.subplots()
sns.barplot(x='Metode Pembayaran', y='Jumlah Transaksi', data=data_filtered, ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
ax2.set_title('Metode Pembayaran Berdasarkan Jumlah Transaksi')
st.pyplot(fig2)

# Grafik Kota Berdasarkan Jumlah Pelanggan
st.subheader('Grafik Kota Berdasarkan Jumlah Pelanggan')
fig3, ax3 = plt.subplots()
sns.barplot(x='Kota', y='Jumlah Pelanggan', data=data_filtered, ax=ax3)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')
ax3.set_title('Kota Berdasarkan Jumlah Pelanggan')
st.pyplot(fig3)

# Grafik Provinsi Berdasarkan Jumlah Pelanggan
st.subheader('Grafik Provinsi Berdasarkan Jumlah Pelanggan')
fig4, ax4 = plt.subplots()
sns.barplot(x='Provinsi', y='Jumlah Pelanggan', data=data_filtered, ax=ax4)
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')
ax4.set_title('Provinsi Berdasarkan Jumlah Pelanggan')
st.pyplot(fig4)
>>>>>>> 38f6c0e5d3f684526fbf62cab6843cd685c29e8c
