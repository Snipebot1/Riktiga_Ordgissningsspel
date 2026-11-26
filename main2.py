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
   
bokstäver=[
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z',
'å', 'ä', 'ö', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z',
'Å', 'Ä', 'Ö'
]
ord = random.choice(ordlista)

gissade_bokstäver = []
gissning_försök = 10
 


while gissning_försök > 0:
    gissning = input(f"Du ska gissa ett ord, bokstav för bokstav, på 9 bokstäver\n Ange en gissning ").lower()
    
    if gissning in gissade_bokstäver:
        print("Du har redan gissat den bokstaven!")
        continue
    
    gissade_bokstäver.append(gissning)
        
    
    if gissning in ord:
        print("Rätt bokstav!")
    elif gissning not in bokstäver:
        print("Ogiltigt gissning")
    else:
        gissning_försök=gissning_försök- 1
        print(f"Du har {gissning_försök} gissningar kvar.")
    
    print("Ordet:", end=" ")
    print("Felgissningar:", end=" ")

    for bokstav in ord:
        if bokstav in gissade_bokstäver:
            print(bokstav, end=" ")
        else:
            print("*", end=" ")
    print("\n") 



   
if all(bokstav in gissade_bokstäver for bokstav in ord):
    print("\nGrattis! Du gissade rätt ord:", ord)
    
      
        

if gissning_försök == 0:
    print("\nDu förlorade! Ordet var:", ord)
















