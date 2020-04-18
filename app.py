# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie(movie_list):
    # You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movie_list.append({
        'title': title,
        'director': director,
        'year': year
    })

    return None


# Create other functions for:
#   - listing movies
def list_movies(movie_list):
    print(f"Movie collection has {len(movie_list)} movies")
    for movie in movie_list:
        print(f"Title {movie['title']}", f"Director {movie['director']}", f"Year {movie['year']}", sep=', ')

    return None


#   - finding movies
def find_movie(movie_list):
    movie_title = input("Enter the movie title you want to find: ")

    for movie in movie_list:
        if movie['title'].lower() == movie_title.lower():
            print("Find the movie!")
            print(f"Title {movie['title']}", f"Director {movie['director']}", f"Year {movie['year']}", sep=', ')
            break
    else:
        print(f"Cannot find the movie {movie_title}")

    return None


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie(movies)
    elif selection == "l":
        list_movies(movies)
    elif selection == "f":
        find_movie(movies)
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)

# Remember to run the user menu function at the end!
