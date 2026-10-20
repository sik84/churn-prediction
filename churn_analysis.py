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
if "churn" in df.columns:
    print("\nChurn-Verteilung:")
    print(df["churn"].value_counts(normalize=True))
else:
    print("\nKeine 'churn'-Spalte im Datensatz. (Kein Problem für generelle EDA)")


# Vorschau
pd.set_option("display.max_columns", None)
print("\nDatenvorschau:")
print(df.head())

# Gruppierte Churn-Rate nach Vertragstyp
churn_by_contract = df.groupby("contract_type")["churn"].mean()

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

# Boxplot: Kundendauer nach Churn-Status
plt.figure(figsize=(8, 5))
sns.boxplot(
    x="churn",
    y="tenure_months",
    data=df,
    color=colors["boxplot"]
)
plt.title("Kundendauer nach Churn-Status")
plt.xlabel("Churn (0 = geblieben, 1 = gekündigt)")
plt.ylabel("Bisherige Kundendauer (Monate)")
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("boxplot_tenure_by_churn.png")
plt.clf()

# Histogramm: Verteilung der monatlichen Gebühren
plt.figure(figsize=(8, 5))
df["monthly_charges"].hist(
    bins=20,
    color=colors["histogram"],
    edgecolor="black"
)
plt.title("Verteilung der monatlichen Gebühren", fontsize=14)
plt.xlabel("Monatliche Gebühren")
plt.ylabel("Anzahl der Kunden")
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("hist_monthly_charges.png")
plt.clf()

# --- Feature Engineering & Datenvorbereitung für Modellierung ---

# One-Hot-Encoding für kategoriale Variablen
df_encoded = pd.get_dummies(
    df,
    columns=["contract_type"],
    drop_first=True,
    dtype=int
)

# Features und Ziel definieren
X = df_encoded.drop(
    columns=["customer_id", "churn", "gender"]
)
y = df_encoded["churn"]

# Train-Test-Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Numerische Features skalieren
scaler = StandardScaler()

numeric_features = ["tenure_months", "monthly_charges"]

X_train = X_train.copy()
X_test = X_test.copy()

X_train[numeric_features] = scaler.fit_transform(
    X_train[numeric_features]
)

X_test[numeric_features] = scaler.transform(
    X_test[numeric_features]
)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Modell initialisieren und trainieren
model = LogisticRegression()
model.fit(X_train, y_train)

# Vorhersage treffen
y_pred = model.predict(X_test)

y_proba = model.predict_proba(X_test)[:, 1]
print("Kündigungswahrscheinlichkeiten (erste 10):", y_proba[:10])

# Experiment: niedrigerer Schwellenwert
y_pred_30 = (y_proba >= 0.30).astype(int)

print("\nConfusion Matrix bei 30 %:")
print(confusion_matrix(y_test, y_pred_30))

print("\nClassification Report bei 30 %:")
print(classification_report(y_test, y_pred_30, zero_division=0))

# Ergebnisse anzeigen
print("\n🔍 Modellbewertung:")
print(f"Genauigkeit: {accuracy_score(y_test, y_pred):.2f}")
print("\nKonfusionsmatrix:")
print(confusion_matrix(y_test, y_pred))
print("\nKlassifikationsbericht:")
print(classification_report(y_test, y_pred, zero_division=0))
print("Minimum:", y_proba.min())
print("Maximum:", y_proba.max())
print("Durchschnitt:", y_proba.mean())