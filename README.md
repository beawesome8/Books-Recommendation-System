# Books-Recommendation-System
This is a personalized book recommendation system built using Flask, Pandas, numpy, sci-kit learn, HTML and bootstrap. A collaborative filtering approach is used for this recommendations system. The app recommends the top 50 rated books and can provide the user with recommendations of books that are similar, using cosine similarity, to what the user has entered or input in the search bar.

## Features
- Recommends books based on user input
- Displays top 50 books with their details including title, author, image, number of ratings, and average rating

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/Books-Recommendation-System.git
    cd Books-Recommendation-System
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv MyEnv
    source MyEnv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have created the pickle files**:
    - `popular_books.pkl`
    - `pivot_table.pkl`
    - `books_df.pkl`
    - `similarity_scores.pkl`

    Place these files in the root directory of the project.

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Open your web browser and go to the link that is generated**:
    ```
    http://127.0.0.1:5000/
    ```

3. **Interact with the application**:
    - On the home page, you can see the top 50 books with their details.
    - Navigate to the recommend page to get book recommendations based on user input.
    - Since the recommend page can take inputs only from the book provided in the dataset use the "Books to test the System.txt" file to search for books
    - If any other book that is not present in the dataset is entered, an error is returend which says - "IndexError: index 0 is out of bounds for axis 0 with size 0"


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License and can be used freely.
