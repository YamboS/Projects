import spotipy
from spotipy.oauth2 import SpotifyPKCE
import numpy as np
import math
#Created by Samuel S. Yambo 7/11/2022 


np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)


def similarity(a,b,weights):
  '''
  Gets the jaccard similarity of the two objects where custom weights are added  
  '''
  test=np.array(a)
  seed_song=np.array(b)
  results=test-seed_song
  results=np.absolute(results)
  results+=1
  results*=results
  results=1/results
  total=np.dot(results,weights)
  
  return total


def spiderweb(max,list_of_artist,level,results,seed_genres):
  '''
  Desc:This is a recursive function that gets a distinct list of artist that are related to the
  artist from the input song
  
  max: The level you want to search for in an artist
  
  List of artist: The seed artist from the song and eventually the final list of artist at the end
  
  level: The level of search you want to reach
  
  seed_genres: The auto generated genre by spotify for the artist that was inputted
  
  -sidenote:If the artist has no genre the narrowing down process is voided and it will 
  search all possibilities which is exhaustive at a high level


  '''
  if level==max:
    
    return

  else:
    
    for id in list_of_artist:
      
      if id!=None:
        related_artist=sp.artist_related_artists(artist_id=id)
        
        for uri in related_artist['artists']:
          test=set(uri['genres'])
    
          if len(test)>0 and len(seed_genres)>0:
            
            if seed_genres.isdisjoint(test):
              
              continue
            
            else:                               
              
              if uri['uri'] not in results:
                results.append(uri['uri'])
    
          elif len(seed_genres)==0:
            
            if uri['uri'] not in results:
                results.append(uri['uri'])
    
          else:
            
            continue
    
      else:
        
        continue
    
    list_of_artist.extend(results[:])
    return spiderweb(max,artist,level+1,results,seed_genres)




def breakdown(list_of_artist,list_of_songs):
    '''
    Desc: Accepts the artist:uri of the list of related artist 

    list of artist: The list of artist uri related to the seed artist

    List of songs: The list of songs from all related artist   
    
    ''' 
    if len(list_of_artist)<2:
      temp=[]
      for uri in list_of_artist:
        temp.append(sp.artist_top_tracks(artist_id=uri))
      temp=temp[0]
      
      for x in range(len(temp['tracks'])):
        list_of_songs.append(temp['tracks'][x]['uri'])
      return
    
    else:
      half=len(list_of_artist)*0.5
      half=math.ceil(half)
      other_half=half
      breakdown(list_of_artist[:half],list_of_songs)
      breakdown(list_of_artist[other_half:],list_of_songs)




def topk(seed,top_songs,related_songs):
  '''
  
  Desc: This is the function that gets all of the songs and gives them a rating of similarity 
  based off of audio features in the song 

  seed: This is the song inputted program and all of the information regarding it;audio features

  top songs: These are the songs that were the top songs of all the artist related to the seed artist
 
  '''
  
  seed_features=sp.audio_features(seed)
  seed_features=seed_features[0]
  seed_song=np.array([seed_features[attributes[0]],seed_features[attributes[1]],seed_features[attributes[2]],
                      seed_features[attributes[3]],seed_features[attributes[4]],seed_features[attributes[5]],
                      seed_features[attributes[6]]])
  
  weights=[1/7 for x in range(7)]
  length=len(top_songs)
  print("Total scanned songs",length)
  
  rem=length%100
  length=(length-rem)/100
  if rem>0:
    length+=1
  uri=[]
  
  for iter in range(int(length)):
    
    uri=top_songs[:100]
    top_song_features=sp.audio_features(uri)
    del top_songs[:100]
    uri.clear()
    
    #each song in the list of songs 
    for track_info in top_song_features:
      
      try:
        test=np.array([track_info[attributes[0]],track_info[attributes[1]],track_info[attributes[2]],
                       track_info[attributes[3]],track_info[attributes[4]],track_info[attributes[5]],
                       track_info[attributes[6]]])
        total=similarity(seed_song,test,weights)
        related_songs.append([total,track_info['uri'],test])
      
      except:
          pass
  
  
  
  return weights


#--------------------------your info -------------------------------------------

SPOTIPY_CLIENT_ID  = 'your client id'
SPOTIPY_REDIRECT_URI= 'https://google.com/'
username=input("Please input your spotify username\n")
scope = "user-library-read playlist-modify-public playlist-modify-private playlist-read-private"
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyPKCE(SPOTIPY_CLIENT_ID,SPOTIPY_REDIRECT_URI,username,scope=scope,open_browser=False))
attributes=['danceability','energy','instrumentalness','acousticness','valence','tempo','loudness'] 

#-------------------------- main program ---------------------------------------

flag=input("Welcome to the playlist builder that finds similar songs to the ones inputted\n\nEnter 0 to create a new playlist\nEnter 1 to add to an existing playlist you created\n")


try:

  if flag=='0':
    name=input('Input the name of the playlist:')
    playlist_name=sp.user_playlist_create(username,name)
    PlayName=playlist_name['id']
    flag=3

  elif flag=='1':
    text=input('Enter the playlist link here\n')
    link,PlayName=text.split("playlist/")
    flag=3

except:
  print('Invalid entry exiting program')


while flag==3:
  try:
    songs=[[],[]]
    artist=[]
    song_name=input('Please enter a song and the artist\'s name\n\n')
    results=sp.search(q=song_name,type='track,artist')
    index=0
    for row in results['tracks']['items']:
      print(index,row['artists'][0]['name'],row['name'])
      index+=1
    index=int(input("Please enter the number next to the song you want to choose\n"))
    try:
      seed_artist=results['tracks']['items'][index]['artists'][0]['uri']
    except:
      print('Invalid entry or no results found\n')
    else:
      seed_track=results['tracks']['items'][index]['uri']
      x=sp.artist(results['tracks']['items'][index]['artists'][0]['uri'])
      
      artist.append(seed_artist)
      seed_genre=set(x['genres'])
      search=int(input('Please enter your level of search(1-4)\n(1) shallow search\n(4) deep search\n'))
      if search>=5:
        search=4
      spiderweb(max=search,list_of_artist=artist,level=0,results=songs[0],seed_genres=seed_genre)
      
      songs[0].clear()
      breakdown(list(set(artist)),songs[0])
      weights=topk(seed_track,songs[0],songs[1])
      
      songs[1].sort(key=lambda x: x[0],reverse=True)
      song_add=[]
      names=np.array(songs[1])
      names=sp.tracks(names[:50,1])
  
      print('Songs and their similarity score in comparison to the song you put in\n\n\n')
      
      for x in range(10): #This number is the amount of songs you want to add to the playlist
        print(names['tracks'][x]['artists'][0]['name'],'-',names['tracks'][x]['name'],songs[1][x][0])
        song_add.append(songs[1][x][1])
      song_add=list(set(song_add))
      sp.playlist_add_items(playlist_id=PlayName, items=song_add)
      exit=input("If you would like to add another song enter 'y' or press enter\n")
      
      if exit=='y' or exit=='Y':
        song_add.clear()
        pass
      else: break
  except:
    print('Something went wrong exiting program')
    flag=1
    continue

if flag==3:
  print('\nHere is your playlist link \nhttps://open.spotify.com/playlist/'+PlayName)