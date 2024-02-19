# Book-Rest-API-Project.py
The Bookstore API is a Flask-based web service designed to serve as a virtual bookstore, allowing users to browse available books, retrieve specific book details, add new books, update existing book information, and delete books from the inventory. The API provides simple yet essential endpoints for interacting with book data via HTTP requests.

![Screenshot 2024-02-19 113834](https://github.com/AmandaEvola/Book-Rest-API-Project.py/assets/92234152/f944fa9b-d414-4d63-aeec-a45b464fdd1d)

![Screenshot 2024-02-19 113906](https://github.com/AmandaEvola/Book-Rest-API-Project.py/assets/92234152/7865454f-62b5-41fb-82d7-c34d1026e729)

![Screenshot 2024-02-19 113933](https://github.com/AmandaEvola/Book-Rest-API-Project.py/assets/92234152/5d38ee5a-8898-4eaa-a453-192b9d843bdf)

![Screenshot 2024-02-19 113316](https://github.com/AmandaEvola/Book-Rest-API-Project.py/assets/92234152/1597b49f-6e39-4a20-97ef-12ea541195d9)


# Key Features
- Retrieve a list of available books with details such as title, author, and image.
- Add, update, and delete books from the inventory.
- Flexible endpoints for interacting with book data via HTTP requests.

# Technologies used 
- Flask
- JSON (JavaScript Object Notation)
- HTTP Methods (GET, POST, PUT, DELETE)

# Installation
1. Clone the repository to your local machine: git clone https://github.com/yourusername/bookstore-api.git
2. Navigate to the project directory: cd bookstore-api
3. Install dependencies: pip install -r requirements.txt

# Usage 
1. Run the Flask application: python app.py
2. Access the API endpoints using HTTP requests. See Endpoints Documentation for details.

# Endpoints Documentation 
## Get/books
Retrieve a list of all books in the bookstore.
### Response: 
        
  {
  "books": [
    {
      "id": 1,
      "title": "Pride and Prejudice",
      "author": "Jane Austen",
      "image_url": "https://example.com/pride_and_prejudice.jpg",
      "book_name": "Pride and Prejudice"
    },
    // Additional books...
  ]
}

## GET /books/{book_id}
Retrieve details of a specific book by ID.

### Response: 
{
  "book": {
    "id": 1,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "image_url": "https://example.com/pride_and_prejudice.jpg",
    "book_name": "Pride and Prejudice"
  }
}

## POST /books
Create a new book entry.

### Request body:
{
  "title": "New Book Title",
  "author": "Author Name",
  "image_url": "https://example.com/new_book.jpg",
  "book_name": "New Book"
}

### Response:

{
  "message": "Book created",
  "book": {
    "id": 5,
    "title": "New Book Title",
    "author": "Author Name",
    "image_url": "https://example.com/new_book.jpg",
    "book_name": "New Book"
  }
}
## PUT /books/{book_id}
Update details of an existing book.
### Request body: 
Same as POST /books

### Response: 
Same as POST /books

## DELETE/books/{book_id}
Delete a book from the inventory.

### Response: 
{
  "message": "Book deleted",
  "book": {
    "id": 5,
    "title": "New Book Title",
    "author": "Author Name",
    "image_url": "https://example.com/new_book.jpg",
    "book_name": "New Book"
  }
}

# Contributing 
Contributions to the Bookstore API are welcome! Please see the contribution guidelines for details.

# License
This project is licensed under the MIT License. 

# Code of conduct
As contributors and maintainers of the Bookstore API project, we are committed to fostering an inclusive and respectful community. We value the participation of every individual and encourage open and constructive communication.

## Our Pledge
In the interest of promoting an open and welcoming environment, we pledge to:

- Be respectful and considerate of differing viewpoints and experiences.
- Welcome contributions from people of all backgrounds and identities.
- Be mindful of our language and behavior, and avoid any form of harassment, discrimination, or disrespectful conduct.
- Support each other in our efforts to learn, grow, and improve the Bookstore API project.

  ## Our standards
  To ensure a positive and productive community experience, we expect all participants to adhere to the following standards:

- Communicate respectfully and professionally, both online and in-person interactions.
- Accept constructive feedback graciously and strive to improve based on it.
- Refrain from engaging in any form of harassment, discrimination, or offensive behavior.
- Be inclusive and considerate of diverse perspectives and experiences.
- Respect the privacy and personal boundaries of others.

  ## Enforcement
  Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting me directly (if you know me personally you should know what my info is).

  ## Attribution
  This Code of Conduct is adapted from the Contributor Covenant, version 2.0, available at https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

  ## Thank you
  We appreciate your commitment to creating a welcoming and inclusive community environment. Together, we can build and maintain a positive and supportive community around the Bookstore 
  API project.

  


