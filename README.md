# Book Recommendations App using GPT-4

This streamlit app uses OpenAI's GPT-4 model to provide the user with book recommendations based on three of their favorite books. I read a lot and recently created a Django app that automates certain Goodreads tasks such as fetching a user's goodreads recommendations from their profile. However I noticed that these recommendations weren't very good so I decided to try and make something that would provide more high quality book recommendations.
</br>
</br>
Part of the problem with Goodreads' recommendations is that it seems to overweight books recently added to the profile and doesn't consider which books are most important to the user.
</br>
</br>
Therefore in this approach, the recommendations are only based off of a user's top 3 favorite books.
</br>
</br>
I used Langchain and Streamlit to create this project.
</br>
</br>
In the demo I inputed some of my favorite books (I have a hard time picking just 3) and as it turns out the recommended books are all books I have read before and enjoyed. This tool also provides an explanation for the recommendations and shows how they connect to the three favorites. One downside is that since the model is not aware of which books a person has already read, they may end up recommending books that aren't new (as was the case in my example).

## Video Demo:

https://github.com/tarabogavelli/book_rec_streamlit_app/assets/87334044/f5d28afa-05f3-4dee-8ebe-72149cbe01c5

<img width="787" alt="Screenshot 2023-08-31 at 12 04 27 AM" src="https://github.com/tarabogavelli/book_rec_streamlit_app/assets/87334044/aa26e0ad-dd3a-4e55-bc3a-019222116e27">
<img width="723" alt="Screenshot 2023-08-31 at 12 04 21 AM" src="https://github.com/tarabogavelli/book_rec_streamlit_app/assets/87334044/3b5ae9f0-f2f9-4c78-a8c4-b17b322f9878">

