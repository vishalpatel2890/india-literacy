import numpy as np

def random_color(country):
        x = np.random.choice(range(256))
        y = np.random.choice(range(256))
        z = np.random.choice(range(256))
        return f'rgb({x},{y},{z})'
