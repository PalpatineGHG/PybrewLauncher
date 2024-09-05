
# Pybrew Launcher v0.1

Pybrew Launcher ist ein Python-basiertes GUI-Tool zum Verwalten und Starten von mehreren Python-Anwendungen. Es bietet eine einfache Benutzeroberfläche, die es dem Benutzer ermöglicht, verschiedene Anwendungen über Icons zu starten und eine Hintergrundmusik abzuspielen.

## Features
- Starten von Python-Anwendungen per Mausklick.
- Hintergrundmusik, die während der Verwendung des Launchers läuft.
- Hover-Effekt bei den Anwendungsicons.
- Zeitanzeige mit blinkendem Doppelpunkt.
- Launcher minimiert sich automatisch, wenn eine App gestartet wird und kehrt nach dem Schließen der App zurück.
- Läuft unter Python und nutzt Bibliotheken wie `Tkinter`, `PIL` und `Pygame`.

## Installation

### Voraussetzungen
Stelle sicher, dass die folgenden Python-Bibliotheken installiert sind:

- `pygame`
- `Pillow`
- `tkinter` (in den meisten Python-Installationen standardmäßig enthalten)

Du kannst die fehlenden Abhängigkeiten mit folgendem Befehl installieren:

```bash
pip install pygame Pillow
```

### Verzeichnisstruktur
Stelle sicher, dass die Verzeichnisstruktur nicht geändert wird und so bleibt wie sie ist.

## Ausführung

Um den Launcher zu starten, führe den folgenden Befehl im Terminal in diesem Pfad projectroot\src\scripts\main.py aus:

```bash
python main.py
```
Oder doppelklicke auf die main.py Datei.

### Features des Launchers

- **Hintergrundmusik abspielen:** Der Launcher startet eine Hintergrundmusik, die in einer Endlosschleife abgespielt wird.
- **App starten:** Klicke auf ein Icon, um eine Anwendung zu starten. Wenn eine App bereits läuft, zeigt der Launcher eine Meldung an, dass keine weiteren Apps gestartet werden können, bis die laufende App geschlossen ist.
- **Hover-Effekt:** Fahre mit der Maus über ein Icon, um den Helligkeitseffekt auszulösen.
- **Zeit-Anzeige:** Der Launcher zeigt die aktuelle Uhrzeit an und aktualisiert sie jede Sekunde mit einem blinkenden Doppelpunkt.

## Anpassungen

Falls du die Musik, Icons oder die Pfade zu den Anwendungen ändern möchtest, kannst du das in der Datei `pybrew_launcher.py` tun. Achte darauf, dass die Pfade korrekt relativ zu deinem Projektverzeichnis gesetzt sind.

## Bekannte Probleme

- **Musik-Wiedergabe:** Stelle sicher, dass die `pygame.mixer`-Bibliothek richtig installiert und initialisiert wurde, um die Hintergrundmusik abzuspielen.
- **Abstürzende Anwendungen:** Wenn eine Anwendung abstürzt, während sie ausgeführt wird, wird sie nicht automatisch neu gestartet. Der Launcher bleibt jedoch stabil.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
