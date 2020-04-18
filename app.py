# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    # You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

    return None


# Create other functions for:
#   - listing movies
def list_movies():
    print(f"Movie collection has {len(movies)} movies")
    for movie in movies:
        print(f"Title {movie['title']}", f"Director {movie['director']}", f"Year {movie['year']}", sep=', ')

    return None


#   - finding movies
def find_movie():
    movie_title = input("Enter the movie title you want to find: ")

    for movie in movies:
        if movie['title'].lower() == movie_title.lower():
            print("Find the movie!")
            print(f"Title {movie['title']}", f"Director {movie['director']}", f"Year {movie['year']}", sep=', ')
            break
    else:
        print(f"Cannot find the movie {movie_title}")

    return None


user_operations = {
    'a': add_movie,
    'l': list_movies,
    'f': find_movie
}

# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection in user_operations:
        operation = user_operations[selection]
        operation()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)

# Remember to run the user menu function at the end!
