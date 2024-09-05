import os


score = 10


class TemporaryManager:
    def __init__(self, filename='C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\saves\\temp_save.txt'):
        self.filename = filename
        self.last_session_score = self.load_last_session_score()

    def load_last_session_score(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                line = file.readline().strip()
                if line:
                    score = int(line)
                    return score
        return 0

    def save_last_session_score(self, score):
        with open(self.filename, 'w') as file:
            file.write(f"{score}\n")

    def set_last_session_score(self, score):
        self.last_session_score = score
        self.save_last_session_score(score)

    def get_last_session_score(self):
        return self.last_session_score
