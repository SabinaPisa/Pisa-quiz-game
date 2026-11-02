# Pisa Quiz Game - Sabina from Uzbekistan
print("PISA UNIVERSITY QUIZ!")

questions = [
    ["Pisa qayerda? A) Italy B) Spain", "A"],
    ["Pisa minorasi? A) Qiyshiq B) Baland", "A"],
    ["Uni. of Pisa nechanchi yilda? A) 1343 B) 1943", "A"]
]

score = 0
for q, ans in questions:
    print("\n" + q)
    user = input("Javobing A/B: ").upper()
    if user == ans:
        print("Togri! Pisa seni kutmoqda!")
        score += 1
    else:
        print("Xato")

print(f"\nNatija: {score}/3")
if score == 3:
    print("WOW! Sen haqiqiy Pisa talabasisan!")
