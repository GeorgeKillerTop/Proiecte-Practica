def verifica_potrivire(cuvant_dictionar, cuvant_joc):
    lungime_joc = len(cuvant_joc)
    lungime_dict = len(cuvant_dictionar)
    diferenta = lungime_dict - lungime_joc
    if diferenta > 2 and diferenta <0:
        return False
    for i, litera_joc in enumerate(cuvant_joc):
        if litera_joc != '*' and (i >= lungime_dict or cuvant_dictionar[i].upper() != litera_joc):
            return False
    return True
def extrage_si_verifica_cuvinte(dictionar, cuvant_joc,cuvant_complet,litere_gasite):
    aparitii = {}
    with open(dictionar, 'r', encoding='utf-8') as fisier:
        for linie in fisier:
            cuvant_dictionar = linie.strip().split()[0] 
            if verifica_potrivire(cuvant_dictionar, cuvant_joc):
                for litera in cuvant_dictionar:
                    if litera.upper() not in cuvant_joc and litera.upper() not in litere_gasite[len(cuvant_joc):]:
                        if litera in aparitii:
                            aparitii[litera] += 1
                        else:
                            aparitii[litera] = 1
        if not aparitii:
            litere_comune=['E', 'A','Ă','Â', 'Î', 'I', 'R', 'N', 'T', 'Ț', 'U', 'Ș', 'S', 'C', 'L', 'O', 'D', 'M', 'P', 'B', 'V', 'F', 'G', 'H', 'K','Z', 'J', 'X', 'Q']
            for litera in litere_comune:
                litere_gasite+=litera.upper()
                #print(litere_gasite[len(cuvant_joc):])
                if litera.upper() in cuvant_complet:
                    for i in range(len(cuvant_complet)):
                        if cuvant_complet[i] == litera.upper():
                            cuvant_joc = cuvant_joc[:i] + litera.upper() + cuvant_joc[i+1:]
                if cuvant_complet == cuvant_joc:
                    break
            #print(len(litere_gasite[len(cuvant_joc):]))
        else:
            aparitii_sortate = sorted(aparitii.items(), key=lambda x: x[1], reverse=True)
            for litera, numar in aparitii_sortate:
                litere_gasite+=litera.upper()
                #print(litere_gasite[len(cuvant_joc):])
                if litera.upper() in cuvant_complet:
                    for i in range(len(cuvant_complet)):
                        if cuvant_complet[i] == litera.upper():
                            cuvant_joc = cuvant_joc[:i] + litera.upper() + cuvant_joc[i+1:]
                    break
        if cuvant_complet != cuvant_joc:
            #print(cuvant_joc,len(litere_gasite[len(cuvant_joc):]))
            return extrage_si_verifica_cuvinte(dictionar, cuvant_joc, cuvant_complet, litere_gasite)
        else:
            return len(litere_gasite[len(cuvant_joc):])
def extrage_cuvinte_din_fisier(nume_fisier):
    numar_incercari=0
    with open(nume_fisier, 'r', encoding='utf-8') as fisier:
        for linie in fisier:
            parti = linie.strip().split(';')
            if len(parti) == 3:
                index, cuvant_joc, cuvant_complet = parti
                litere_gasite = cuvant_complet
                numar_incercari+=extrage_si_verifica_cuvinte(dictionar, cuvant_joc,cuvant_complet,litere_gasite)
                print(index,numar_incercari,cuvant_complet)
if __name__ == "__main__":
    dictionar = "dictionar.txt"
    lista_cuvinte = "cuvinte_de_verificat.txt"
    cuvant_joc = "*A**C****"
    cuvant_complet = "FAGOCITUL"
    litere_gasite = cuvant_complet
    extrage_cuvinte_din_fisier(lista_cuvinte)
