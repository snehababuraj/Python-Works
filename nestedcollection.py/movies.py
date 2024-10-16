movies=[

    {
        "title": "Bad Asses on the Bayou",
        "year": 2015,
        "cast": [
            "Danny Trejo",
            "Danny Glover",
            "John Amos",
            "Loni Love"
        ],
        "genres": [
            "Action"
        ]
    },
    {
        "title": "Chappie",
        "year": 2015,
        "cast": [
            "Sharlto Copley",
            "Dev Patel",
            "Watkin Tudor Jones",
            "Yolandi Visser"
        ],
        "genres": [
            "Science Fiction"
        ]
    },
    {
        "title": "Road Hard",
        "year": 2015,
        "cast": [
            "Adam Carolla",
            "David Koechner",
            "Diane Farr",
            "Jay Mohr",
            "David Alan Grier"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "The Second Best Exotic Marigold Hotel",
        "year": 2015,
        "cast": [
            "Judi Dench",
            "Maggie Smith",
            "Bill Nighy"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Unfinished Business",
        "year": 2015,
        "cast": [
            "Vince Vaughn",
            "Dave Franco",
            "Sienna Miller",
            "Nick Frost"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "Cinderella",
        "year": 2015,
        "cast": [
            "Lily James",
            "Richard Madden",
            "Cate Blanchett",
            "Helena Bonham Carter",
            "Holliday Grainger"
        ],
        "genres": [
            "Romance"
        ]
    },
    {
        "title": "The Cobbler",
        "year": 2015,
        "cast": [
            "Adam Sandler",
            "Dustin Hoffman",
            "Dan Stevens",
            "Steve Buscemi"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Cymbeline",
        "year": 2015,
        "cast": [
            "Ed Harris",
            "Milla Jovovich",
            "Ethan Hawke",
            "John Leguizamo"
        ],
        "genres": [
            "Crime"
        ]
    },
    {
        "title": "Home Sweet Hell",
        "year": 2015,
        "cast": [
            "Patrick Wilson",
            "Katherine Heigl",
            "Jordana Brewster",
            "Jim Belushi",
            "Daniel Zovatto"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "It Follows",
        "year": 2015,
        "cast": [
            "Maika Monroe",
            "Keir Gilchrist",
            "Jake Weary",
            "Daniel Zovatto"
        ],
        "genres": [
            "Horror"
        ]
    }
]


#q1 total
#print(len(movies))

#q2 print movie names
movie_names=[n.get("title") for n in movies ]
#print(movie_names)

#q3  print movies with genres horror

comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
#print(comedy_movies)
#q comdey,drama
comdey_drama_movies=[ m.get("title")for m in movies if "Comedy" in m.get("genres") or "Drama" in m.get("genres")]
#print(comdey_drama_movies)

comdey_drama_movies=[ m.get("title")for m in movies if "Comedy" in m.get("genres") and "Drama" in m.get("genres")]
#print(comdey_drama_movies)


#q4 print genres of all movie title:genres
#movie=[m.get("title") for m in movies ]
#wc={g:movie.get("genres") for g in set(movie)}
#print(wc)


#q5 print the cast of particular movie

film_cast=[m.get("cast")for m in movies if m.get("title")=="It Follows"]
#print(film_cast)

#q6 year
#year=[m.get("title")for m in movies if m.get("year")==2015]
#print(year)

#qq
actors=[]
for m in movies:
    for a in m.get("cast"):
        actors.append(a)
print(actors)
wc={a:actors.count(a) for a in set(actors)}
print(wc)

for k,v in wc.items():
    if v>1:
       print(k)

