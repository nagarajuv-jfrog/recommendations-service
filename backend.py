import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# The recommendations service has its own list of 6 potential books to recommend.
# In a real-world scenario, this could be powered by a more complex algorithm.
recommendable_books = [
    { "id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "description": "A classic of modern American literature.", "stock": 5, "price": 12.99, "image": "https://placehold.co/300x450/a3bfb8/ffffff?text=To+Kill+a+Mockingbird" },
    { "id": 2, "title": "1984", "author": "George Orwell", "description": "A dystopian novel set in a totalitarian society.", "stock": 8, "price": 10.99, "image": "https://placehold.co/300x450/f0a3a3/ffffff?text=1984" },
    { "id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "A story of the fabulously wealthy Jay Gatsby.", "stock": 3, "price": 9.99, "image": "https://placehold.co/300x450/f7e1a3/ffffff?text=The+Great+Gatsby" },
    { "id": 4, "title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "A fantasy novel and prelude to The Lord of the Rings.", "stock": 12, "price": 14.99, "image": "https://placehold.co/300x450/a3f7a3/ffffff?text=The+Hobbit" },
    { "id": 5, "title": "Fahrenheit 451", "author": "Ray Bradbury", "description": "A dystopian novel where books are outlawed.", "stock": 6, "price": 10.00, "image": "https://placehold.co/300x450/f7a3a3/ffffff?text=Fahrenheit+451" },
    { "id": 11, "title": "Brave New World", "author": "Aldous Huxley", "description": "A dystopian novel which anticipates developments in reproductive technology.", "stock": 5, "price": 11.99, "image": "https://placehold.co/300x450/f0b0f0/ffffff?text=Brave+New+World" }
]

@app.route('/api/recommendation', methods=['GET'])
def get_recommendation():
    """
    API endpoint to get a single random book recommendation.
    """
    recommended_book = random.choice(recommendable_books)
    return jsonify(recommended_book)

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)