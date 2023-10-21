
most_selling_artists = [
    {'artist': 'U2', 'copies': 150},
    {'artist': 'Bob Marley', 'copies': 75},
    {'artist': 'Prince', 'copies': 100},
    {'artist': 'Adele', 'copies': 100},
    {'artist': 'Bruce Springsteen', 'copies': 120},
    {'artist': 'ABBA', 'copies': 150},
    {'artist': 'Eagles', 'copies': 150},
    {'artist': 'AC/DC', 'copies': 200},
    {'artist': 'Whitney Houston', 'copies': 200},
    {'artist': 'Michael Jackson', 'copies': 350},
    {'artist': 'Beyoncé', 'copies': 100},
    {'artist': 'Guns N Roses', 'copies': 100},
    {'artist': 'The Beatles', 'copies': 600},
    {'artist': 'Phil Collins', 'copies': 100},
    {'artist': 'Eric Clapton', 'copies': 100},
    {'artist': 'Simon & Garfunkel', 'copies': 100},
    {'artist': 'The Bee Gees', 'copies': 220},
    {'artist': 'Nirvana', 'copies': 75},
    {'artist': 'Metallica', 'copies': 125},
    {'artist': 'Coldplay', 'copies': 100},
    {'artist': 'Frank Sinatra', 'copies': 150},
    {'artist': 'Bon Jovi', 'copies': 100},
    {'artist': 'Eminem', 'copies': 220},
    {'artist': 'David Bowie', 'copies': 140},
    {'artist': 'Elvis Presley', 'copies': 600},
    {'artist': 'Pink Floyd', 'copies': 250},
    {'artist': 'Celine Dion', 'copies': 200},
    {'artist': 'Mariah Carey', 'copies': 200},
    {'artist': 'The Rolling Stones', 'copies': 200},
    {'artist': 'Billy Joel', 'copies': 150},
    {'artist': 'Barbra Streisand', 'copies': 145},
    {'artist': 'Queen', 'copies': 300},
    {'artist': 'Elton John', 'copies': 300},
    {'artist': 'Johnny Cash', 'copies': 90},
    {'artist': 'Queen', 'copies': 250},
    {'artist': 'Santana', 'copies': 100},
    {'artist': 'Madonna', 'copies': 300},
    {'artist': 'The Doors', 'copies': 80},
    {'artist': 'Led Zeppelin', 'copies': 300},
    {'artist': 'Bob Dylan', 'copies': 125},
    {'artist': 'Stevie Wonder', 'copies': 100},
    {'artist': 'The Supremes', 'copies': 70},
    {'artist': 'George Michael', 'copies': 120},
    {'artist': 'The Who', 'copies': 100},
    {'artist': 'Ray Charles', 'copies': 75},
    {'artist': 'Santana', 'copies': 100},
    {'artist': 'Jimi Hendrix', 'copies': 65},
    {'artist': 'The Beach Boys', 'copies': 100},
    {'artist': 'Green Day', 'copies': 85},
    {'artist': 'Aerosmith', 'copies': 150},
]


def find_highest_index(arr) -> tuple[int, int]:
    highest_index = 0
    counter = 0

    for index, item in enumerate(arr):
        if item['copies'] > arr[highest_index]['copies']:
            highest_index = index
        counter += 1

    return highest_index, counter

def sort_artists() -> None:
    list_to_sort = most_selling_artists
    sorted_list = []
    counter = 0
    highest_index_count = 0

    for i in range(len(list_to_sort)):
        highest_index, index_count = find_highest_index(list_to_sort)
        sorted_list.append(list_to_sort[highest_index])
        list_to_sort.pop(highest_index)
        counter += 1
        highest_index_count += index_count

    print(f'Operations: {counter + highest_index_count}')

    for item in sorted_list:
        print(f'Artist: {item["artist"]}, Copies: {item["copies"]}M')

sort_artists()