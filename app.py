import streamlit as st
import pickle
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(layout='wide')

# Define a function that creates a link to your index.html file
def create_link():
    components.html("""
<html>
<style>
h1{color:white; font-size: 50px;}
p#new{color: white; font-family: cursive;}
p#span{color: red; font-size: 15px;font-family: cursive;}
h2{color: yellow;}
</style>
<body>
<h1>Welcome To The Book Recommender System.</h1>
<p id = "new">The Book Recommender System makes use of Genre to suggest you the Book Titles Similar to the Genre. This book recommender is useful when you like a book of a particular genre and are more interested in reading books of similar Genre.<br></p>
<p id = "span">SOMETIMES YOU MIGHT SEE ONE BOOK BEING RECOMMENDED MORE THAN ONCE. WELL WORRY NOT!! THIS AIN'T THE SYSTEM'S ERROR. IT IS JUST TO SHOW THE USER THAT MORE THE NUMBER OF TIMES A BOOK IS REPEATED, THE MORE POPULAR IT IS!!</p> 
<h2>Do Check Out the Top 50 Books Currently Trending in the Year 2023 By Clicking Below.</h2>
</body>
</html>
""", width=1080, height=230)
    link = """<a href="index_html.html" target="_blank" style="color: white; text-decoration: none; font-size: 40px;">Check Out The Top 50 Books</a>"""
    return link

# Display the link in your Streamlit app using the html component
st.components.v1.html(create_link(), height=70)

def recommend(genre):
    if books[books['genre']==genre].empty:
        print("No books found for genre:", genre)
        return []
    genre_index = books[books['genre']==genre].index[0]
    distances = similarity[genre_index]
    genre_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])[1:15]
    recommended_books = []
    for i in genre_list:
        book = books.iloc[i[0]]
        recommended_books.append(f"{book.title} || The Genre of this book is: [{book.genre}]")
    return recommended_books


# Rest of the code remains the same

similarity = pickle.load(open('similarity.pkl','rb'))

books_list = pickle.load(open('books_latest.pkl','rb'))

books = pd.DataFrame(books_list)

st.title("Book Recommender System")

selected_books_option = st.selectbox(
    "Which genre you want?", books['genre'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_books_option)
    for i in recommendations:
        st.write(i)
