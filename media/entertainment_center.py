import fresh_tomatoes
import media

# Creating a function with all the instance variables required
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy that come to life",
                        "https://i.ytimg.com/vi/8gL2nKAa9Q8/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )
avatar = media.Movie("Avatar",
                     "A marine goes to alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY" )
Jason_Bourne5 = media.Movie("Jason Bourne5",
                     "CIA operator taking revenge",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcQ27a64TqUZLOU1QbJiBPhu4mBZMW50wFzR62ob5W9o9Mgx7blK", # NOQA
                     "https://www.youtube.com/watch?v=HOQh9KwJqwg" )
inception = media.Movie("inception",
                     "Dream with in a dream",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD", # NOQA
                     "https://www.youtube.com/watch?v=8hP9D6kZseM" )
Jungle_book = media.Movie("Jungle Book",
                     "Life of a boy in the jungle.",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcQgNaB5wtt0G7_mTFVygkFtmjWut_Z0QSz2GzDsHeiZDHno4fjh",# NOQA
                     "https://www.youtube.com/watch?v=5mkm22yO-bs" )
Departed = media.Movie("Departed",
                     "A story of spy",
                     "http://static.rogerebert.com/uploads/movie/movie_poster/the-departed-2007/large_tGLO9zw5ZtCeyyEWgbYGgsFxC6i.jpg", #NOQA
                     "https://www.youtube.com/watch?v=iojhqm0JTW4" )
# Creating an array of the movies choosen
movies = [toy_story, avatar, Jason_Bourne5, inception, Jungle_book, Departed]
# Creats a HTML page that opens and shows the trailer of that movie
fresh_tomatoes.open_movies_page(movies)
