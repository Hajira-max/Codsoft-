# 🎬📚  Recommendation system

# Predefined recommendations for books and movies by genre
recommendations = {
    "books": {
        "fantasy": ["Harry Potter by J.K. Rowling", "The Hobbit by J.R.R. Tolkien", "Percy Jackson by Rick Riordan"],
        "mystery": ["The Da Vinci Code by Dan Brown", "Gone Girl by Gillian Flynn", "Sherlock Holmes by Arthur Conan Doyle"],
        "romance": ["Pride and Prejudice by Jane Austen", "Me Before You by Jojo Moyes", "The Notebook by Nicholas Sparks"],
        "sci-fi": ["Dune by Frank Herbert", "Ender’s Game by Orson Scott Card", "Neuromancer by William Gibson"]
    },
    "movies": {
        "fantasy": ["The Lord of the Rings", "Harry Potter", "Pan’s Labyrinth"],
        "mystery": ["Shutter Island", "Se7en", "The Girl with the Dragon Tattoo"],
        "romance": ["Titanic", "La La Land", "The Fault in Our Stars"],
        "sci-fi": ["Interstellar", "Inception", "The Matrix"]
    }
}

def recommend():
    print("👋 Welcome to the Recommendation System!")
    print("Type 'exit' anytime to quit.\n")

    while True:
        choice = input("Would you like recommendations for 'books' or 'movies'? ").strip().lower()

        # Exit option
        if choice in ["exit", "quit"]:
            print("👋 Goodbye! Hope you enjoy the recommendations!")
            break

        if choice not in recommendations:
            print("❌ Sorry, I can only recommend 'books' or 'movies'. Try again.\n")
            continue

        genre = input("Great! Now tell me the genre (fantasy, mystery, romance, sci-fi): ").strip().lower()

        if genre in ["exit", "quit"]:
            print("👋 Goodbye! Hope you enjoy the recommendations!")
            break

        if genre not in recommendations[choice]:
            print("❌ Sorry, I don’t have recommendations for that genre. Try again.\n")
            continue

        # Show recommendations
        print(f"\n✨ Here are some {choice} I recommend in the {genre.title()} genre:")
        for item in recommendations[choice][genre]:
            print(f"👉 {item}")
        print("\n---\n")

# Run the recommendation system
if __name__ == "__main__":
    recommend()
     
