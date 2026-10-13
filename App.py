from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Library database containing 10 books
books = [
    {
        "id": "B001",
        "name": "Java Programming",
        "author": "Herbert Schildt",
        "department": "CSE/ISE",
        "copies": 3
    },
    {
        "id": "B002",
        "name": "Database Management Systems",
        "author": "Korth",
        "department": "CSE/ISE",
        "copies": 2
    },
    {
        "id": "B003",
        "name": "Computer Networks",
        "author": "Andrew S. Tanenbaum",
        "department": "CSE/ISE",
        "copies": 4
    },
    {
        "id": "B004",
        "name": "Operating System Concepts",
        "author": "Silberschatz",
        "department": "CSE/ISE",
        "copies": 1
    },
    {
        "id": "B005",
        "name": "Data Structures",
        "author": "Seymour Lipschutz",
        "department": "CSE/ISE",
        "copies": 3
    },
    {
        "id": "B006",
        "name": "Software Engineering",
        "author": "Ian Sommerville",
        "department": "ISE",
        "copies": 2
    },
    {
        "id": "B007",
        "name": "Python Programming",
        "author": "Mark Lutz",
        "department": "CSE/ISE",
        "copies": 5
    },
    {
        "id": "B008",
        "name": "Machine Learning",
        "author": "Tom M. Mitchell",
        "department": "CSE/ISE",
        "copies": 2
    },
    {
        "id": "B009",
        "name": "Web Technology",
        "author": "Uttam K. Roy",
        "department": "ISE",
        "copies": 3
    },
    {
        "id": "B010",
        "name": "Computer Graphics",
        "author": "Donald D. Hearn",
        "department": "CSE/ISE",
        "copies": 1
    }
]


# Display the website
@app.route("/")
def home():
    return render_template("index.html", books=books)


# Search books and answer chatbot questions
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message", "").strip().lower()

    if not message:
        return jsonify({"reply": "Please enter a question."})

    if "show all books" in message or "list all books" in message:
        return jsonify({
            "reply": "Here are all 10 books in the library.",
            "books": books
        })

    results = []

    # Find matching books
    for book in books:
        if (
            message == book["id"].lower()
            or message in book["name"].lower()
            or message in book["author"].lower()
        ):
            results.append(book)

    if results:

        replies = []

        for book in results:
            status = (
                "Available"
                if book["copies"] > 0
                else "Not available"
            )

            replies.append(
                f"Book: {book['name']}\n"
                f"Book ID: {book['id']}\n"
                f"Author: {book['author']}\n"
                f"Department: {book['department']}\n"
                f"Available copies: {book['copies']}\n"
                f"Status: {status}"
            )

        return jsonify({"reply": "\n\n".join(replies)})

    return jsonify({
        "reply": (
            "Sorry, I couldn't find that book. "
            "Try searching by book name, author, or book ID."
        )
    })


if __name__ == "__main__":
    app.run(debug=True)