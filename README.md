# Book Recommendations App using GPT-4

This app uses OpenAI's GPT-4 model to provide the user with book recommendations based on three of their favorite books. I read a lot and recently created a Django app that automates certain Goodreads tasks such as fetching a user's Goodreads recommendations from their profile. However I noticed that these recommendations weren't very good so I decided to try and make something that would provide more high quality book recommendations.
</br>
</br>
Part of the problem with Goodreads' recommendations is that it seems to overweight books recently added to the profile and doesn't consider which books are most important to the user.
</br>
</br>
In this approach, the recommendations are only based on a user's top 3 favorite books.
</br>
</br>
I used Langchain and Streamlit to create this project.
</br>
</br>
In the demo I inputed three of my favorite books. As it turns out the recommended books are all books I have read before and enjoyed. This tool also provides an explanation for the recommendations and shows how they connect to the three favorites. In my opinion, the explanations and connections between the recommended and favorite books are fairly accurate. One downside is that since the model is not aware of which books a person has already read, they may end up recommending books that aren't new (as was the case in my example).

## Video Demo:

https://github.com/tarabogavelli/book_rec_streamlit_app/assets/87334044/f5d28afa-05f3-4dee-8ebe-72149cbe01c5

</br>
<img width="760" alt="Screenshot 2023-08-31 at 12 05 43 AM" src="https://github.com/tarabogavelli/book_rec_streamlit_app/assets/87334044/3639d945-ccbd-421a-b7e2-25538c99acb1">
<img width="777" alt="Screenshot 2023-08-31 at 12 05 57 AM" src="https://github.com/tarabogavelli/book_rec_streamlit_app/assets/87334044/8f5ed994-145b-4f4e-a6f4-d7d68f59fb6c">

 

