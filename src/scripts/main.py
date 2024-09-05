def run():
    import os
    import pygame
    import subprocess
    import tkinter as tk
    from tkinter import messagebox
    from PIL import Image, ImageTk, ImageEnhance

    class PybrewLauncher:
        def __init__(self, root):
            self.root = root
            self.script_dir = os.path.dirname(os.path.abspath(__file__))
            self.music_path = os.path.join(self.script_dir, os.pardir, 'assets', 'aud', 'soundtrack.mp3')
            self.icon_path = os.path.join(self.script_dir, os.pardir, 'assets', 'img', '3ds-homebrew.png')
            self.app_process = None

            self.setup_ui()
            self.play_music()

        def setup_ui(self):
            self.root.title("Pybrew Launcher v0.1")  # Version im Fenstertitel
            self.root.geometry("1280x720")
            self.root.resizable(False, False)  # Fenstergröße fixieren
            self.root.configure(bg='#3C3C3C')

            # Icon des Launchers setzen
            icon_img = tk.PhotoImage(file=self.icon_path)
            self.root.iconphoto(False, icon_img)

            # Überschrift "Pybrew Launcher v0.1" hinzufügen
            title_label = tk.Label(self.root, text="Pybrew Launcher v0.1", font=("Arial", 24), bg='#3C3C3C', fg='white')
            title_label.pack(pady=10)

            # Die aktuelle Zeit anzeigen
            self.time_label = tk.Label(self.root, font=("Arial", 16), bg='#3C3C3C', fg='white')
            self.time_label.place(relx=1.0, x=-10, y=10, anchor='ne')
            self.update_time()  # Initiale Zeit setzen

            # Apps hinzufügen mit angepasstem Abstand
            blockheads_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'BlockHeads', 'src', 'main.py')
            blockheads_icon_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'BlockHeads', 'blockheadz_icon.png')
            self.create_app("BlockHeads", blockheads_icon_path, blockheads_path, (10, 100))

            minecraft_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'MinecraftPygameEdition', 'src', 'main.py')
            minecraft_icon_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'MinecraftPygameEdition', 'pyblocks_demo_icon.png')
            self.create_app("Minecraft Pygame Edition", minecraft_icon_path, minecraft_path, (180, 100))

            pytris_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'Pytris', 'src', 'main.py')
            pytris_icon_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'Pytris', 'assets', 'img', 'pytris_icon.png')
            self.create_app("Pytris", pytris_icon_path, pytris_path, (350, 100))

            wows_ship_mastery_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'WoWs Ship Mastery', 'windows-build.ver1.0', 'uncompiled', 'WoWs Ship Mastery', 'data', 'main.py')
            wows_ship_mastery_icon_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'WoWs Ship Mastery', 'wows_ship_mastery_icon.png')
            self.create_app("WoWs Ship Mastery", wows_ship_mastery_icon_path, wows_ship_mastery_path, (520, 100))

            calculator_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'Calculator', 'main.py')
            calculator_icon_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'Calculator', 'simple_calculator.png')
            self.create_app("Calculator", calculator_icon_path, calculator_path, (690, 100))

            informatik_projekt_woche_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'InformatikProjektWoche', 'src', 'main.py')
            informatik_projekt_woche_icon_path = os.path.join(self.script_dir, os.pardir, 'content', 'Pybrew', 'own', 'apps', 'InformatikProjektWoche', 'informatik_projekt_woche_icon.png')
            self.create_app("Informatik Projekt Woche", informatik_projekt_woche_icon_path, informatik_projekt_woche_path, (860, 100))

        def play_music(self):
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play(-1)  # Endlosschleife

        def stop_music(self):
            pygame.mixer.music.stop()

        def create_hover_effect(self, image):
            if image.mode != "RGB":
                image = image.convert("RGB")
            enhancer = ImageEnhance.Brightness(image)
            return enhancer.enhance(1.2)  # Erhöht die Helligkeit um 20%

        def create_app(self, name, icon_path, script_path, position):
            # Icon laden und skalieren
            icon_img = Image.open(icon_path)
            icon_img = icon_img.resize((150, 150), Image.Resampling.LANCZOS)

            # Erstelle die Hover-Variante des Icons
            icon_img_hover = self.create_hover_effect(icon_img)
            icon = ImageTk.PhotoImage(icon_img)
            icon_hover = ImageTk.PhotoImage(icon_img_hover)

            # Erstelle einen Button mit dem Icon
            button = tk.Button(self.root, image=icon, command=lambda: self.launch_program(script_path), borderwidth=0, bg='#3C3C3C')
            button.place(x=position[0], y=position[1])

            # Hover-Effekte aktivieren
            button.bind("<Enter>", lambda event: button.config(image=icon_hover))
            button.bind("<Leave>", lambda event: button.config(image=icon))

            # Reference to prevent garbage collection
            button.icon = icon
            button.icon_hover = icon_hover

        def launch_program(self, script_path):
            if self.app_process is not None:
                messagebox.showinfo("Info", "Eine App läuft bereits. Bitte schließen Sie die laufende App, bevor Sie eine neue starten.")
                return

            self.stop_music()  # Stoppe die Musik, wenn eine App gestartet wird
            self.root.iconify()  # Minimiert das Fenster

            try:
                self.app_process = subprocess.Popen(['python', script_path])
                self.root.after(1000, self.check_process)  # Überprüfen nach 1 Sekunde
            except Exception as e:
                messagebox.showerror("Error", f"Could not launch the program.\n{str(e)}")
                self.app_process = None  # Im Fehlerfall auch den Prozess zurücksetzen

        def check_process(self):
            if self.app_process is not None:
                retcode = self.app_process.poll()
                if retcode is not None:  # Der Prozess ist beendet
                    self.app_process = None
                    self.play_music()  # Musik nach Schließen der App wieder starten
                    self.root.deiconify()  # Wiederherstellen des Fensters
                    self.root.attributes('-topmost', 1)  # Setzt das Fenster in den Vordergrund
                    self.root.attributes('-topmost', 0)  # Entfernt das Fenster aus dem Vordergrundmodus
                else:
                    self.root.after(1000, self.check_process)  # Überprüfen nach weiteren 1 Sekunde

        def update_time(self):
            from datetime import datetime
            now = datetime.now()
            time_string = now.strftime("%H:%M")
            self.time_label.config(text=time_string)
            self.root.after(500, self.blink_colon)

        def blink_colon(self):
            current_text = self.time_label.cget("text")
            if ":" in current_text:
                self.time_label.config(text=current_text.replace(":", " "))
            else:
                self.time_label.config(text=current_text.replace(" ", ":"))
            self.root.after(500, self.blink_colon)

    def main():
        root = tk.Tk()
        PybrewLauncher(root)
        root.mainloop()

    if __name__ == "__main__":
        main()

run()
