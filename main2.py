import random

ordlista = [
    "tillkortakommande", "oöverskådlighet", "mångfacetterad", "oförsonlighet", "kontemplation",
    "ambivalens", "obestridlighet", "förnumstighet", "vedergällning", "ogenomtränglighet",
    "förbehållsamhet", "förgänglighet", "oförvitlighet", "inkonsekvens", "prokrastinering",
    "disproportionerlig", "epistemologi", "ontologi", "hermeneutik", "fenomenologi",
    "dialektik", "existentialism", "metafysik", "kausalitet", "determinism",
    "subjektivitet", "objektivitet", "intersektionalitet", "kontradiktion", "dekonstruktion",
    "abstraktionsförmåga", "generalisering", "fragmentering", "individualisering", "institutionalisering",
    "rationalisering", "konceptualisering", "oundgänglighet", "oförklarlighet", "självförhärligande",
    "samvetsbetänkligheter", "förutsättningslöshet", "oefterhärmlighet", "föränderlighet", "ovedersäglig",
    "beskaffenhet", "omständlighet", "tillspetsning", "vederhäftighet", "klandervärdhet",
    "ogenomförbarhet", "eftertrycklighet", "skenhelighet", "undfallenhet", "förhärdelse",
    "prejudicerande", "inkommensurabel", "transcendental", "immanent", "empirisk",
    "hypotetisk", "paradigmskifte", "konceptuell", "deduktion", "induktion",
    "inferens", "analogi", "premiss", "postulat", "axiomatik",
    "teleologisk", "antropocentrism", "eurocentrism", "heterogenitet", "homogenisering",
    "diskrepans", "kontingens", "implikation", "konnotation", "denotation",
    "polysemi", "etymologi", "morfologi", "syntaktisk", "semantik",
    "retorik", "allegori", "parafrasering", "obsolet", "inkommensurabilitet",
    "självmotsägelsefullhet", "ofrånkomlighet", "mångtydighet", "förutsägbarhet", "oeftergivlighet",
    "förkastlighet", "tvetydighet", "vidlyftighet", "omvälvning"
]
   

ord = random.choice(ordlista)

gissade_bokstaver = []
gissning_försök = 10

print("Välkommen till ordgissningsspelet!")
print("Du ska gissa vilket ord datorn har valt.")
print("Du har 10 försök.")

while gissning_försök > 0:

    print("\nOrdet:", end=" ")

    for bokstav in ord:
        if bokstav in gissade_bokstaver:
            print(bokstav, end=" ")
        else:
            print("_", end=" ")

    print("\nFörsök kvar:", gissning_försök)

    gissning = input(f"Du ska gissa ett ord, bokstav för bokstav, på 9 bokstäver\n Ange en gissnings ").lower()

    if gissning in gissade_bokstaver:
        print("Du har redan gissat den bokstaven!")
        continue

    gissade_bokstaver.append(gissning)

    if gissning in ord:
        print("Rätt bokstav!")
    else:
        print("Fel bokstav!")
        gissning_försök -= 1

    if all(bokstav in gissade_bokstaver for bokstav in ord):
        print("\nGrattis! Du gissade rätt ord:", ord)
        break

if gissning_försök == 0:
    print("\nDu förlorade! Ordet var:", ord)
















