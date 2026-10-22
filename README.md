# 🔁 Projekt churn-prediction - Churn-Analyse für SaaS-Kunden

Dieses Projekt zeigt eine explorative Analyse eines simulierten Kunden-Datensatzes mit dem Ziel, **Kündigungsverhalten (Churn)** besser zu verstehen.

## 🎯 Zielsetzung

Ziel ist es, **mögliche Muster und Einflussfaktoren** zu erkennen, die zur Kündigung von Kunden führen.  
Das Projekt simuliert eine reale Fragestellung aus der **SaaS-Branche**, z. B. für Online-Tools, Memberships oder Software-Abos.

## 📊 Daten

Der Datensatz ist synthetisch generiert (nicht vertraulich) und enthält folgende Felder:

- `customer_id`: Eindeutige Kunden-ID
- `tenure_months`: Bisherige Kundendauer in Monaten
- `monthly_charges`: Monatliche Gebühren
- `contract_type`: Vertragstyp
- `Gender`: Geschlecht
- `churn`: Kündigungsstatus (1 = gekündigt, 0 = nicht gekündigt)

Für die logistische Regression werden tenure_months, monthly_charges und contract_type als Eingangsmerkmale verwendet. 
Die Kunden-ID und gender werden nicht als Modellmerkmale berücksichtigt.

### 📊 Visuelle Auswertungen

| Visualisierung | Beschreibung |
|----------------|--------------|
| `bar_churn_by_contract.png` | Vergleich der beobachteten Churn-Raten nach Vertragsart |
| `boxplot_tenure_by_churn.png` | Vergleich der bisherigen Kundendauer zwischen Kunden mit und ohne Kündigung |
| `hist_monthly_charges.png` | Verteilung der monatlichen Gebühren im Datensatz |

Die Visualisierungen dienen der explorativen Datenanalyse. Beobachtete Zusammenhänge erlauben keine unmittelbaren Rückschlüsse auf kausale Ursachen.

## 🔍 Erste Erkenntnisse

- Der Datensatz enthält 500 simulierte Kunden. Davon haben 27,4 % gekündigt.
- Bei Kunden mit `Month-to-Month`-Verträgen liegt die beobachtete Churn-Rate bei etwas über 30 %.
- Die bisherige Kundendauer (`tenure_months`), die monatlichen Gebühren (`monthly_charges`) und die Vertragsart (`contract_type`) wurden als mögliche Merkmale für die Churn-Vorhersage ausgewählt.
- Aus den bisherigen Ergebnissen lassen sich keine kausalen Ursachen für Kundenkündigungen ableiten.

Die Aussagekraft der einzelnen Merkmale und ihre Zusammenhänge mit dem Kündigungsverhalten müssen weiter untersucht werden.

## 🤖 Modellbewertung – Logistische Regression

Zur Vorhersage von Kundenkündigungen wurde eine logistische Regression eingesetzt. Der Datensatz wurde in 80 % Trainingsdaten (400 Kunden) und 20 % Testdaten (100 Kunden) aufgeteilt.

### Standard-Schwellenwert: 50 %

- Accuracy: 73 %
- Recall für Churn = 1: 0 %
- Richtig erkannte Kündiger: 0 von 27
- Übersehene Kündiger: 27 von 27

Obwohl das Modell eine Accuracy von 73 % erreicht, erkennt es keinen einzigen tatsächlichen Kündiger. Für das Geschäftsziel der frühzeitigen Churn-Erkennung ist diese Vorhersageleistung nicht ausreichend.

### Experimenteller Schwellenwert: 30 %

- Accuracy: 58 %
- Precision für Churn = 1: 24 %
- Recall für Churn = 1: 26 %
- Richtig erkannte Kündiger: 7 von 27
- Falsche Alarme: 22

Durch die Senkung des Schwellenwerts werden erstmals Kündiger erkannt. Gleichzeitig entstehen zusätzliche Fehlalarme, und die Accuracy sinkt.

### Interpretation und Limitationen

Die Ergebnisse zeigen, dass eine hohe Accuracy allein kein ausreichendes Qualitätskriterium für ein Churn-Modell ist.

Der Schwellenwert von 30 % wurde ausschließlich experimentell auf den Testdaten untersucht und ist kein unabhängig validiertes Optimum.

Die simulierten Daten könnten nur schwache Zusammenhänge zwischen den verfügbaren Merkmalen und dem Kündigungsverhalten enthalten. Vor einem produktiven Einsatz wären weitere Merkmalsanalysen und eine unabhängige Validierung erforderlich.

## 💼 Geschäftlicher Mehrwert und mögliche Anwendungen

Das Projekt demonstriert, wie Unternehmen Kundendaten analysieren können, um mögliche Zusammenhänge mit Kundenkündigungen zu untersuchen.

- **Kundensegmentierung:** Vergleich der Churn-Raten zwischen verschiedenen Vertragsarten.
- **Analyse möglicher Risikofaktoren:** Untersuchung der Kundendauer und monatlichen Gebühren im Zusammenhang mit Kündigungen.
- **Modellbewertung:** Vergleich unterschiedlicher Entscheidungsschwellenwerte und ihrer Auswirkungen auf die Erkennung von Kündigern.
- **Grundlage für Weiterentwicklungen:** Prüfung zusätzlicher Merkmale und Validierung des Modells, bevor konkrete Kundenbindungsmaßnahmen abgeleitet werden.

**Aktuelle Einschränkung:** Das entwickelte Modell ist ein analytischer Prototyp und noch nicht für den produktiven Einsatz als Churn-Frühwarnsystem geeignet.

## 🛠️ Technologien

- Python 3
- Pandas für Datenanalyse
- Matplotlib/Seaborn für Visualisierung (optional)
- Simulierter CSV-Datensatz

## 📁 Struktur

```text
.
├── .gitignore
├── LICENSE
├── README.md
├── churn_analysis.py
├── requirements.txt
├── bar_churn_by_contract.png
├── boxplot_tenure_by_churn.png
├── hist_monthly_charges.png
├── boxplot_usage_by_churn.png
├── hist_last_login.png
├── churn_by_contract.png
└── notebooks/
    └── exploration.ipynb
```

Die aktuelle Analyse verwendet die Grafiken `bar_churn_by_contract.png`, `boxplot_tenure_by_churn.png` und `hist_monthly_charges.png`.

Die übrigen PNG-Dateien stammen aus früheren Projektständen und werden vom aktuellen Analyseskript nicht erzeugt.

---

🚀 Dieses Projekt ist Teil meines Data-Science-Portfolios und dient zur Demonstration typischer Fragestellungen im Bereich **Kundenbindung & Business Analytics**.

📂 Datenbasis  
Die verwendeten Daten sind simuliert (keine echten Kundendaten).  
Sie dienen ausschließlich Demonstrations- und Lernzwecken.  
