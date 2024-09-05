# Block Heads v1.0

Dies ist ein einfaches 2D-Shoot-'em-up-Spiel, das mit PyGame erstellt wurde. Der Spieler steuert einen Block Head, weicht feindlichen Projektilen aus und schießt auf Gegner, um Punkte zu sammeln. Das Spiel speichert den Highscore zwischen den Sitzungen.

## Spielbeschreibung

- **Ziel**: Überlebe so lange wie möglich und sammle so viele Punkte wie möglich, indem du feindliche Block Heads abschießt.
- **Steuerung**:
  - `WASD` oder Pfeiltasten: Bewegen des Spielers.
  - `Rechte Umschalttaste`: Schießen.
  - `Esc`: Spiel beenden.
  - `Leertaste`: Spiel neu starten, wenn der Spieler gestorben ist.

## Installation

1. **Python installieren**: Stelle sicher, dass Python 3.x (Wurde mit Python 3.12.3 programmiert) auf deinem System installiert ist. Du kannst es von [python.org](https://www.python.org/) herunterladen.

2. **Bibliothek installieren**: Installiere die benötigten Python-Bibliotheken mit pip:

    ```bash
    pip install pygame
    ```

3. **Projektstruktur**: Stelle sicher, dass die Projektdateien die folgende Struktur haben:

    ```
    my_game/
    ├── img/
    │   ├── player.png
    │   ├── enemy.png
    │   ├── bullet.png
    │   ├── enemy_bullet.png
    │   └── python_icon.ico
    ├── sound/
    │   ├── background_music.wav
    │   ├── shoot_sound.wav
    │   ├── player_death_sound.wav
    │   └── enemy_death_sound.wav
    ├── saves/
    │   └── save.txt
    │   └── saves.txt
    │   └── temp_save.txt
    ├── modules/
    │   ├── settings.py
    │   └── highscore_manager.py
    │   └── temporary_manager.py
    └── main.py
    └── backup.py
    └── README.MD
    └── LICENCE
    ```

## Ausführen des Spiels

Wechsle in das Verzeichnis des Spiels und starte das Spiel mit dem folgenden Befehl:

```bash
python main.py
```

## Viel Spaß beim spielen :D