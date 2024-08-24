from django.http import JsonResponse

# View to return a list of movies
def movie_list(request):
    movies = [
        {"id": 1, "title": "Inception", "genre": "Science Fiction", "year": 2010},
        {"id": 2, "title": "The Shawshank Redemption", "genre": "Drama", "year": 1994},
        {"id": 3, "title": "The Dark Knight", "genre": "Action", "year": 2008},
    ]
    return JsonResponse(movies, safe=False)

# View to return details of a specific movie
def movie_detail(request, movie_id):
    movie_details = {
        1: {"id": 1, "title": "Inception", "genre": "Science Fiction", "year": 2010, "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO."},
        2: {"id": 2, "title": "The Shawshank Redemption", "genre": "Drama", "year": 1994, "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
        3: {"id": 3, "title": "The Dark Knight", "genre": "Action", "year": 2008, "description": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice."},
    }
    movie = movie_details.get(movie_id, {"error": "Movie not found"})
    return JsonResponse(movie)