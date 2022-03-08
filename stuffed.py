
import random

def random_animal():
    items = ["Peachy Unicorn", "Cotton Candy", "Mer-Cat", "Whiskers the Cat" , "Aphmau Fairy Cat", "Bessie the Cat"]
    weights = [0.05,0.05,0.1,0.1,0.2,0.5]
    random_item = random.choices(items,weights)
    #print(random_item)
    return str(random_item)

if __name__ == "__main__":
    random_animal()

