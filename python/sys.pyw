#SpeedCoding 2020 Lpinf
#Accords du participe passé GUI
#Défi:
#    Ne pas poser de question, faire des propositions
#    Afficher les exemples à l'écran.
#    Faire une interface GUI avec Tk

"""
Système de choix:
choixNN
NN correspond à l'arborescence : 1 = OUI, 2=NON
choix 22211= end2
"""
from tkinter import *
from tkinter.messagebox import *
GUI = Tk()
GUI.title("Accords du participe passé")
GUI['bg']='white'
def error():
    showinfo("Fonction erreur", "Le code cet élément n'a pas encore été implémenté !")
def credits():
    showinfo("About","""
Programme créé par Lpinf (Léonard PIGACHE) 2019,
Dernier build  le mardi 17 mars 2020 a 13h50 
6  builds pour la version actuelle
Version 1.0.3.6""")
menubar = Menu(GUI)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Retour", command=error)
menubar.add_cascade(label="Arborescence", menu=menu1)
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=credits)
menubar.add_cascade(label="Aide", menu=menu3)

GUI.config(menu=menubar)
l = LabelFrame(GUI, text="Accords du Participe Passé", padx=20, pady=20)
l.pack(fill="both", expand="yes")
q = LabelFrame(l, text="Question :", padx=20, pady=20)
q.pack(fill="both", expand="yes")
r = LabelFrame(l, text="Choix", padx=20, pady=20)
r.pack(fill="both", expand="yes")
rep = Label(q, text="A l'intérieure de la frame")
rep.pack
def clear():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Question :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Choix", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    print("cleared screen !")
def end9():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Accord avec le COD").pack()
    Label(r, text="La lettre qu'elles ont écrite").pack()
def end8():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Le participe reste invariable").pack()
    Label(r, text="Elles ont écrit des œuvres admirables").pack()
def end6():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Accord avec le sujet").pack()
    Label(r, text="[...] en anglais ont été traduites").pack()
def end13():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Le participe reste invariable").pack()
    Label(r, text="Elles ont marché longtemps.").pack()
def end4():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Le participe reste invariable").pack()
    Label(r, text="Elles se sont ecrit.").pack()
def end1():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Le participe reste invariable").pack()
    Label(r, text="Elles se sont ecrit.").pack()
def end2():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Accord avec le COD").pack()
    Label(r, text="Les lettres qu'elles se sont écrites.").pack()
def end12():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Accord avec le sujet").pack()
    Label(r, text="Elle se sont promenées").pack()
def end11():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Le PP s'accorde avec le sujet").pack()
    Label(r, text="Elle se sont enfuies.").pack()
def choix121_11():
    clear()
    c1 = Button(r, text="Précède le participe", command=end2)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Ne précède pas le participe", command=end1)
    c2.pack(side=LEFT)
    Label(q, text="Le COD").pack()
def choix121_1():
    clear()
    c1 = Button(r, text="Oui", command=choix121_11)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Non", command=end4)
    c2.pack(side=LEFT)
    Label(q, text="Ya t'il un COD?").pack()
def choix121_21():
    clear()
    c1 = Button(r, text="Oui", command=end4)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Non", command=end12)
    c2.pack(side=LEFT)
    Label(q, text="Fonctionne t'il avec un COI?").pack()
def choix121_2():
    clear()########################################
    c1 = Button(r, text="Oui", command=choix121_21)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Non", command=end11)
    c2.pack(side=LEFT)
    Label(q, text="Existe t'il a la forme active? (sans 'SE')").pack()
def choix121():
    clear()
    c1 = Button(r, text="COD?", command=choix121_1)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Forme active existante?", command=choix121_2)
    c2.pack(side=LEFT)
    Label(q, text="Selectionnez le chemin suivant").pack()
def choix111():
    clear()
    c1 = Button(r, text="Précède le participe", command=end9)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Ne précède pas le participe", command=end8)
    c2.pack(side=LEFT)
    Label(q, text="Le COD").pack()
def choix11():
    clear()
    c1 = Button(r, text="OUI", command=choix111)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="NON", command=end13)
    c2.pack(side=LEFT)
    Label(q, text="Ya t'il un COD?").pack()
def choix12():
    clear()
    c1 = Button(r, text="Pronominal", command=choix121)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Non pronominal", command=end6)
    c2.pack(side=LEFT)
    Label(q, text="Le verbe est :").pack()
def choix1():
    clear()
    c1 = Button(r, text="Avoir", command=choix11)
    c1.pack(side=RIGHT)
    c2 = Button(r, text="Être", command=choix12)
    c2.pack(side=LEFT)
    Label(q, text="Il s'agit de l'auxiliaire").pack()
def end5():
    global r,q
    r.destroy()
    q.destroy()
    q = LabelFrame(l, text="Réponse :", padx=20, pady=20)
    q.pack(fill="both", expand="yes")
    r = LabelFrame(l, text="Exemple", padx=20, pady=20)
    r.pack(fill="both", expand="yes")
    Label(q, text="Accord avec le nom qu'il détermine.").pack()
    Label(r, text="Ces œuvres écrites.").pack()
c1 = Button(r, text="Sans auxiliaire", command=end5)
c1.pack(side=RIGHT)
c2 = Button(r, text="Avec auxiliaire", command=choix1)
c2.pack(side=LEFT)
c2 = Button(l, text="Credits", command=choix1)
Label(q, text="Le participe passé est employé").pack()
GUI.mainloop()
