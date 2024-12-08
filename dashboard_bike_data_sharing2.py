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
# Ensure these CSV files exist in the working directory
pertanyaan_1 = pd.read_csv("grpd_day_bike_data.csv")  # Dataset for seasonal and weather analysis
pertanyaan_2 = pd.read_csv("grpd_hour_bike_data.csv")    # Dataset for weekday analysis

# Tabs for visualization
tab1, tab2 = st.tabs(["Season and Weather Analysis", "Weekday Analysis"])

# **Tab 1: Season and Weather Analysis**
with tab1:
    st.subheader("Number of Bikes Rented by Season and Weather Situation")

    # Creating the plot
    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.barplot(x='season_', y='cnt_sum', hue='weathersit_', data=pertanyaan_1, palette='Set2', ax=ax1)
    ax1.set_title("Number of Bikes Rented by Season and Weather Situation", fontsize=14)
    ax1.set_xlabel("Season", fontsize=12)
    ax1.set_ylabel("Number of Bikes Rented", fontsize=12)
    ax1.set_xticks([0, 1, 2, 3])
    ax1.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'], rotation=0)

    # Adjusting legend
    handles, labels = ax1.get_legend_handles_labels()
    new_labels = ['Clear', 'Mist/Cloudy', 'Light Rain/Snow', 'Heavy Rain/Snow']
    ax1.legend(handles=handles, labels=new_labels, title='Weather Situation', loc='upper right')

    # Display the plot
    st.pyplot(fig1)

# **Tab 2: Weekday Analysis**
with tab2:
    st.subheader("Number of Bikes Rented by Day of the Week")

    # Creating the plot
    fig2, ax2 = plt.subplots(figsize=(12, 7))
    sns.barplot(x='w_e_e_k_d_a_y', y='c_n_t', data=pertanyaan_2, palette='Set2', ax=ax2)
    ax2.set_title("Number of Bikes Rented by Day of the Week", fontsize=14)
    ax2.set_xlabel("Day of the Week", fontsize=12)
    ax2.set_ylabel("Number of Bikes Rented", fontsize=12)
    ax2.set_xticks([0, 1, 2, 3, 4, 5, 6])
    ax2.set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], rotation=0)

    # Display the plot
    st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("**Created using Streamlit by Risdasih Agustin**")
