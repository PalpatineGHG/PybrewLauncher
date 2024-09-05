
# World of Warships Ship Mastery (Uncompiled)

## Überblick

Dies ist ein Python-Programm, das eine Benutzeroberfläche für die Verwaltung von Schiffsmeisterschaften im Spiel "World of Warships" bietet. Das Programm ermöglicht es Benutzern, ihre Schiffe zu bewerten und den Fortschritt zu verfolgen.

## Funktionen

- **Anmeldung und Registrierung:** Benutzer können sich anmelden oder registrieren.
- **Schiffsbewertung:** Benutzer können ihre Schiffe als "Nicht gekauft", "Schlecht", "Mittel" oder "Gut" bewerten.
- **Speichern der Daten:** Die Daten werden in einer JSON-Datei gespeichert.
- **Benutzerverwaltung:** Administratoren können Benutzer hinzufügen, löschen und anzeigen.

## Ordnerstruktur

Die Projektstruktur sieht wie folgt aus:

```
.
├── src
│   └── data
│       └── config_files
│           ├── user_config
│           │   └── users.json
│           └── config.json
├── main.py
└── requirements.txt
```

- `src/data/config_files/user_config/users.json`: Speichert die Benutzerinformationen.
- `src/data/config_files/config.json`: Standardkonfigurationsdatei für neue Benutzer.
- `main.py`: Der Hauptcode des Programms.
- `requirements.txt`: Abhängigkeiten des Projekts.

## Installation und Ausführung

### Voraussetzungen

- Python 3.x
- PyQt5

### Installation der Abhängigkeiten

Führen Sie den folgenden Befehl aus, um die benötigten Abhängigkeiten zu installieren:

```bash
pip install -r requirements.txt
```

### Starten des Programms

Um das Programm zu starten, führen Sie den folgenden Befehl aus:

```bash
python main.py
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der `LICENCE`-Datei.
