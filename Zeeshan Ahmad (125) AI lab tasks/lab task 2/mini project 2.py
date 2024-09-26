movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def get_average_budget(movies):
    total_budget = sum(budget for _, budget in movies)
    return total_budget / len(movies)

def find_high_budget_movies(movies, average_budget):
    high_budget_movies = [(name, budget, budget - average_budget) for name, budget in movies if budget > average_budget]
    return high_budget_movies

def add_movies(movies):
    num_movies = int(input("How many movies do you want to add? "))
    for _ in range(num_movies):
        name = input("Enter movie name: ")
        budget = int(input("Enter movie budget: "))
        movies.append((name, budget))

def main():
    add_movies(movies)
    average_budget = get_average_budget(movies)
    print(f"Average budget: {average_budget}")
    
    high_budget_movies = find_high_budget_movies(movies, average_budget)
    for name, budget, difference in high_budget_movies:
        print(f"{name} had a budget {difference} higher than the average")
    
    print(f"Total number of movies above the average budget: {len(high_budget_movies)}")

main()
