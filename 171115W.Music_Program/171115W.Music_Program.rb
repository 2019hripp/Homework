# File Name: 171115W.Music_Program.rb

@songs = []
@artists = []


def intro
	puts "here's a music thing have at it"
end

#asking what the user wants to work with
def songOrArtist
	puts "Let's start. Are you working with songs are artists?"
	@song_or_artist = gets.chomp #save user response
		if @song_or_artist == "Songs" || "songs"
			song #directs user to the song section
		elsif @song_or_artist == "Artists" || "artists"
			artist #directs user to the artist section
		else @song_or_artist != "Artists" || "artists" || "Songs" || "songs"
			puts "Error. Restarting."
			songOrArtist #goes back to start if user doesn't work with program
		end
end


def song
	puts "Would you like to add or delete?"
	@song_add_or_delete = gets.chomp
		if @song_add_or_delete == "add" || "delete"
			puts "Whats the song name?"
				@songName = gets.chomp
			if @song_add_or_delete == "add"
				@songs.push(@songName)
				puts "done"
				mid
			else @song_add_or_delete == "delete"
				@songs.delete(@songName)
				puts "done"
				mid
			end
		else @song_add_or_delete != "add" || "delete"
			puts "You can only put 'add' or 'delete'"
			song
		end
end

def artist
	puts "Are you adding or deleting here?"
		@artist_add_or_delete == gets.chomp
	puts "What's it called?"
		@artistName == gets.chomp

		if @artist_add_or_delete == "add"
			@artist.push(@artistName)
			puts "task completed"
		elsif @artist_add_or_delete == "delete"
			@artist.delete(@artistName)
			puts "task completed"
		else
			puts "Try again. You can only put 'add' or 'delete'"
			artist
		end
	mid
end

def mid
	puts "What would you like to do?"
	print #{@songs}

end