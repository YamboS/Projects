import time
import spotipy
import numpy as np
import Reccomender
import RelativeDiversity
import linecache
import sys
import pyinputplus as pyip
from joblib import load
from sklearn import tree


class userInfo:


    def __init__(self , sp):
        self.relative_diversity=RelativeDiversity.relative_diversity()
        self.sp = sp
        self.playlistId = None
        self.name = None
        self.link = None
        self.searchLVL = None
        self.artist = None
        self.song = None
        self.genre = None
        self.addSongsList = []
    
    def getPlaylistInfo(self):
        try:
            text = input('Enter the playlist link here\n')
            self.link, self.playlistId = text.split("playlist/")
            
        except Exception as e:
            userObj.printException()

    def setUserPlaylistInfo(self):
        self.name = input('Input the name of the playlist\nName of playlist:')

    def userHasPlaylist(self):

        flag = pyip.inputInt(prompt='Welcome to playlist reccomender \nTo create a playlist enter (0)\nTo add to your existing playlist enter (1)\n',min=0,lessThan=2)
        if flag==1:
            self.getPlaylistInfo()
        elif flag==0:
            self.setUserPlaylistInfo()

    def printException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

    def getSearchlvl(self):
        self.searchLVL = pyip.inputNum('Please enter your level of search(1-3)\n(1) shallow search\n(3) deep search\n', min=1, lessThan=4)
        if self.searchLVL >= 4:
            self.searchLVL = 3

    def findSong(self):
        try:
            song_name = input('Please enter a song and the artist\'s name\n\n')
            results = self.sp.search(q=song_name, type='track,artist')
            index=self.selectSong(results)

            self.artist = results['tracks']['items'][index]['artists'][0]['uri']
            self.song = results['tracks']['items'][index]['uri']
            self.genre = self.sp.artist(results['tracks']['items'][index]['artists'][0]['uri'])
        except Exception as e:
            userObj.printException()
            print("You did not enter a song or there were no results for your search")

    def selectSong(self,results):

        index = 0
        for row in results['tracks']['items']:
            print(index, row['artists'][0]['name'], row['name'])
            index += 1

        index=pyip.inputInt(prompt='Please enter the number next to the song you want to choose\n',min=0,max=index)
        return index

    def showResults(self,songNames,rec):
        print('Songs and their Similarity score in comparison to the song you put in\n\n\n')
        tree = load('model.joblib')
        for x in range(15):
            songArray = np.array(rec.finalSongSelect[x][2])
            if tree.predict([songArray]):
                self.addSongsList.append(rec.finalSongSelect[x][1])
                print(songNames['tracks'][x]['artists'][0]['name'], '-', songNames['tracks'][x]['name'],
                      rec.finalSongSelect[x][0])
        self.addSongsList = list(set(self.addSongsList))
        self.addSongsList = self.relative_diversity.final_song_pick(sp.tracks(self.addSongsList))

    def createUserPlaylist(self):
         if self.playlistId==None:
             playlist_name = sp.user_playlist_create(rec.username, self.name)
             self.playlistId = playlist_name['id']

    def addSongsToPlaylist(self):
        self.sp.playlist_add_items(playlist_id=self.playlistId, items=self.addSongsList)

rec = Reccomender.reccomender()

sp = spotipy.Spotify(auth_manager=spotipy.SpotifyPKCE(rec.SPOTIPY_CLIENT_ID, rec.SPOTIPY_REDIRECT_URI, rec.username, scope=rec.scope,open_browser=False))

rec.setSpotifyObj(sp)

userObj = userInfo(sp)

userObj.userHasPlaylist()
while 1:
    try:
        userObj.findSong()

        rec.seedSong = userObj.song


        response=pyip.inputInt(prompt="Would you like to manually set the artist seed for this playlist?\nYes (1)\nNo (0)\n",min=0,max=1)
        if response==1:
            profileUrl=input("Enter the url of the artist profile: ")
            rec.setArtist(profileUrl)
            rec.genre=set()
        else:
            rec.artist.append(userObj.artist)
            rec.genre = set(userObj.genre['genres'])


        userObj.getSearchlvl()

        start_time = time.time()

        rec.searchForRelatedArtist(userObj.searchLVL)

        rec.getRelatedArtistSongs(rec.artist)

        rec.getSongFeats(rec.seedSong)

        rec.finalSongSelect.sort(key=lambda x: x[0], reverse=True)

        songNames = np.array(rec.finalSongSelect,dtype=object)

        songNames = sp.tracks(songNames[:50, 1])

        userObj.showResults(songNames,rec)

        userObj.createUserPlaylist()

        userObj.addSongsToPlaylist()

        print("--- %s seconds ---" % (time.time() - start_time))
        exit = input("If you would like to add another song enter 'y' or press enter\n")

        if exit.lower() == 'y':
            userObj.addSongsList.clear()
            rec.clear()
            continue
        else:
            print('\nHere is your playlist link \nhttps://open.spotify.com/playlist/' + userObj.playlistId)
            break
    except:
        print("Something went wrong along the way")
        userObj.printException()
