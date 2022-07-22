* The following libraries are needed to use this program:Numpy,spotipy
* The area under your personal info needs to be filled out with information that you acquire from spotify developers website
The client id 
------------------------------------------------------------------------------------------------------------------------------------
This is my attempt at a reccomender system based on jaccard similarity using similar artist and their top songs to find songs similar to the one the user input.
This can create a playlist or add to an existing playlist that has been created by the current user.

when using the "breakdown" function the max should not exceed 4 as this will cause a huge amount of api calls that will likely reach the rate limit before being able to finish executing. Also, the amount of time needed for this search is ridiculous.

I decided to just go with uniform weights and reduce some of the attributes instead of using custom weights and more attributes.
Another major change I decided to do was not to base the final selection based on the similarity but by the top K similar songs so there would always be a reccomendation returned. The amount of songs can be changed but currently it is set to 10. Also the songs are listed in order based on the similarity to the song after they are added.

If you have any questions or suggestions feel free to contact me with the header "Spotipy github project" in an email to syambo@yahoo.com.
