"""Tyler Langtry"""


name = input("Name?")

while len(name) == 0:
    name = input("Name?")

print(name[1::2])
