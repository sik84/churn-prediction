# 🔁 Projekt churn-prediction - Churn-Analyse für SaaS-Kunden

Dieses Projekt zeigt eine explorative Analyse eines simulierten Kunden-Datensatzes mit dem Ziel, **Kündigungsverhalten (Churn)** besser zu verstehen.

## 🎯 Zielsetzung

Ziel ist es, **mögliche Muster und Einflussfaktoren** zu erkennen, die zur Kündigung von Kunden führen.  
Das Projekt simuliert eine reale Fragestellung aus der **SaaS-Branche**, z. B. für Online-Tools, Memberships oder Software-Abos.

## 📊 Daten

Der Datensatz ist synthetisch generiert (nicht vertraulich) und enthält folgende Felder:

- `CustomerID`: Eindeutige ID
- `ContractType`: Monatlich, Jährlich, Zwei-Jahresvertrag
- `UsageHours`: Durchschnittliche Nutzungszeit pro Monat
- `LastLogin`: Tage seit letztem Login
- `SupportTickets`: Anzahl erstellter Tickets
- `PaymentMethod`: Zahlungsmethode
- `Churn`: 1 = gekündigt, 0 = aktiv

### 📊 Visuelle Auswertungen (→ im Projekt-Ordner gespeichert)

| Plot | Aussage |
|------|---------|
| `bar_churn_by_contract.png` | Kündigungsrate nach Vertragstyp – Monatstarife deutlich höher |
| `boxplot_usage_by_churn.png` | Gekündigte Kunden nutzen den Service tendenziell weniger |
| `hist_last_login.png` | Häufung bei Kunden, die sich lange nicht eingeloggt haben |

## 🔍 Erste Erkenntnisse

- Kunden mit **Monatsverträgen** zeigen eine deutlich höhere Kündigungsrate.
- **Jahres- und Zwei-Jahres-Verträge** haben eine signifikant geringere Churn-Rate.- **Kreditkartenzahlung** ist mit einer niedrigeren Kündigungsquote verbunden.
- Kunden, die nicht gekündigt haben (Churn = 0), zeigen tendenziell eine höhere und stabilere Nutzung pro Monat.

## 🔍 Konkrete Mehrwerte:

- Frühwarnsystem für Kündigungsrisiken → Der analysierte Zusammenhang zwischen Vertragstyp & Churn zeigt, wo gezielte Maßnahmen lohnen.

- Nutzungsbasierte Segmentierung → Boxplot-Analyse offenbart Nutzungsverhalten aktiver vs. gekündigter Kunden.

- Verhaltensbasierte Interventionspunkte → Login-Histogramm liefert Hinweise für Inaktivität und ermöglicht gezielte Re-Engagement-Kampagnen.

- Modellbasierte Vorhersage von Kündigungen (Logistische Regression) → Unternehmen können zukünftige Churns antizipieren und Präventivmaßnahmen einleiten.

## 🛠️ Technologien

- Python 3
- Pandas für Datenanalyse
- Matplotlib/Seaborn für Visualisierung (optional)
- Simulierter CSV-Datensatz

## 📁 Struktur

.
├── LICENSE
├── README.md
├── bar_churn_by_contract.png
├── boxplot_usage_by_churn.png
├── churn_analysis.py
├── churn_by_contract.png
├── data
├── hist_last_login.png
├── notebooks
│   └── exploration.ipynb
└── requirements.txt


---

🚀 Dieses Projekt ist Teil meines Data-Science-Portfolios und dient zur Demonstration typischer Fragestellungen im Bereich **Kundenbindung & Business Analytics**.
