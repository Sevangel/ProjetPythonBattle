import pygame
import pygame.freetype
import sys

from pygame.sprite import spritecollide
from Game import *
from Données import *
from PlayerA import *
from PlayerB import *

class Faiblesses(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()

        self.damage = 5
        self.specialdamageJ1 = 0
        self.specialdamageJ2 = 0

        self.ShrekWeaknesses = [
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

            "a bombe atomique",
            "des bêtes",
            "sur ta personne",
            "un beau gosse",
            "une chiffe mole",
            "un débile profond",
            "un macaque édenté",
            "une ordure méprisable",
            "un rabougri édenté",
            "gros malpropre"
        ]

        self.FlynnWeaknesses = [
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

            "quelqu'un de fou",
            "un petit lapin libidineux",
            "complètement idiot",
            "une pomme de terre écrasée",
            "un manche à balais",
            "un orphelin",
            "un séducteur déplumé",
            "une misérable loque humaine",
            "une vieille crapule",
            "un pâle escroc"
        ]

        self.AbuelitaWeaknesses = [
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

            "des dieux",
            "un festival",
            "dans une orgie",
            "tes ancêtres",
            "un possédé",
            "musiciens et renier ta famille",
            "un vieux débris",
            "un vieux chnoque",
            "une vieille charogne",
            "une pauvre cloche"
        ]