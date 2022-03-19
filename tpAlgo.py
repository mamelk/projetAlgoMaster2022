# QUESTION 1 :  INTERSECTION DE DEUX CERCLES

Fonction intersection_cercle():booleen
    Reel x1, x2, y1, y2, r1, r2;

    DEBUT
        Ecrire ("Taper la coordonnée x, y et le rayon du premier cercle");
        Lire (x1, y1, r1);

        Ecrire("Taper la coordonnées x, y, et le rayon du deuxième cercle");
        Lire(x2, y2, r2);

        Si (sqrt((x2-x1)^2 + (y2-y1)^2) <= (r1+r2)) alors
            retourner Vrai;
        Sinon
            Retourner Faux;
        Finsi
    FIN
Finfonction

# COMPLEXITE : complexité constante


# QUESTION 2: tableau trié

Fonction tableau_trie(tab1 : Reel, tab2 : Reel) : *Reel
    Reel tab3[];
    Entier i, x, p;

    DEBUT
        Redim tab3[longueur(tab1)+longueur(tab2)];
        # RECUPERATION DES ELEMENTS DU PREMIERS TABLEAUX
        Pour i = 0 a longueur(tab1)-1 faire
            tab3[i] = tab1[i];
        Finpour

        # RECUPERATION DES ELEMENTS DU DEUXIEME TABLEAU
        Pour i = longueur(tab1) a longueur(tab1) + longueur(tab2)-1 faire
            tab3[i] = tab2[i-longueur(tab1)];
        Finpour

        # TRIE DU TROISIEME TABLEAU
        Pour i = longueur(tab3-1) a 0 faire
            pour j = 0 a i - 1
                Si tab3[j + 1] < tab3[j] alors
                    p = tab3[j + 1];
                    tab3[j + 1] = tab3[j];
                    tab3[j] = p;
                Finsi
            Finpour
        Finpour
        Retourner *tab3;
Finfonction

# COMPLEXITE : complexité quadratique
