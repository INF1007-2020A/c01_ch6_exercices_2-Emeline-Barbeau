#!/usr/bin/env python
# -*- coding: utf-8 -*-


from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    
    some_dict = {}
    index = 0

    for item in some_list:  # Remplit un dictionnaire avec les infos d'un tableau
        some_dict[item] = index
        index += 1
    
    return some_dict

def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    
    result = [(color, cnames[color]) for color in colors]
    return result


def odd_integer_for_loop(end: int) -> list:
    odd_int = [] 
    for num in range(1, end, 2):  # Met dans une liste uniquement les nbrs impaires
        odd_int.append(num)

    return odd_int


def odd_integer_list_comprehension(end: int) -> list:
    odd_int = [num for num in range(1, end, 2)] 
    return odd_int


def loop_traversal(integers: list) -> None:
    for index in range(len(integers)):
        print(f"{index}: {integers[index]}")
    

def word_dict_for_loop(words: list) -> dict:
    word_dict = {}

    for word in words:
        word_dict[word[0].upper()] = word  # Met la 1ère lettre en majuscule en key du dictionnaire

    return word_dict


def word_dict_comprehension(words: list) -> dict:
    word_dict = {word[0].upper(): word for word in words}
    return word_dict


def dictionary_traversal(words: dict) -> None:
    for key in sorted(words.keys()):
        print(f"{key}: {words[key]}") 


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    integer = 13
    integers_for = odd_integer_for_loop(integer)
    print(f"Liste avec boucle for et le nombre 13: {integers_for}")
    integers_comprehension = odd_integer_for_loop(integer)
    print(f"Liste avec list comprehension et le nombre 13: {integers_comprehension}")

    print(f"Les 2 listes sont-elles identiques? {integers_for == integers_comprehension}")
    print(f"Parcours d'une des 2 listes...")
    loop_traversal(integers_for)

    words = ["initialisation", "ajout", "modification", "suppression", "dictionnaire"]
    words_for = word_dict_for_loop(words)
    print(f"Dictionnaire avec la boucle for: {words_for}")
    words_comprehension = word_dict_comprehension(words)
    print(f"Dictionnaire avec le dictionary comprehension: {words_comprehension}")

    print(f"Les 2 dictionnaires sont-ils identiques? {words_for == words_comprehension}")
    print(f"Parcours d'un des 2 dictionnaires...")
    dictionary_traversal(words_comprehension)


if __name__ == '__main__':
    main()
