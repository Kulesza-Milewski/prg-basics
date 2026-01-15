# class definition
class Song:
   def __init__(self, artist, track_title, album, year):
      self.artist = artist
      self.track_title = track_title
      self.album = album
      self.year = year

   def __str__(self):
      return f'Song({self.artist}, {self.track_title}, {self.album}, {self.year})'

# object creation
song1 = Song('Ed Sheeran', 'Hearts Dont Break Around Here', 'Divide', 2017)
song2 = Song('Queen', 'Bohemian Rhapsody', 'A Night at the Opera', 1975)

## object usage
print('================')
print(song1)
print('================')
print(song2)
print('================')
