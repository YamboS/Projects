import numpy as np
import math
import itertools


class reccomender:

    def __init__(self):
        self.username = 'sodiumchloride249'
        self.SPOTIPY_CLIENT_ID = '6b5a19f4d4074723bdafafe34281bb27'
        self.SPOTIPY_REDIRECT_URI = 'https://google.com/'
        self.scope = "user-library-read playlist-modify-public playlist-modify-private playlist-read-private"
        self.attributes = ['danceability', 'acousticness', 'loudness', 'speechiness', 'tempo']
        self.artist = []
        self.finalSongSelect = []
        self.songs = []
        self.recSongFeats = []
        self.seedSong = ""

    def setArtist(self,artist):
        self.artist=[artist]

    def setSpotifyObj(self,sp):
        self.sp=sp
    
    def getSimilarity(self, reccomendedSong, originalSong):
        weights = [1 / len(self.attributes) for i in range(len(self.attributes))]
        recSongFeats = np.array(reccomendedSong)
        orgSongFeats = np.array(originalSong)
        differenceOfRes = recSongFeats - orgSongFeats
        differenceOfRes = np.absolute(differenceOfRes)
        differenceOfRes += 1
        differenceOfRes *= differenceOfRes
        differenceOfRes = 1 / differenceOfRes
        total = np.dot(differenceOfRes, weights)

        return total

    def searchForRelatedArtist(self, levelOfSearch):
        if levelOfSearch == 0:
            return
        else:
            x = len(self.artist)
            for i in range(x):
                self.getRelatedArtist(self.artist[i])
            return self.searchForRelatedArtist(levelOfSearch - 1)

    def getRelatedArtist(self, artistId):
        if id != None:

            related_artist_list = self.sp.artist_related_artists(artist_id=artistId)

            for singleArtistInfo in related_artist_list['artists']:
                recGenre = set(singleArtistInfo['genres'])

                if self.checkGenreAssigned(recGenre):

                    if len(self.genre) >= 1 and self.genre.isdisjoint(recGenre):
                        continue

                    else:
                        self.addArtist(singleArtistInfo['uri'])
        else:
            return

    def checkGenreAssigned(self, recArtistGenre):

        if len(self.genre) == 0:
            return True

        elif len(self.genre) > 0 and len(recArtistGenre) > 0:
            return True

        else:
            return False

    def addArtist(self, artistUri):
        if artistUri not in self.artist:
            self.artist.append(artistUri)

    def getRelatedArtistSongs(self, list_of_artist):

        if len(list_of_artist) < 2:
            temp = []

            for uri in list_of_artist:
                temp.append(self.sp.artist_top_tracks(artist_id=uri))
            temp = temp[0]


            for i in range(len(temp['tracks'])):
                self.songs.append(temp['tracks'][i]['uri'])


        else:
            half = math.ceil(len(list_of_artist) * 0.5)
            other_half = half
            self.getRelatedArtistSongs(list_of_artist[:half])
            self.getRelatedArtistSongs(list_of_artist[other_half:])

    def getSongFeats(self, seed):

        seed_features = self.sp.audio_features(seed)
        seed_features = seed_features[0]
        seed_song = self.createFeatArray(seed_features)
        self.unloadSongs()
        print(len(self.recSongFeats))
        for track_info in self.recSongFeats:
            try:
                recFeats = self.createFeatArray(track_info)
                total = self.getSimilarity(seed_song, recFeats)
                self.finalSongSelect.append([total, track_info['uri'], recFeats])

            except:
                pass

    def createFeatArray(self, featList):
        featObj = []
        for att in self.attributes:
            featObj.append(featList[att])
        return np.array(featObj)

    def unloadSongs(self):

        length = len(self.songs)
        print("Total scanned songs", length)
        for i in range(self.calcRemainder(length)):
            v = i + 1
            temp = self.songs[i * 100:v * 100]
            self.recSongFeats.append(self.sp.audio_features(temp))
            temp.clear()
        self.recSongFeats = self.flatten(self.recSongFeats)

    def calcRemainder(self, iterations):
        rem = iterations % 100
        iterations = (iterations - rem) / 100
        if rem > 0:
            iterations += 1
        return int(iterations)

    def flatten(self, listOflist):
        return list(itertools.chain(*listOflist))

    def clear(self):
        self.artist = []
        self.finalSongSelect = []
        self.songs = []
        self.recSongFeats = []
        self.seedSong = ""
