The following libraries are needed to use this program:Numpy,spotipy


This is my attempt to use some machine learning concepts to find songs that are similar to one inputted by the user 


This can create a playlist or add to an existing playlist that is currently under the user's name 


The area under your personal info needs to be filled out with information that you acquire from spotify developers website
These are the client id and client secret


I have not yet done error checking with this program and is currently still in development but is usable at the moment given the input is valid.
I have attempted to do some sort of crash prevention but have not finished. 
Generally it works as it's supposed to.


A note about predefined values in the code


when calling the "breakdown" function the max should not exceed 4 as this will cause a huge amount of api calls that will likely reach the rate limit before being able to finish executing
Let it also be noted that depending on the song the music gets more unrelated as you increase the level
The predefined weights may be a bit biased but they were a combination of weights that in my opinion produced good results.
That being said feel free to mess around with those to your liking but the total of all of the weights should add up to 1


Lastly in the "similarity" function there is a predefined value on line 70 that I have set to 0.9 for 90% similarity with the similarity function. 
If you were to lower this threshold to say 0.8 the results would change drastically and more songs would be accepted and added to the playlist at the end of the day.
So, if you have issues getting a decent amount of songs you can change this threshold to anywhere above 0.5 or increase max in "breakdown".