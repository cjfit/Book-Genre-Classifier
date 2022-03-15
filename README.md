Thanks for checking out my practice book genre problem!

In this exercise we take a JSON-formatted file with key-value pairs of book and description as the first input.
Our second input is a CSV with a genre, a keyword phrase, and a weighted value.

The output to the terminal is each book with its total categorical "average" for each category.

I used Python 3.9.9 to develop this project.

Let's get classifying:
1. Create a new Python 3.9.9 virtual environment or use existing
2. Enter terminal and `pip install pandas numpy` if not installed.
3. Execute from command line by passing the two required args: `python main.py sample_book_data.json sample_genre_keyword_value.csv`

Enjoy! :)

The exercise took me just over three hours to complete.

This was a very interesting challenge to work through. I had to change my approach a few times in the project, particularly around the output sorting approach and electing to not tokenize the book description. This iteration is case-sensitive for keyphrases.

Many of the edge cases I encountered were related to juggling between list comprehension, dictionaries, and Pandas. I tried my best to anticipate these.


