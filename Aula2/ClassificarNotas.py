# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

print(" Insira uma nota de 0 a 100, sua notá será classificada de A-F")
nota = float(input("Qual sua nota? "))

#Classificar a nota
if nota >= 90:
    classificacao = "A"
elif nota >= 80:
    classificacao = "B"
elif nota >= 70:
    classificacao = "C"
elif nota >= 60:
    classificacao = "D"
else:
    classificacao = "F"

print(f"Sua nota tem a classificação {classificacao}")

