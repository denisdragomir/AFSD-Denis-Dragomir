elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

print("=== A1. Elevii și notele lor ===")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print()
nota_max = max(note)
nota_min = min(note)

print(max(note))
print(min(note))

elevi_max = [elevi[i] for i in range(len(note)) if note[i] == nota_max]
elevi_min = [elevi[i] for i in range(len(note)) if note[i] == nota_min]


print(f"Nota maximă este {nota_max}, obținută de: {', '.join(elevi_max)}")
print(f"Nota minimă este {nota_min}, obținută de: {', '.join(elevi_min)}")
print()
media = sum(note) / len(note)

print("Media clasei esteÎ")
print(media)
print()


for i in range(len(elevi)):
    if note[i] >= 5:
        print(elevi[i])
print()
for i in range(len(note)):
    if note[i] < 10:
        note[i] = min(note[i] + 1, 10)
print("Note după majorare:", note)
print()


elevi.append(elev_nou)
note.append(nota_elev_nou)
print("Elevi actualizați:", elevi)
print("Note actualizate:", note)
print()


if elev_de_sters in elevi:
    poz = elevi.index(elev_de_sters)
    elevi.pop(poz)
    note.pop(poz)
    print(f"Elevul {elev_de_sters} a fost șters.")
else:
    print(f"Elevul {elev_de_sters} nu există.")
print()


for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print()





i = 0
while i < len(interogari_nume):
    nume = interogari_nume[i]
    if nume == "stop":
        break
    if nume in elevi:
        poz = elevi.index(nume)
        print(f"{nume} are nota {note[poz]}")
    else:
        print(f"{nume} nu se află în catalog.")
    i += 1
print()



promovati = sum(1 for n in note if n >= 5)
respinși = len(note) - promovati
print(f"Promovați: {promovati}, Respinși: {respinși}")
print()



note_promovate = [n for n in note if n >= 5]
if len(note_promovate) > 0:
    media_prom = sum(note_promovate) / len(note_promovate)
    print(f"Media promovaților este: {media_prom:.2f}")
else:
    print("Niciun elev promovat.")