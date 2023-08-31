# Book Recommendations App using GPT-4

This streamlit app uses OpenAI's GPT-4 model to provide the user with book recommendations based on three of their favorite books. I read a lot and recently created a Django app that automates certain Goodreads tasks such as fetching a user's goodreads recommendations from their profile. However I noticed that these recommendations weren't very good so I decided to try and make something that would provide more high quality book recommendations.
</br>
Part of the problem with Goodreads' recommendations is that it seems to overweight books recently added to the profile and doesn't consider which books are most important to the user.
</br>
Therefore in this approach, the recommendations are only based off of a user's top 3 favorite books.
</br>
I used Langchain and Streamlit to create this project.
</br>
In the demo I inputed some of my favorite books (I have a hard time picking just 3) and as it turns out the recommended books are all books I have read before and enjoyed. This tool also provides an explanation for the recommendations and shows how they connect to the three favorites. One downside is that since the model is not aware of which books a person has already read, they may end up recommending books that aren't new (as was the case in my example).

## Video Demo:
