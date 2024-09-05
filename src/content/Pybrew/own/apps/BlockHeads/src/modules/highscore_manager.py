import os

class HighscoreManager:
    def __init__(self, filename='C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\saves\\saves.txt'):
        self.filename = filename
        self.highscore = self.load_highscore()

    def load_highscore(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                line = file.readline().strip()
                if line:
                    name, score = line.split(':')
                    return {'name': name, 'score': int(score)}
        return {'name': 'highscore', 'score': 0}

    def save_highscore(self):
        with open(self.filename, 'w') as file:
            file.write(f"{self.highscore['name']}:{self.highscore['score']}\n")

    def set_highscore(self, score):
        self.highscore = {'name': 'highscore', 'score': score}
        self.save_highscore()

    def get_highscore(self):
        return self.highscore['score']
