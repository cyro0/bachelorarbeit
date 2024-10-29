import pandas as pd
import altair as alt

# Daten erstellen (basierend auf der Beschreibung und dem Bild)
data = pd.DataFrame({
    'Modell/Datensatz': [
        'Toxicchat Training', 
        'jackhhao/jailbreak-classification', 
        'deepset-prompt-injection', 
        'xTRam1/safe-guard-prompt-injection', 
        'deepset-prompt-injection mit ~10% der Gesamtparameter',
        'ShieldGemma 27B',
        'LlamaGuard2 7B'
    ],
    'Toxicchat': [
        '0.99/0.82', 
        '0.89/0.49', 
        '0.59/0.50', 
        '0.93/0.51', 
        '0.59/0.50', 
        '0.73/0.81', 
        '0.62/0.63'
    ],
    'jackhhao/jailbreak-classification': [
        '0.87/0.95', 
        '0.98/0.99', 
        '0.38/0.77', 
        '0.85/0.89', 
        '0.39/0.77', 
        '-', 
        '-'
    ],
    'deepset-prompt-injection': [
        '0.31/0.76', 
        '0.45/0.79', 
        '0.97/0.99', 
        '0.59/0.79', 
        '0.97/0.98', 
        '-', 
        '-'
    ],
    'xTRam1/safe-guard-prompt-injection': [
        '0.66/0.70', 
        '0.83/0.80', 
        '0.40/0.68', 
        '0.99/0.99', 
        '0.41/0.66',
        '-', 
        '-'
    ]
})

# Die Metriken aus den kombinierten Strings extrahieren
for col in data.columns[1:]:
    data[col] = data[col].astype(str).str.split('/', expand=True)
    data[col + ' F1'] = pd.to_numeric(data[col][0])
    data[col + ' AUPRC'] = pd.to_numeric(data[col][1])
    data = data.drop(columns=[col])

# Daten umformen für Altair
data_melted = data.melt('Modell/Datensatz', var_name='Datensatz und Metrik', value_name='Wert')
data_melted[['Datensatz', 'Metrik']] = data_melted['Datensatz und Metrik'].str.split(' ', expand=True)

# Balkendiagramm erstellen
chart = alt.Chart(data_melted).mark_bar().encode(
    x=alt.X('Modell/Datensatz:N', title='Modell/Datensatz'),
    y=alt.Y('Wert:Q', title='Wert'),
    color='Metrik:N',
    column=alt.Column('Datensatz:N', title='Evaluierungsdatensatz'),
    tooltip=['Modell/Datensatz', 'Datensatz', 'Metrik', 'Wert']
).properties(
    title='Vergleich von F1-Score und AUPRC'
).interactive()

chart.save('f1_auprc_vergleich_balkendiagramm.html')