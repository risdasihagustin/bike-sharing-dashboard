import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit Dashboard Title
st.title("Bike Rental Analysis Dashboard")
st.markdown("""
This dashboard presents two analyses:
1. **Number of Bikes Rented by Season and Weather Situation**
2. **Number of Bikes Rented by Day of the Week**
""")

# Reading the datasets
# Pastikan file CSV berada di direktori kerja
pertanyaan_1 = pd.read_csv("day_df.csv")  # Dataset untuk seasonal dan weather analysis
pertanyaan_2 = pd.read_csv("hour_df.csv")  # Dataset untuk weekday analysis

# Konversi kolom kategori menjadi tipe string atau kategori
pertanyaan_1['season_'] = pertanyaan_1['season_'].astype(str)
pertanyaan_1['weathersit_'] = pertanyaan_1['weathersit_'].astype(str)
pertanyaan_2['w_e_e_k_d_a_y'] = pertanyaan_2['w_e_e_k_d_a_y'].astype(str)

# Mapping kategori menjadi lebih deskriptif
season_mapping = {"1": "Spring", "2": "Summer", "3": "Fall", "4": "Winter"}
pertanyaan_1['season_'] = pertanyaan_1['season_'].map(season_mapping)

weather_mapping = {
    "1": "Clear",
    "2": "Mist/Cloudy",
    "3": "Light Rain/Snow",
    "4": "Heavy Rain/Snow"
}
pertanyaan_1['weathersit_'] = pertanyaan_1['weathersit_'].map(weather_mapping)

weekday_mapping = {
    "0": "Monday",
    "1": "Tuesday",
    "2": "Wednesday",
    "3": "Thursday",
    "4": "Friday",
    "5": "Saturday",
    "6": "Sunday"
}
pertanyaan_2['w_e_e_k_d_a_y'] = pertanyaan_2['w_e_e_k_d_a_y'].map(weekday_mapping)

# Tabs untuk visualisasi
tab1, tab2 = st.tabs(["Season and Weather Analysis", "Weekday Analysis"])

# **Tab 1: Season and Weather Analysis**
with tab1:
    st.subheader("Number of Bikes Rented by Season and Weather Situation")
    
    # Dropdown untuk memilih musim
    selected_season = st.selectbox("Select Season:", options=["All"] + pertanyaan_1['season_'].unique().tolist())
    filtered_data_1 = (
        pertanyaan_1 if selected_season == "All" else pertanyaan_1[pertanyaan_1['season_'] == selected_season]
    )

    # Validasi data
    if filtered_data_1.empty:
        st.warning("No data available for the selected season.")
    else:
        # Plot data
        fig1, ax1 = plt.subplots(figsize=(12, 7))
        sns.barplot(
            x='season_', y='cnt_sum', hue='weathersit_', data=filtered_data_1, palette='Set2', ax=ax1
        )
        ax1.set_title("Number of Bikes Rented by Season and Weather Situation", fontsize=14)
        ax1.set_xlabel("Season", fontsize=12)
        ax1.set_ylabel("Number of Bikes Rented", fontsize=12)
        ax1.legend(title='Weather Situation', loc='upper right')
        st.pyplot(fig1)

# **Tab 2: Weekday Analysis**
with tab2:
    st.subheader("Number of Bikes Rented by Day of the Week")
    
    # Multiselect untuk memilih hari
    selected_days = st.multiselect(
        "Select Days of the Week:",
        options=pertanyaan_2['w_e_e_k_d_a_y'].unique(),
        default=pertanyaan_2['w_e_e_k_d_a_y'].unique()
    )
    filtered_data_2 = pertanyaan_2[pertanyaan_2['w_e_e_k_d_a_y'].isin(selected_days)]

    # Validasi data
    if filtered_data_2.empty:
        st.warning("No data available for the selected days.")
    else:
        # Plot data
        fig2, ax2 = plt.subplots(figsize=(12, 7))
        sns.barplot(
            x='w_e_e_k_d_a_y', y='c_n_t', data=filtered_data_2, palette='Set2', ax=ax2
        )
        ax2.set_title("Number of Bikes Rented by Day of the Week", fontsize=14)
        ax2.set_xlabel("Day of the Week", fontsize=12)
        ax2.set_ylabel("Number of Bikes Rented", fontsize=12)
        st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("**Created using Streamlit**")
