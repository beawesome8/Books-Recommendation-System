from flask import Flask, render_template, request
import numpy as np
import pickle 

popular_books = pickle.load(open('popular_books.pkl','rb'))
pivot_table = pickle.load(open('pivot_table.pkl','rb'))
books_df = pickle.load(open('books_df.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))
#creating an object of the Flask Class
app = Flask(__name__)

# link  - http://127.0.0.1:5000/

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_books['Book-Title'].values),
                           author = list(popular_books['Book-Author'].values),
                           image = list(popular_books['Image-URL-M'].values),
                           votes = list(popular_books['Number of Ratings'].values),
                           rating = list(popular_books['Average of Ratings'].values),
                           
                          )
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods = ['post'])
def recommend():
    user_input = request.form.get('user_input')
    
    book_index = np.where(pivot_table.index == user_input)[0][0]
    #Fetching the simmilarity scores of the book in a sorted descedning list and excludinng the first index as it is the book itself
    similar_items = sorted(list(enumerate(similarity_scores[book_index])), key = lambda x: x[1], reverse = True)[1:5]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books_df[books_df['Book-Title'] == pivot_table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
       
    print(data)
     
    return render_template('recommend.html', data = data)
if __name__ == '__main__':
    app.run(debug=True)