import pygame
import random
import pygame.freetype
import sys
from Game import *
from Données import *
from Menu import *
from PlayerA import *
from PlayerB import *

class Run(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
        self.wordx = 300
        self.wordy = 400
        self.selecty = 40
        self.T1J1 = True
        self.T2J1 = False
        self.T3J1 = False
        self.T4J1 = False
        self.T5J1 = False
        self.T1 = True
        self.T2 = False
        self.T3 = False
        self.T4 = False
        self.T5 = False
        self.Fin = False
        self.titlefont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 14)

        Accroches = [
            "Hey tete de gland",
            "Bonjour mon mignon",
            "Ecoute moi bien petit malin",
            "Je ne me repeterai pas",
            "Soyons clair"
            ""
        ]

        Sujets = [
            "ton haleine",
            "ta face",
            "ta femme",
            "ta dégaine",
            "ton marais",
            "toi, gibier de potence, tu",
            "ta maison",
            "ton âne",
            "tes dents",
            "ton odeur",
            "ton nez",
            "ta tête",
            "ton sens du style",
            "tes oreilles",
            "tes cheveux",
            "toi, greluchon famélique, tu",
            "tes parents",
            "tes larmes",
            "ton sourire",
            "ton éducation",
            "ta mère",
            "ton fils",
            "ton pays",
            "tes traditions",
            "tes chaussures",
            "tes enfants, ces bougres de galapiat",
            "ta fille",
            "ton métier",
            "ta famille",
            "ton grand-père",
            "tu",
            "ton perroquet",
            "ta vie",
            "ton identité",
            "ta verve",
            "sale voyou, tu",
            "ta carapace mario kart",
            "tes insultes",
            "tes pieds",
            "ton vocabulaire"
            ""
        ]

        Verbes = [
            "sens/t/ent comme",
            "a/s/ont perdu contre",
            "es/t/sont né(s) en",
            "raconte/s/nt des blagues sales",
            "a/s/ont surement tué(s)",
            "sera/s/ont toujours seul(s)",
            "es/t/sont aussi bête(s) que",
            "mange/s/nt",
            "dégoûte/s/nt",
            "répugne/s/nt",
            "ressemble/s/nt à",
            "pose/s/nt nu pour",
            "met/s/tent des fringues de vieux",
            "a/s/ont pété sur",
            "a/s/ont des cheveux pire que",
            "es/t/sont très vilain/e/s",
            "fond/s/ent comme",
            "coule/s/nt comme",
            "abandonne/s/nt",
            "es/t/sont aussi bien que",
            "chante/s/nt comme",
            "joue/s/nt comme",
            "veux/t/lent être",
            "danse/s/nt comme",
            "adore/s/nt secrètement",
            "crache/s/nt sur",
            "fabrique/s/nt",
            "laisse/s/nt à désirer",
            "pense/s/nt comme",
            "crois/t/nt en",
            "es/t/sont",
            "découvre/s/nt",
            "admire/s/nt des photos",
            "n'es/t/ne sont pas",
            "a/s/ont été à",
            "fument",
            "conduisent comme",
            "boivent comme",
            "parle/s/nt comme",
            "grimpe/s/nt aux rideaux avec",
            ""
        ]

        Compléments = [
            "la bombe atomique",
            "des bêtes",
            "sur ta personne",
            "un beau gosse",
            "une chiffe mole",
            "un débile profond",
            "un macaque édenté",
            "une ordure méprisable",
            "un rabougri édenté",
            "gros malpropre",
            "quelqu'un de fou",
            "un petit lapin libidineux",
            "complètement idiot",
            "une pomme de terre écrasée",
            "un manche à balais",
            "un orphelin",
            "un séducteur déplumé",
            "une misérable loque humaine",
            "une vieille crapule",
            "un pâle escroc",
            "des dieux",
            "un festival",
            "dans une orgie",
            "tes ancêtres",
            "un possédé",
            "musiciens et renier ta famille",
            "un vieux débris",
            "un vieux chnoque",
            "une vieille charogne",
            "une pauvre cloche",
            "un sinistre individu",
            "un vieux matou",
            "toi",
            "princesse peach",
            "malfaisant",
            "cacochyme",
            "un petit foutriquet",
            "un sale pourri",
            ""
        ]

        MotFin = [
            "et tout le monde le sait !",
            "et j'en ai la preuve !",
            "et tu en as conscience !",
            "et ça ne changera jamais !",
            "et le pire, c'est que tu aimes ça !",
            ""
        ]

        self.word = random.sample(Accroches, 4)
        self.sujet = random.sample(Sujets, 4)
        self.verbe = random.sample(Verbes, 4)
        self.complement = random.sample(Compléments, 4)
        self.wordfin = random.sample(MotFin, 4)


    def Tour1joueur1(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 1 Joueur 1", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour1joueur2(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 1 Joueur 2", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour2joueur1(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 2 Joueur 1", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))
    
    def Tour2joueur2(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 2 Joueur 2", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour3joueur1(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 3 Joueur 1", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour3joueur2(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 3 Joueur 2", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour4joueur1(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 4 Joueur 1", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour4joueur2(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 4 Joueur 2", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour5joueur1(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 5 Joueur 1", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def Tour5joueur2(self, surface) :

        textsurftour, rect = self.titlefont.render("Tour 5 Joueur 2", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

    def T5wordpos(self, surface) :

        textfont = pygame.freetype.Font('Ressources/8bitOperatorBold.ttf', 16)

        mot = self.wordfin


        textsurf1, rect = textfont.render(mot[0], (0,0,0))
        textsurf2, rect = textfont.render(mot[1], (0,0,0))
        textsurf3, rect = textfont.render(mot[2], (0,0,0))
        textsurf4, rect = textfont.render(mot[3], (0,0,0))

        self.screen.blit(textsurf1, (self.wordx + 50,self.wordy + 40))
        self.screen.blit(textsurf2, (self.wordx + 50,self.wordy + 80))
        self.screen.blit(textsurf3, (self.wordx + 50,self.wordy + 120))
        self.screen.blit(textsurf4, (self.wordx + 50,self.wordy + 160))
    
    def T4wordpos(self, surface) :

        textfont = pygame.freetype.Font('Ressources/8bitOperatorBold.ttf', 16)

        mot = self.complement


        textsurf1, rect = textfont.render(mot[0], (0,0,0))
        textsurf2, rect = textfont.render(mot[1], (0,0,0))
        textsurf3, rect = textfont.render(mot[2], (0,0,0))
        textsurf4, rect = textfont.render(mot[3], (0,0,0))

        self.screen.blit(textsurf1, (self.wordx + 50,self.wordy + 40))
        self.screen.blit(textsurf2, (self.wordx + 50,self.wordy + 80))
        self.screen.blit(textsurf3, (self.wordx + 50,self.wordy + 120))
        self.screen.blit(textsurf4, (self.wordx + 50,self.wordy + 160))

    def T3wordpos(self, surface) :

        textfont = pygame.freetype.Font('Ressources/8bitOperatorBold.ttf', 16)

        mot = self.verbe

        textsurf1, rect = textfont.render(mot[0], (0,0,0))
        textsurf2, rect = textfont.render(mot[1], (0,0,0))
        textsurf3, rect = textfont.render(mot[2], (0,0,0))
        textsurf4, rect = textfont.render(mot[3], (0,0,0))

        self.screen.blit(textsurf1, (self.wordx + 50,self.wordy + 40))
        self.screen.blit(textsurf2, (self.wordx + 50,self.wordy + 80))
        self.screen.blit(textsurf3, (self.wordx + 50,self.wordy + 120))
        self.screen.blit(textsurf4, (self.wordx + 50,self.wordy + 160))

    def T2wordpos(self, surface) :

        textfont = pygame.freetype.Font('Ressources/8bitOperatorBold.ttf', 16)

        mot = self.sujet

        textsurf1, rect = textfont.render(mot[0], (0,0,0))
        textsurf2, rect = textfont.render(mot[1], (0,0,0))
        textsurf3, rect = textfont.render(mot[2], (0,0,0))
        textsurf4, rect = textfont.render(mot[3], (0,0,0))

        self.screen.blit(textsurf1, (self.wordx + 50,self.wordy + 40))
        self.screen.blit(textsurf2, (self.wordx + 50,self.wordy + 80))
        self.screen.blit(textsurf3, (self.wordx + 50,self.wordy + 120))
        self.screen.blit(textsurf4, (self.wordx + 50,self.wordy + 160))

    def wordpos(self, surface) :

        textfont = pygame.freetype.Font('Ressources/8bitOperatorBold.ttf', 16)

        mot = self.word

        textsurf1, rect = textfont.render(mot[0], (0,0,0))
        textsurf2, rect = textfont.render(mot[1], (0,0,0))
        textsurf3, rect = textfont.render(mot[2], (0,0,0))
        textsurf4, rect = textfont.render(mot[3], (0,0,0))

        self.screen.blit(textsurf1, (self.wordx + 50,self.wordy + 40))
        self.screen.blit(textsurf2, (self.wordx + 50,self.wordy + 80))
        self.screen.blit(textsurf3, (self.wordx + 50,self.wordy + 120))
        self.screen.blit(textsurf4, (self.wordx + 50,self.wordy + 160))

    def selectionmot(self) :

        textfont = pygame.freetype.Font('Ressources/8bitOperator.ttf', 16)
        buttonmot, rect = textfont.render("X", (0,0,0))
        self.screen.blit(buttonmot, (self.wordx, self.wordy + self.selecty))


    def moveselectiondown(self) :

        if self.selecty >= 160 :
            self.selecty = self.selecty + 0
        else :
            self.selecty = self.selecty + 40
        
            
    def moveselectionup(self) :
    
        if self.selecty <= 40 :
            self.selecty = self.selecty - 0
        else :
            self.selecty = self.selecty - 40