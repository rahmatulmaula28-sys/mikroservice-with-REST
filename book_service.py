from flask import Flask, jsonify

app = Flask(__name__)

# Database khusus Book Service
books = [
    {
        "id": 1,
        "title": "Belajar Flask",
        "stock": 5
    }
]


# =========================
# GET SEMUA BUKU
# =========================
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# =========================
# GET BUKU BERDASARKAN ID
# =========================
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for b in books:
        if b['id'] == book_id:
            return jsonify(b)

    return jsonify({
        "error": "Not found"
    }), 404


# =========================
# MENJALANKAN SERVICE
# =========================
if __name__ == '__main__':
    # Book Service berjalan pada port 5001
    app.run(port=5001, debug=True)