
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv('CO2_BILAN_restructured.csv')

# Titre de l'application
st.title('Visualisation des émissions de CO2 par véhicule')

# Filtrage par norme EURO
euro_norms = data['Norme EURO'].unique()
selected_norm = st.selectbox('Sélectionnez la norme EURO', euro_norms)

filtered_data = data[data['Norme EURO'] == selected_norm]

# Affichage des données filtrées
st.write('Données filtrées :')
st.dataframe(filtered_data)

# Graphique des émissions par mois
fig, ax = plt.subplots()
for vehicle in filtered_data['Véhicule'].unique():
    vehicle_data = filtered_data[filtered_data['Véhicule'] == vehicle]
    ax.plot(vehicle_data['Mois'], vehicle_data['Émissions CO2 (kg)'], label=vehicle)

ax.set_xlabel('Mois')
ax.set_ylabel('Émissions CO2 (kg)')
ax.set_title('Émissions de CO2 par mois')
ax.legend()

st.pyplot(fig)
