from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)

Joffrey.set_eyes("blue")
print(Joffrey.get_eyes())

Joffrey.set_hairs("light")
print(Joffrey.get_hairs())

print(Joffrey.__dict__)
