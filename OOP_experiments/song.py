class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_the_song(self):
		for line in self.lyrics:
			print(line)
		print("\n")

first_part = Song(["Twenty-five years and my life is still",
			"Trying to get up that great big hill of hope",
			"For a destination"])

second_part = Song(["I realized quickly when I knew I should",
			"That the world was made up of this brotherhood of man",
			"For whatever that means"])

third_part = Song(["And so I cry sometimes",
			"When I'm lying in bed just to get it all out",
			"What's in my head",
			"And I, I am feeling a little peculiar"])


first_part.sing_the_song()
second_part.sing_the_song()
third_part.sing_the_song()