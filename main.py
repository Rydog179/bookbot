def main():
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
        print(file_contents)


def sort_on(char_dict):
    return char_dict["num"]

def count():
    print("--- Begin report of books/frankenstein.txt ---")
    number = 0
    alphabet= {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0
    }
    
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
        words = file_contents.split()
        
      
        for word in words:
            number += 1
    print (number)
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read().lower()
        for chars in file_contents:
            if chars in alphabet:
                alphabet[chars] +=1

    char_list= []
    for key in alphabet:
        char_dict = {"char": key, "num":alphabet[key]}
        char_list.append(char_dict)
    
    char_list.sort(key=sort_on, reverse=True)
    for item in char_list:
        print(f"The {item['char']} character was found {item['num']} times.")
    print("--- End report ---")

   
    
    
    
    
    




    
count()
        
            


        