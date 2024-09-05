import sys
import os
import json
import random
import shutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout, QScrollArea, QDialog, QListWidget, QListWidgetItem,
    QMessageBox, QLineEdit
)
from PyQt5 import QtCore

class ShipMasteryApp(QWidget):
    def __init__(self, config_path, app):
        super().__init__()
        self.setWindowTitle('World of Warships Ship Mastery')
        self.config_path = config_path
        self.app = app
        self.load_data()
        self.initUI()

    def load_data(self):
        try:
            with open(self.config_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            QMessageBox.critical(self, "Fehler", "Konfigurationsdatei nicht gefunden!")
            self.close()

    def initUI(self):
        main_layout = QVBoxLayout()

        self.scroll_area = QScrollArea(self)
        self.scroll_area_widget = QWidget()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_area_widget)

        self.scroll_layout = QVBoxLayout(self.scroll_area_widget)

        self.save_button = QPushButton('Speichern', self)
        self.save_button.clicked.connect(self.save_data)

        logout_button = QPushButton('Abmelden', self)
        logout_button.clicked.connect(self.logout)

        main_layout.addWidget(self.scroll_area)
        main_layout.addWidget(self.save_button)
        main_layout.addWidget(logout_button)

        self.setLayout(main_layout)
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)

        self.populate_ui()

    def populate_ui(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

        if not self.data:
            return

        for tier, tier_data in self.data['ships']['tier'].items():
            for nation, nation_data in tier_data['nation'].items():
                for ship_class, class_data in nation_data['class'].items():
                    for ship_name, mastery_value in class_data.items():
                        ship_layout = QVBoxLayout()

                        ship_layout.addWidget(QLabel(ship_name))

                        combo_box = QComboBox()
                        combo_box.addItems(["Nicht gekauft", "schlecht", "mittel", "gut"])

                        if mastery_value is None:
                            combo_box.setCurrentIndex(0)
                        else:
                            combo_box.setCurrentIndex(mastery_value + 1)

                        combo_box.currentIndexChanged.connect(
                            lambda value, ship=ship_name: self.update_mastery(ship, value)
                        )

                        ship_layout.addWidget(combo_box)
                        self.scroll_layout.addLayout(ship_layout)

    def update_mastery(self, ship_name, mastery_value):
        for tier, tier_data in self.data['ships']['tier'].items():
            for nation, nation_data in tier_data['nation'].items():
                for ship_class, class_data in nation_data['class'].items():
                    if ship_name in class_data:
                        class_data[ship_name] = None if mastery_value == 0 else mastery_value - 1
                        return

    def save_data(self):
        if not self.config_path:
            return

        try:
            with open(self.config_path, 'w') as file:
                json.dump(self.data, file, indent=4)
            QMessageBox.information(self, "Erfolg", "Daten erfolgreich gespeichert!")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Speichern der Daten: {e}")

    def logout(self):
        self.close()
        self.app.show_login_window()


class LoginWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle('Anmeldung')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText('Benutzername')
        layout.addWidget(self.username_input)

        self.login_button = QPushButton('Anmelden', self)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton('Registrieren', self)
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.delete_button = QPushButton('Benutzer löschen', self)
        self.delete_button.clicked.connect(self.delete_user)
        layout.addWidget(self.delete_button)

        self.view_users_button = QPushButton('Alle Benutzer anzeigen', self)
        self.view_users_button.clicked.connect(self.view_users)
        layout.addWidget(self.view_users_button)

        self.setLayout(layout)
        self.setFixedSize(300, 200)
        self.update_users_file()

    def login(self):
        username = self.username_input.text().strip()
        users_file_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config', 'users.json')

        if not os.path.exists(users_file_path):
            QMessageBox.critical(self, "Fehler", "Benutzerdatenbank nicht gefunden!")
            return

        with open(users_file_path, 'r') as users_file:
            users = json.load(users_file)

        if username in users:
            config_path = users[username]
            self.app.show_main_window(config_path)
            self.close()
        else:
            QMessageBox.critical(self, "Fehler", "Benutzer nicht gefunden!")

    def register(self):
        username = self.username_input.text().strip()
        if not username:
            QMessageBox.warning(self, "Warnung", "Benutzername darf nicht leer sein!")
            return

        users_file_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config', 'users.json')
        if not os.path.exists(users_file_path):
            users = {}
        else:
            with open(users_file_path, 'r') as users_file:
                users = json.load(users_file)

        if username in users:
            QMessageBox.warning(self, "Warnung", "Benutzername existiert bereits!")
            return

        config_path = self.create_user_directory(username)
        users[username] = config_path

        with open(users_file_path, 'w') as users_file:
            json.dump(users, users_file, indent=4)

        QMessageBox.information(self, "Erfolg", "Benutzer erfolgreich registriert!")
        self.app.show_main_window(config_path)
        self.close()

    def create_user_directory(self, username):
        user_id = random.randint(10000, 99999)
        user_folder_name = f"usr.{username}.id{user_id}"
        user_folder_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config', user_folder_name)

        os.makedirs(user_folder_path, exist_ok=True)
        default_config_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'config.json')
        user_config_path = os.path.join(user_folder_path, f"{user_folder_name}.json")
        shutil.copyfile(default_config_path, user_config_path)
        return user_config_path

    def delete_user(self):
        username = self.username_input.text().strip()
        users_file_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config', 'users.json')

        if not os.path.exists(users_file_path):
            QMessageBox.critical(self, "Fehler", "Benutzerdatenbank nicht gefunden!")
            return

        with open(users_file_path, 'r') as users_file:
            users = json.load(users_file)

        if username in users:
            confirmation = QMessageBox.question(self, "Benutzer löschen",
                                                f"Möchten Sie den Benutzer '{username}' wirklich löschen?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                user_folder_name = users[username].split('\\')[-2]  # Adjust if path uses '/' instead of '\\'
                user_folder_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config', user_folder_name)
                shutil.rmtree(user_folder_path)
                del users[username]

                with open(users_file_path, 'w') as users_file:
                    json.dump(users, users_file, indent=4)

                QMessageBox.information(self, "Erfolg", "Benutzer erfolgreich gelöscht!")
                self.update_users_file()
        else:
            QMessageBox.critical(self, "Fehler", "Benutzer nicht gefunden!")

    def update_users_file(self):
        users_file_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config', 'users.json')
        user_config_folder = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config')

        if not os.path.exists(users_file_path):
            users = {}
        else:
            with open(users_file_path, 'r') as users_file:
                users = json.load(users_file)

        for folder_name in os.listdir(user_config_folder):
            folder_path = os.path.join(user_config_folder, folder_name)
            if os.path.isdir(folder_path):
                config_file_path = os.path.join(folder_path, f"{folder_name}.json")
                if os.path.exists(config_file_path):
                    username = folder_name.split('.')[1]
                    users[username] = config_file_path

        with open(users_file_path, 'w') as users_file:
            json.dump(users, users_file, indent=4)

    def view_users(self):
        dialog = ViewUsersDialog(self)
        dialog.exec_()


class ViewUsersDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Alle Benutzer anzeigen')
        self.setMinimumWidth(400)

        layout = QVBoxLayout()

        users_list_widget = QListWidget()
        users_list_widget.setAlternatingRowColors(True)

        users_file_path = os.path.join(os.path.dirname(__file__), 'src', 'data', 'config_files', 'user_config', 'users.json')
        if not os.path.exists(users_file_path):
            QMessageBox.critical(self, "Fehler", "Benutzerdatenbank nicht gefunden!")
            return

        with open(users_file_path, 'r') as users_file:
            users = json.load(users_file)

        for username, config_path in users.items():
            item = QListWidgetItem(f'{username}: {config_path}')
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            users_list_widget.addItem(item)

        layout.addWidget(users_list_widget)

        self.setLayout(layout)


class MyApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.main_window = None
        self.login_window = LoginWindow(self)
        self.login_window.show()

    def show_main_window(self, config_path):
        if self.main_window:
            self.main_window.close()
        self.main_window = ShipMasteryApp(config_path, self)
        self.main_window.show()

    def show_login_window(self):
        if self.main_window:
            self.main_window.close()
        self.login_window = LoginWindow(self)
        self.login_window.show()


if __name__ == '__main__':
    app = MyApp(sys.argv)
    sys.exit(app.exec_())
