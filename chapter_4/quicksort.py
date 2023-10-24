from typing import List, Any, Tuple, Dict

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

def quick_sort(arr: List, key: str) -> tuple[list[Dict], int]:
    operations_count = 1

    if len(arr) < 2:
        return arr, operations_count
    elif len(arr) == 2:
        return [arr[0], arr[1]] if arr[0][key] > arr[1][key] else [arr[1], arr[0]], operations_count

    pivot = arr[0]
    smaller = [row for row in arr if row[key] < pivot[key]]
    bigger = [row for row in arr if row[key] > pivot[key]]

    sorted_smaller, smaller_operations_count = quick_sort(smaller, key)
    sorted_bigger, bigger_operations_count = quick_sort(bigger, key)

    sorted_list = sorted_bigger + [pivot] + sorted_smaller
    operations = operations_count + smaller_operations_count + bigger_operations_count

    return sorted_list, operations

def quick_sort_artists() -> None:
    sorted_artists, operations = quick_sort(most_selling_artists, 'copies')

    print(f'Operations: {operations}')
    for item in sorted_artists:
        print(f'Artist: {item["artist"]}, Copies: {item["copies"]}M')

quick_sort_artists()