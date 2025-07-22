import pandas as pd

# Datenquelle
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(url)

# Basisinfos
print("\nSpalten im Datensatz:")
print(df.columns)
print("\n📊 Datenübersicht:")
print(df.shape)
print("\n🔎 Datentypen:")
print(df.dtypes)
print("\n🧼 Fehlende Werte:")
print(df.isnull().sum())

# Zielspalte Churn (nur wenn vorhanden)
if "Churn" in df.columns:
    print("\n🎯 Churn-Verteilung:")
    print(df["Churn"].value_counts(normalize=True))
else:
    print("\nℹ️ Keine 'Churn'-Spalte im Datensatz. (Kein Problem für generelle EDA)")


# Vorschau
print("\n👀 Datenvorschau:")
print(df.head())