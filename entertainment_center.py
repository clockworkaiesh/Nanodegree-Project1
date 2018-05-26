import fresh_tomatoes
import media

lone_survivor = media.Movie(
    "Lone Suvivor",
    "Lone Survivor is a 2013 American biographical war thriller film based on the 2007 eponymous non-fiction book",  # NOQA
    "https://movieposters2.com/images/1301381-b.jpg",
    "https://youtu.be/yoLFk4JK_RM")


adrift = media.Movie(
    "Adrift",
    "Story of 2 avid sailors setting out on a journey across the ocean, meets a catastrophic hurricanes in recorded history.",  # NOQA
    "https://goo.gl/EaCfqR",
    "https://youtu.be/n9ukI7khQpE")


ratatouille = media.Movie(
    "Ratatouille",
    "Remy dreams of becoming a great chef, despite being a rat in a definitely rodent-phobic profession.",  # NOQA
    "https://goo.gl/35XcjG",
    "https://youtu.be/uVeNEbh3A4U")


big_hero_6 = media.Movie(
    "Big Hero 6",
    "Determined to uncover the mystery, Hiro transforms his friends into a band of high-tech heroes called Big Hero 6",  # NOQA
    "https://goo.gl/RQQzAd",
    "https://youtu.be/z3biFxZIJOQ")


age_of_adaline = media.Movie(
    "Age Of Adaline",
    "Adaline Bowman has miraculously remained a youthful 29 years of age for nearly eight decades, and hides her secret",  # NOQA
    "https://goo.gl/gP3GLC",
    "https://youtu.be/7UzSekc0LoQ")


me_before_you = media.Movie(
    "Me Before You",
    "Young and quirky Louisa, is put to the test when she becomes a caregiver for Will Traynoraccident.",  # NOQA
    "https://goo.gl/qk82bS",
    "https://youtu.be/Eh993__rOxA")


kingsman = media.Movie(
    "Kingsman: The Golden Circle",
    "It's James Bond On Laughing Gas.",
    "https://goo.gl/g3gh53",
    "https://youtu.be/6Nxc-3WpMbg")


mission_impossible = media.Movie(
    "Mission Impossible: Rogue Nation",
    "With the IMF now disbanded and Ethan Hunt out in the cold, a new threat - called the Syndicate - soon emerges",  # NOQA
    "https://goo.gl/mYiuzQ",
    "https://youtu.be/pXwaKB7YOjw")


camp_xray = media.Movie(
    "Camp X Ray",
    "A female guard at Guantanamo Bay forms an unlikely friendship with one of the facility's longtime detainees.",  # NOQA
    "https://goo.gl/1MEsqM",
    "https://youtu.be/V602GMSSo0Y")


movies = [
    lone_survivor, adrift, ratatouille,
    big_hero_6, age_of_adaline,
    me_before_you, kingsman,
    mission_impossible, camp_xray]

fresh_tomatoes.open_movies_page(movies)
