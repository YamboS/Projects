import Reccomender
import linecache
import sys
rec = Reccomender.reccomender()


class relative_diversity:

    def __init__(self):
        y = 1 / 8
        self.listOfUri=[]
        self.final_songs = []
        self. weights = [y, y, y, y, y, y, y, y]

    def rel_diversity(self,pop_score, list_of_songs):
        if len(list_of_songs) == 0:
            return 1
        else:
            total = 0
            for song in list_of_songs:
                dif = pop_score - song
                total += abs(dif)
            total /= len(list_of_songs)
            return total


    def quality(self,pop_score, list_of_songs):
        sim = pop_score * 0.50
        rel = self.rel_diversity(pop_score, list_of_songs) * 0.50
        return sim + rel


    def final_song_pick(self,song_list):
       discard=[]
       try:
        while len(self.listOfUri) < 7:
            current_highest_score = 0

            for song in song_list['tracks']:

                popularityScore = self.quality(song["popularity"], self.final_songs)

                if popularityScore > current_highest_score and song not in discard:
                    current_highest_score = popularityScore
                    highest_scoring_song = song
            discard.append(highest_scoring_song)
            self.final_songs.append(highest_scoring_song["popularity"])
            self.listOfUri.append(highest_scoring_song["uri"])


        return self.listOfUri


       except:
           self.printException()

    def printException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
