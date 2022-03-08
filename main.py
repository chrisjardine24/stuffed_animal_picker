
import random


items = ["Peachy Unicorn", "Cotton Candy", "Mer-Cat", "Whiskers the Cat" , "Aphmau Fairy Cat", "Bessie the Cat"]
weights = [1,1,1,1,2,6]
random_item = random.choices(items,weights)

print(random_item)