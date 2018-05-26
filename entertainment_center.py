import fresh_tomatoes
import media

lone_survivor = media.Movie("Lone Suvivor",
                            "Lone Survivor is a 2013 American biographical war thriller film based on the 2007 eponymous non-fiction book",  # NOQA
                            "https://movieposters2.com/images/1301381-b.jpg",
                            "https://youtu.be/yoLFk4JK_RM")


adrift = media.Movie("Adrift",
                     "Story of 2 avid sailors setting out on a journey across the ocean, meets a catastrophic hurricanes in recorded history.",  # NOQA
                     "https://ia.media-imdb.com/images/M/MV5BMTkxMTI2MjE4OF5BMl5BanBnXkFtZTgwMjIyODQzNTM@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                     "https://youtu.be/n9ukI7khQpE")


ratatouille = media.Movie("Ratatouille",
                          "Remy dreams of becoming a great chef, despite being a rat in a definitely rodent-phobic profession.",  # NOQA
                          "https://i.pinimg.com/564x/02/d9/1f/02d91f8899c03a2bf656e0b197753b7f.jpg",  # NOQA
                          "https://youtu.be/uVeNEbh3A4U")


big_hero_6 = media.Movie("Big Hero 6",
                         "Determined to uncover the mystery, Hiro transforms his friends into a band of high-tech heroes called Big Hero 6",  # NOQA
                         "https://imgix.ttcdn.co/i/product/original/0/538386-1967ef50199e4051bac86bd45bab7ccf.jpeg?q=100&auto=format%2Ccompress&w=500",  # NOQA
                         "https://youtu.be/z3biFxZIJOQ")


age_of_adaline = media.Movie("Age Of Adaline",
                             "Adaline Bowman has miraculously remained a youthful 29 years of age for nearly eight decades, and hides her secret",  # NOQA
                             "http://broadcast-everywhere.net/wp-content/uploads/2016/02/Matinee-Movie-The-Age-of-Adaline-PWPL-February-4th.jpg",  # NOQA
                             "https://youtu.be/7UzSekc0LoQ")


me_before_you = media.Movie("Me Before You",
                            "Young and quirky Louisa, is put to the test when she becomes a caregiver for Will Traynoraccident.",  # NOQA
                            "http://images6.fanpop.com/image/photos/40000000/Me-Before-You-Movie-Poster-movie-trailers-40097762-380-500.jpg",  # NOQA
                            "https://youtu.be/Eh993__rOxA")


kingsman = media.Movie("Kingsman: The Golden Circle",
                       "It's James Bond On Laughing Gas.",
                       "https://20ui41tp7v127j03rcnp97oh-wpengine.netdna-ssl.com/wp-content/uploads/2018/04/sabado_kingsman.jpg",  # NOQA
                       "https://youtu.be/6Nxc-3WpMbg")


mission_impossible = media.Movie("Mission Impossible: Rogue Nation",
                                 "With the IMF now disbanded and Ethan Hunt out in the cold, a new threat - called the Syndicate - soon emerges",  # NOQA
                                 "https://images-na.ssl-images-amazon.com/images/I/91PAjeQr62L._SY445_.jpg",  # NOQA
                                 "https://youtu.be/pXwaKB7YOjw")


camp_xray = media.Movie("Camp X Ray",
                        "A female guard at Guantanamo Bay forms an unlikely friendship with one of the facility's longtime detainees.",  # NOQA
                        "https://i.pinimg.com/originals/12/bb/f3/12bbf3b84f216643bf5a836b8f13b9f6.jpg",  # NOQA
                        "https://youtu.be/V602GMSSo0Y")  # NOQA


movies = [lone_survivor, adrift, ratatouille, big_hero_6, age_of_adaline, me_before_you, kingsman, mission_impossible, camp_xray]  # NOQA

fresh_tomatoes.open_movies_page(movies)
