import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Farbpalette für Visualisierungen
colors = {
    "churn_bar": "skyblue",
    "boxplot": "mediumseagreen",
    "histogram": "salmon"
}



# Datenquelle
df = pd.read_csv('/mnt/c/Users/Stefan/Downloads/simulated_churn_data.csv')

# Basisinfos
print("\nSpalten im Datensatz:")
print(df.columns)
print("\nDatenübersicht:")
print(df.shape)
print("\nDatentypen:")
print(df.dtypes)
print("\nFehlende Werte:")
print(df.isnull().sum())


# Zielspalte Churn (nur wenn vorhanden)
if "Churn" in df.columns:
    print("\nChurn-Verteilung:")
    print(df["Churn"].value_counts(normalize=True))
else:
    print("\nKeine 'Churn'-Spalte im Datensatz. (Kein Problem für generelle EDA)")


# Vorschau
pd.set_option("display.max_columns", None)
print("\nDatenvorschau:")
print(df.head())

# Gruppierte Churn-Rate nach Vertragstyp
churn_by_contract = df.groupby("ContractType")["Churn"].mean()

# Plot
plt.figure(figsize=(8, 5))
churn_by_contract.plot(kind="bar", color=colors["churn_bar"])
plt.title("Churn-Rate nach Vertragstyp", fontsize=14)
plt.ylabel("Durchschnittliche Churn-Rate")
plt.xlabel("Vertragstyp")
plt.xticks(rotation=0)
plt.grid(True, axis='y', linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("bar_churn_by_contract.png")
plt.clf()

# Boxplot für UsageHours
plt.figure(figsize=(8, 5))
sns.boxplot(x="Churn", y="UsageHours", data=df, palette=[colors["boxplot"], "lightgray"])
plt.title("Monatliche Nutzung nach Churn-Status")
plt.xlabel("Churn (0 = aktiv, 1 = gekündigt)")
plt.ylabel("Monatliche Nutzungsstunden")
plt.grid(True, axis='y', linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("boxplot_usage_by_churn.png")
plt.clf()

# Histogramm: Verteilung der Logins

plt.figure(figsize=(8, 5))
df["LastLogin"].hist(bins=20, color=colors["histogram"], edgecolor="black")
plt.title("Verteilung: Tage seit letztem Login", fontsize=14)
plt.xlabel("Tage seit letztem Login")
plt.ylabel("Anzahl der Kunden")
plt.grid(True, axis='y', linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("hist_last_login.png")
plt.clf()

# --- Feature Engineering & Datenvorbereitung für Modellierung ---

# One-Hot-Encoding für kategoriale Variablen
df_encoded = pd.get_dummies(df, columns=["ContractType", "PaymentMethod"], drop_first=True)

# Features und Ziel definieren
X = df_encoded.drop(["CustomerID", "Churn"], axis=1)
y = df_encoded["Churn"]

# Numerische Features skalieren
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test-Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Modell initialisieren und trainieren
model = LogisticRegression()
model.fit(X_train, y_train)

# Vorhersage treffen
y_pred = model.predict(X_test)

# Ergebnisse anzeigen
print("\n🔍 Modellbewertung:")
print(f"Genauigkeit: {accuracy_score(y_test, y_pred):.2f}")
print("\nKonfusionsmatrix:")
print(confusion_matrix(y_test, y_pred))
print("\nKlassifikationsbericht:")
print(classification_report(y_test, y_pred))
