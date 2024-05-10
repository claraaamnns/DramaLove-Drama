import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définition de la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Visual Novel')

# Chargement des images
personnage_image = pygame.image.load("britanny.jfif")
personnage_image = pygame.transform.scale(personnage_image, (200, 400))
background_image = pygame.image.load("bedroom liv.jpg")
background_image = pygame.transform.scale(background_image, (largeur, hauteur))

# Définition de la police
font = pygame.font.Font(None, 36)
# Fonction pour afficher le texte dans la zone de texte
def afficher_texte(texte):
    bulle_dialogue = pygame.draw.rect(fenetre, BLANC, (0, hauteur - 200, largeur, 200))
    blit_text(fenetre,texte,(bulle_dialogue.x,bulle_dialogue.y),font)


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


# Définition des scènes du visual novel
scenes = [
    {
        "background": background_image,
        "personnage": personnage_image,
        "texte": ["Aujourd'hui est un grand jour: c'est mon premier jour au Princess Heartbreak High School!",
                  " J'ai tellement hâte de rencontrer tout le monde, et qui sait, peut-être que mon prince charmant se trouvera parmi eux?",
                  " Ce matin, je me suis faite toute belle, et j'ai choisi de mettre:",
                  " une robe courte blanche à fleurs roses OU un tailleur féminin rose pâle à paillettes.",
                  " J'espère que tout le monde va me trouver super kawaii trop cute, et remarquer que j'aime la couleur rose!",
                  " Je me suis préparé un petit repas tout mignon pour ma lunch box: des pâtes à l'ail.",
                  " J'ai toujours aimé la grande cuisine, et j'ai appris par moi-même à faire des pâtes et à couper l'ail.",
                  " J'aimerais tellement qu'il y ai un club de cuisine à mon nouveau lycée!",
                  " Avec ce talent, je vais être acceptée illico! ",
                  "Allez, il faut que j'y aille, ou je vais arriver en retard.",
                  "Je m'approche de l'imposante bâtisse qui se dresse devant moi, intrigué par les rumeurs qui entourent ce lycée pas comme les autres.",
                  "Les murs extérieurs affichent une couleur rose éclatante, étincelant sous les rayons du soleil.",
                  " En franchissant le grand portail d'entrée, je me rends compte que tout ce qui compose cet endroit magique est fait de différentes nuances de rose.",
                  " Je n'en crois pas mes yeux. J'avance, ébahie par cette vision que je croyais jusqu'ici être celle du paradis, et remarque que je suis de plus en plus dévisagée par les élèves aux alentours.",
                    " J'entends des chuchotements qui s'interrogent et m'inventent des prénoms, qui affirment m'avoir déjà vue quelque part.",
                    " Je pourrais aller les voir et leur assurer qu'il n'y a aucune chance que ça soit le cas car je viens d'emménager ici pour le travail de mon père, mais je suis trop absorbée par mon nouveau chez moi.",
                    "Soudain, mes bras heurtent quelque chose, et dans mon élan, je fais tomber mes livres que je tenais pourtant fermement contre moi.",
                    " Dans un fracas de feuilles, ils s'étalent au sol, lui aussi rose.",
                    " “Olaaaa! Doucement, ma chérie, tu vas te faire mal.” dit une créature magnifique. C’était un jeune homme blond très chic, avec un visage amical."],
        "choix": ["ramasser", "attendre"]
    },
    {
        "background": background_image,
        "personnage": personnage_image,
        "texte": "Vous choisissez Choix 1. Cela vous mène à la fin 1.",
        "choix": []
    },
    {
        "background": background_image,
        "personnage": personnage_image,
        "texte": "Vous choisissez Choix 2. Cela vous mène à la fin 2.",
        "choix": []
    }
]

# Variables de jeu
scene_actuelle = 0
texte_actuel = 0
scene = None

def afficher_scene():
    global scene, scene_actuelle, texte_actuel
    scene = scenes[scene_actuelle]

    # Affichage du fond et du personnage
    fenetre.blit(scene["background"], (0, 0))
    fenetre.blit(scene["personnage"], (50, 100))

    texte_actuel = 0
    # Affichage du texte
    afficher_texte(scene["texte"][texte_actuel])
    pygame.display.set_caption("Visual Novel - Choix Multiple")

    # Affichage des choix
    #for i, choix in enumerate(scene["choix"]):
        #choix_surface = font.render(choix, True, BLANC)
        #fenetre.blit(choix_surface, (50, 400 + i * 50))

def texte_suivant():
    global scene, scene_actuelle, texte_actuel
    texte_actuel += 1
    if texte_actuel >= len(scene["texte"]):
        pass
    else:
        afficher_texte(scene["texte"][texte_actuel])


def jeu():
    global scene, scene_actuelle, texte_actuel

    running = True
    afficher_scene()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                texte_suivant()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #if 400 <= mouse_y <= 450:
                    #if 50 <= mouse_x <= 350:  # Choix 1
                        #scene_actuelle = 1
                    #elif 450 <= mouse_x <= 750:  # Choix 2
                        #scene_actuelle = 2

        pygame.display.flip()






# Fonction principale pour les choix multiples
def choix_multiple():
    running = True
    choix = None

    while running:
        screen.fill(WHITE)
        draw_text("Choisissez une option :", font, BLACK, screen, 50, 50)

        # Affichage des options
        option1_rect = pygame.Rect(50, 150, 300, 50)
        option2_rect = pygame.Rect(50, 250, 300, 50)

        pygame.draw.rect(screen, BLACK, option1_rect, 2)
        pygame.draw.rect(screen, BLACK, option2_rect, 2)

        draw_text("Option 1", font, BLACK, screen, 60, 160)
        draw_text("Option 2", font, BLACK, screen, 60, 260)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if option1_rect.collidepoint(mouse_pos):
                    choix = "Option 1 choisie"
                    running = False
                elif option2_rect.collidepoint(mouse_pos):
                    choix = "Option 2 choisie"
                    running = False

        pygame.display.update()

    return choix

# Boucle principale du jeu
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        choix = choix_multiple()
        print("Vous avez choisi:", choix)

if __name__ == "__main__":
    main()


