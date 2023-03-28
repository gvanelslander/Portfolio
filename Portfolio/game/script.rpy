# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image score = "scorepdf.png"
image pok = "pokemon.jpg"
image poklist = "pokelist.png"
image poktitle = "pokpok.png"

# Déclarez les personnages utilisés dans le jeu.
define g = Character('Gérald', color="#c8ffc8")


# Le jeu commence ici
label start:

    scene bureautravail
    "Bonjour comment allez vous?"
    "J'espere que vous allez bien"
    "Qui suis je allez vous me dire et bien...?"
    show picwish at right
    with dissolve
    g "Enchanté je m'appelle Gérald j'ai 24 ans et je suis dévellopeur!"
    g "J'ai fait un bachelier de 3 ans dans les technologies de l'informatique, mais j'ai eu aussi des cours de Game Design."
    g "Le Game Design est le fait de concevoir les principes d'un jeu vidéo, son ambiance et ses mécaniques."
    g "Je vous propose de vous montrer quelques projet que j'ai pu réaliser"

menu:
    g "Par quel projet voulez vous commencer?"
    "Une application qui permet de simplifier la lecture d'un fichier pdf concernant une compétition de golf":
        jump golf
    "Un Demake des combats pokémons":
        jump poke
    "Un jeu sérieux sur l'alcolémie au volant":
        jump alcool

label golf:
    g "Suivez moi!"
    scene golfi
    with dissolve
    show picwish at right
    with dissolve
    g "Bienvenue sur le terrain de golf!"
    g "Etant joueur de golf je participe à quelques compétitions dans mon club de golf."
    g "Tel que le men's day!"
    g "Ce projet a été réalisé pour simplifier un pdf qui contient le classement de cette compétition."
    show score:
        xpos 0
        ypos 0


    g "Je vais revenir un peu en arrière. Le men's day est une compétition hebdomadaire qui à lieu de mi-mars jusqu'à fin septembre."
    g "Chaque semaine votre score du jour est comptabilisé et les 16 personnes ayant le meilleurs scores parmi leur 8 meilleurs scores participent à la finale qui à lieu en octobre."
    g "Et ce fichier pdf est mise à jour chaque semaine, mais le soucis c'est qu'il est très compliqué à lire et de voir à quel position on se situe et quel sont nos scores."
    g "Donc je me suis dis que j'allais créer une application qui permettrai de lire plus facilement ce pdf."

    g "L'application demande à l'utilisateur de rentrer le fichier pdf et demande a l'utilisateur quel est son nom."
    g "En fonction de cela l'utilisateur va pouvoir voir facilement quels sont les scores qu'il a réalisé, son classement et peut voir qui est la personne qui se situe devant lui sur le classement."
    g "Et il a aussi l'occasion de comparer ses scores avec un autre joueur."
    hide score
menu:
    g "C'est tout ce qu'il y a savoir sur ce projet, je vous propose de continuer"
    "Un Demake des combats pokémons":
        jump poke
    "Un jeu sérieux sur l'alcolémie au volant":
        jump alcool
    "Vous me connaissez un peu mieux":
        jump fin

label poke:
    scene pokemon
    with dissolve
    show picwish at right
    with dissolve

    g "Durant ma scolarité j'ai du réaliser un demake de jeu avec un de mes camarades de classes."
    g "Un demake consiste à refaire un jeu de nos jours pour qu'il puisse être joué sur des consoles plus anciennes, et pour cela nous avons choisis Pokémon et plus particulièrement le système de combat"
    g "Pourquoi ce choix? Car cela nous semblait un projet réalisable par rapport aux temps qui nous était donné."
    show poklist:
        xpos 0
        ypos 0
    show poktitle:
        xpos 100
        ypos 0
    g "Ce projet a été réalisé sur pascal (un langage de programmation proche de l'algorithmie)."
    g "Le jeu dure une vingtaine de minutes et tous les graphismes ont été réaliser en ASCII."
    g "L'ASCII est le fait de faire des dessins à l'aide de symboles/chiffres/lettres."
    hide poklist
    hide poktitle
menu:
    g "Voila c'était un de mes premiers projets, passons à la suite!"
    "Une application qui permet de simplifier la lecture d'un fichier pdf concernant une compétition de golf":
        jump golf
    "Un jeu sérieux sur l'alcolémie au volant":
        jump alcool
    "Vous me connaissez un peu mieux":
        jump fin

label alcool:
    scene alcoolvolant
    with dissolve
    show picwish at right
    with dissolve
    g "Boir ou conduire? Il faut choisir!"
    g "Ce n'est pas qu'un slogan! C'est aussi un jeu serieux."
    g "Que j'ai réalisé en cours, il vous montre quels sont les répercussions possible après avoir consommé quelques verres de trop."
    g "Et comment ces effets peuvent vous conduire à faire un accident qui peut avoir des consèquences."
menu:
    g "C'est tout ce qu'il y a savoir sur ce projet, je vous propose de continuer"
    "Une application qui permet de simplifier la lecture d'un fichier pdf concernant une compétition de golf":
        jump golf
    "Un Demake des combats pokémons":
        jump poke
    "Vous me connaissez un peu mieux":
        jump fin

label fin:
    scene bureautravail
    with dissolve
    show picwish at right
    with dissolve

    g "Encore merci à vous d'avoir pris du temps pour me découvrir un peu plus moi et mes projets."
    g "Si vous avez d'éventuelles question je vous invite à m'envoyé un mail à ggvanels@hotmail.be"
