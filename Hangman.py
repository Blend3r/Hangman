import random
import os
import pygame

pygame.mixer.init()

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
def making_a_guess():
    x = 0
    global update_display, guess
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
            pygame.mixer.Sound('right.wav').play()
        x += 1
    if correct_guess == False:
        print(f"There is no {guess}, sorry.")
        pygame.mixer.Sound('wrong.wav').play()
        update_display += 1
    x = 0


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def play_game():
    global update_display, blank_list, chosen_word, guess

    word_list = [    "python", "guitar", "elephant", "whisper", "jigsaw", "library", "mystery", "blizzard", "crescent", "puzzle",
    "journey", "treasure", "oxygen", "glacier", "phantom", "zebra", "harmony", "breeze", "galaxy", "orbit",
    "quartz", "canyon", "jungle", "flamingo", "pirate", "monarch", "nugget", "sphinx", "victory", "wizard",
    "rocket", "shadow", "sapphire", "boulder", "whistle", "horizon", "goblin", "lantern", "tornado", "dolphin",
    "marble", "pickle", "squirrel", "voyage", "feather", "nectar", "cascade", "fortune", "meadow", "anchor",
    "bamboo", "cosmic", "paradox", "frost", "tundra", "hurdle", "violet", "asteroid", "clover", "amber",
    "spider", "scepter", "ivory", "dagger", "potion", "basilisk", "mirage", "zephyr", "gargoyle", "fable",
    "chimney", "harbor", "knight", "castle", "voyager", "turquoise", "phoenix", "blossom", "compass", "pyramid",
    "cyclone", "ember", "prism", "dragonfly", "galleon", "oracle", "pebble", "riddle", "falcon", "quiver",
    "crystal", "forest", "thunder", "moonlight", "avalanche", "enigma", "serpent", "labyrinth", "lighthouse",
    "quicksand", "sorcerer", "asterisk", "barrel", "canvas", "desert", "engine", "flourish", "grizzly", "harvest",
    "icicle", "jackal", "kimono", "lizard", "mariner", "nectarine", "octopus", "penguin", "quagmire", "rainbow",
    "safari", "telescope", "umbrella", "vortex", "warrior", "xylophone", "yacht", "zephyr", "alchemy", "bamboo",
    "candlestick", "daylight", "emerald", "fern", "gorilla", "hydrant", "illusion", "jasmine", "kettle", "lantern",
    "mocha", "nectar", "obelisk", "peacock", "quarry", "ranger", "shimmer", "topaz", "umpire", "velvet",
    "wolverine", "xenon", "yellow", "zeppelin", "apricot", "balloon", "canyon", "diamond", "earthen", "firefly",
    "gigantic", "hedgehog", "infinity", "junction", "kilogram", "latitude", "mulberry", "nautilus", "oasis",
    "plummet", "quicksilver", "rosewood", "sparrow", "talisman", "underwater", "voyager", "waterfall", "zeppelin",
    "albatross", "bonfire", "carousel", "dragon", "entourage", "freckle", "goblet", "hummingbird", "inception",
    "journeyman", "keystone", "lantern", "marble", "nomadic", "octagon", "parrot", "quiver", "riverbank",
    "silhouette", "trapezoid", "utopia", "volcano", "watermelon", "xenophobia", "yonder", "zodiac", "armadillo",
    "butterfly", "conundrum", "daisy", "equator", "feather", "goldmine", "haunted", "invention", "jackpot", 
    "kangaroo", "luminous", "marzipan", "nostalgia", "onyx", "platform", "quartzite", "robust", "scorpion",
    "terrarium", "umbrella", "veranda", "windowpane", "xylophonist", "yogurt", "zeppelin", "accordion", 
    "backpack", "cathedral", "dewdrop", "evergreen", "fascinate", "grapevine", "hedge", "iguana", "jukebox",
    "kindle", "lighthouse", "moonbeam", "nightfall", "outpost", "pacific", "quest", "resonance", "seagull",
    "tundra", "utensil", "vista", "whimsical", "xylophone", "youngster", "zeppelin", "aesthetic", "blizzard",
    "companion", "dungeon", "eclipse", "fractal", "gargantuan", "harbinger", "invisible", "journey", "kaleidoscope",
    "labyrinth", "miracle", "neutron", "opal", "paradise", "quasar", "rhombus", "symphony", "twilight", "utopia",
    "velocity", "waterway", "xylitol", "yearning", "zenith", "astronomy", "blossom", "constellation", "dandelion",
    "effervescent", "fountain", "glimmer", "horizon", "illusion", "jungle", "keystone", "lunar", "mirage", 
    "nightmare", "overture", "pixie", "quicksilver", "relic", "shadow", "telescope", "unicorn", "vapor", 
    "whirlwind", "xylophone", "zephyr", "aurora", "beacon", "crescendo", "daydream", "ethereal", "fable",
    "galaxy", "harmony", "infinite", "jeopardy", "kingdom", "lullaby", "mystical", "nebula", "oasis", "pendulum",
    "quest", "reflection", "starlight", "tranquil", "undertow", "vortex", "wonderland", "xenith", "yonder", "zenith",
    "acoustic", "bizarre", "cavalier", "delicate", "emerald", "fantasy", "glorious", "hazard", "intrigue", 
    "jubilee", "kindred", "legacy", "mosaic", "noble", "overture", "parable", "quirky", "radiance", "serenade",
    "tempest", "uplift", "vivacious", "wanderer", "xylophone", "yearn", "zealous", "alpine", "breeze", 
    "chariot", "devotion", "ephemeral", "frost", "gleaming", "halcyon", "intricate", "javelin", "knight", 
    "luminous", "mirth", "nexus", "opulent", "pasture", "quaint", "reverie", "specter", "twine", "ultraviolet",
    "verdant", "whimsy", "xanadu", "yule", "zephyr"]
    chosen_word = list(random.choice(word_list))

    blank = ""
    for letter in chosen_word:
        blank += "_"
    blank_list = list(blank)

    update_display = 0

    clear_screen()
    print(HANGMANPICS[update_display])
    guess = input(f"Welcome to hangman.\n{blank}\nMake a guess? ")
    making_a_guess()
    clear_screen()
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))
    while update_display < 6:
        if blank_list == chosen_word:
            print("YOU WIN!")
            pygame.mixer.stop()
            pygame.mixer.Sound('win.wav').play()
            break
        guess = input("Make another guess? ")
        making_a_guess()
        clear_screen()
        print(HANGMANPICS[update_display])
        print(''.join(blank_list))

    if update_display == 6:
        print("GAME OVER.")
        pygame.mixer.stop()
        pygame.mixer.Sound('lose.wav').play()
        print(f"The word was: {''.join(chosen_word)}")


while True:
    play_game()
    restart = input("Press enter to exit or press 'r' to restart the game: ")
    if restart.lower() != 'r':
        break

print("Thanks for playing!")