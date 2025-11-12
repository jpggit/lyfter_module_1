
import csv

def collect_videogames():
    games = []

    while True: 
        name = input ("Game name: ").strip()
        genre = input("Genre: ").strip()
        developer = input("Developer: ").strip()
        esbr = input("ESBR rating: ").strip()

        game = {
            "Name": name,
            "Genre": genre,
            "Developer": developer,
            "ESBR": esbr,
        }

        games.append(game)

        more = input("Do you want to enter another game? (y/n): ").strip().lower()
        if more == 'n':
            break
        
    return games


def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file: 
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


games = collect_videogames()
write_csv_file('csv_saver.csv', games, games[0].keys())