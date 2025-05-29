import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = '/Users/muhammadzuamaalamin/Documents/labbelajar2new/streamlite/project1/Hospital_Indonesia_datasets.csv'
st.title("Dashboard data rumah sakit Indonesia")
data = pd.read_csv(path,delimiter=';')

# Sidebar sebagai navigasi halaman
menu = st.sidebar.selectbox(
    "Pilih Halaman",
    ["General", "Cek Data Provinsi", "Cek Data Kabupaten", "Kesimpulan Data"]
)

# Halaman Beranda
if menu == "General":
    st.write("Ini adalah halaman utama.")
    st.write("📊 data rumah sakit")
    st.dataframe(data)
    st.write("📊 deskripsi Data")
    st.write(data.describe())
    st.write("📊 informasi Data")
    st.write(data.info())

     #statistik
    st.write("📊 Statistik Data")
    # Create a bar chart to show the number of hospitals in the selected province
    x = data['propinsi'].value_counts().index
    y = data['propinsi'].value_counts().values

    fig, ax = plt.subplots()
    ax.bar(x, y, color='blue')
    ax.set_title(f"sebaran Rumah Sakit di Provinsi Indonesia")
    ax.set_xlabel("propinsi")
    ax.set_ylabel("Jumlah Rumah Sakit")
    plt.xticks(rotation=45)

    st.pyplot(fig)

    ranking_data = pd.DataFrame({
            "Provinsi": data['propinsi'].value_counts().index,
            "Jumlah Rumah Sakit": data['propinsi'].value_counts().values
    }).reset_index(drop=True)
        
        # Tampilkan DataFrame peringkat
    st.dataframe(ranking_data)

        # Pie chart for ownership distribution
    st.write("📊 Distribusi Kepemilikan Rumah Sakit")

    ownership_counts = data['kepemilikan'].value_counts()
    labels = ownership_counts.index
    sizes = ownership_counts.values
    st.dataframe({"Jenis Kepemilikan": labels, "Jumlah": sizes})


# Halaman Biodata
elif menu == "Cek Data Provinsi":
    st.title("Halaman Cek Data Provinsi")
    prov = st.selectbox("Pilih Provinsi", data['propinsi'].unique())

    # Filter data berdasarkan provinsi yang dipilih
    filtered_data = data[data['propinsi'] == prov]
    jumlah  = filtered_data['id'].count()
    # Tampilkan hasil
    st.write(f" Jumlah Data rumah sakit di Provinsi {prov}: {jumlah}")
    st.dataframe(filtered_data)

    # Pie chart for ownership distribution
    st.write(f"📊 Distribusi Kelas Rumah Sakit Provinsi {prov}")
    new_data = data[data['propinsi'] == prov]
    kelas_count = new_data['kelas'].value_counts()
    labels = kelas_count.index
    sizes = kelas_count.values

    # Pie chart for class distribution
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(f"Distribusi Kelas Rumah Sakit di Provinsi {prov}")
    st.pyplot(fig)

    # Display data in tabular format
    st.dataframe({"Kelas Rumah Sakit": labels, "Jumlah": sizes})

# Halaman Biodata
elif menu == "Cek Data Kabupaten":
    kab = st.selectbox("Pilih Kabupaten/Kota ", data['kab'].unique())

    # Filter data berdasarkan provinsi yang dipilih
    filtered_data = data[data['kab'] == kab]
    jumlah  = filtered_data['id'].count()
    # Tampilkan hasil
    st.write(f" Jumlah Data rumah sakit di Provinsi {kab}: {jumlah}")
    st.dataframe(filtered_data)

# Halaman Data Rumah Sakit
elif menu == "Kesimpulan Data":
    st.title("Halaman Data Rumah Sakit")
    # Asumsikan kamu sudah punya DataFrame `data`
    # Misal: data = pd.read_csv('data_rs.csv')
    import pandas as pd
    data = pd.DataFrame({
        'nama_rs': ['RS A', 'RS B', 'RS C'],
        'propinsi': ['Jawa Timur', 'Jawa Barat', 'Jawa Timur']
    })

    prov = st.selectbox("Pilih Provinsi", data['propinsi'].unique())
    filtered = data[data['propinsi'] == prov]
    st.dataframe(filtered)
