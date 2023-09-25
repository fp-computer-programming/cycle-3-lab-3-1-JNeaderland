#Author: Jacob Neaderland
magic_charge = input("Whats is your magic charge?")
shield_charge = input("What is your shield_charge?")

magic_charge = int (magic_charge)
shield_charge = int(shield_charge)

if not (magic_charge >= 90 or shield_charge >= 75):
    print ("The dragon burns you to a crisp.")
else:
	print ("You defeated the dragon! But the princess is in another castle.")