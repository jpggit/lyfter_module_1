#Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def sort_songs(path):
    # Read all songs
    with open(path, "r", encoding='utf-8') as file:
        songs = [line.strip() for line in file if line.strip()] #strip /n and spaces at the ends

    # Sort songs
    sorted_songs = sorted(songs)

    # Write sorted songs to new file
    with open("encoding_data_alpha.txt", "w", encoding='utf-8') as file:
        for song in sorted_songs:
            file.write(song + "\n")

sort_songs("encoding_data_raw.txt")
