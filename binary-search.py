import math

# 128 name list
names_list = [
    'Abdiel',
    'Adriana',
    'Adriano',
    'Alex',
    'Alice',
    'Alison',
    'Amanda',
    'Ana',
    'Anderson',
    'André',
    'Andreia',
    'Ângela',
    'Ângelo',
    'Antônia',
    'Antônio',
    'Arllon',
    'Arthur',
    'Azazel',
    'Beatriz',
    'Bianca',
    'Bruna',
    'Bruno',
    'Caio',
    'Camila',
    'Camilo',
    'Carlos',
    'Carolina',
    'Caroline',
    'Catarina',
    'Cecília',
    'Clara',
    'Clarissa',
    'Cristiano',
    'Daniel',
    'Débora',
    'Diego',
    'Douglas',
    'Eduarda',
    'Eduardo',
    'Emanuel',
    'Fabiana',
    'Felipe',
    'Fernanda',
    'Fernando',
    'Flávia',
    'Gabriela',
    'Giovanna',
    'Guilherme',
    'Gustavo',
    'Helena',
    'Heloísa',
    'Henrique',
    'Isabella',
    'Isadora',
    'João',
    'Jonas',
    'José',
    'Josefina',
    'Júlia',
    'Juliana',
    'Juliano',
    'Lara',
    'Larissa',
    'Laura',
    'Leandro',
    'Leonardo',
    'Letícia',
    'Lia',
    'Lívia',
    'Lorena',
    'Luana',
    'Lucas',
    'Luiz',
    'Manuela',
    'Marcelo',
    'Marco',
    'Marcos',
    'Maria',
    'Mariana',
    'Mariano',
    'Marília',
    'Matheus',
    'Maxuel',
    'Melissa',
    'Miguel',
    'Mirella',
    'Natália',
    'Otávio',
    'Parmênides',
    'Patrícia',
    'Pedro',
    'Platão',
    'Priscila',
    'Ptolomeu',
    'Rafael',
    'Rafaela',
    'Raul',
    'Renan',
    'Renata',
    'Renato',
    'Ricardo',
    'Roberto',
    'Robson',
    'Rodrigo',
    'Ronaldo',
    'Ryan',
    'Samael',
    'Samuel',
    'Silvana',
    'Sócrates',
    'Sofia',
    'Sophia',
    'Tertuliano',
    'Thiago',
    'Tiago',
    'Túlio',
    'Valentina',
    'Valentino',
    'Valéria',
    'Vanessa',
    'Victor',
    'Vinícius',
    'Vitor',
    'Vitória',
    'Vitorina',
    'Viviane',
    'Yasmin',
    'Zlatan',
]


def print_iterations(counter) -> None:
    print('Iterations: ' + str(counter))


def normal_search(search_name: str) -> int:
    counter = 0

    for name in names_list:
        counter += 1

        if name == search_name:
            print('Name at position: ' + str(counter))
            return counter

    print('Name was not found in list.')
    return counter


def binary_search(search_name: str) -> int:
    counter = 0
    low = 0
    high = len(names_list) -1

    while low <= high:
        counter += 1
        mid = math.ceil(low + (high - low) // 2)
        guess_name = names_list[mid]

        if guess_name == search_name:
            print('Name at position: ' + str(mid + 1))
            return counter
        elif search_name < guess_name:
            high = mid - 1
        else:
            low = mid + 1

    print('Name was not found in list.')
    return counter


def search_name() -> None:
    searchable_name = input('Enter name to search:\n')

    print('Normal Search: ')
    print_iterations(normal_search(searchable_name))

    print('\n')

    print('Binary Search: ')
    print_iterations(binary_search(searchable_name))

search_name()




