import os 

def find_and_replace(file_path, search_word, replace_word):
    
    try:
        if not os.path.exists(file_path):
            with open(file_path,'w') as file:
                file.write("python is a high level programming language.\n it is case sensitive language.\n ")
            print(f"'{file_path}' file created .")

        with open (file_path,'r') as file:
            content =file.read()


        if search_word not in content:
            print(f"'{search_word}' if not in file.")
            return
        
        modified_content= content.replace(search_word,replace_word)

        with open(file_path,'w') as file:
            file.write(modified_content)
        
        print("success !!")
        print(f"'{search_word}' word is replaced in '{replace_word} !!")

    except PermissionError:
        print("ERROR: IF NOT PERMISSION IN THIS FILE.")
         
    except Exception as e:
        print(" UNEXPECTED ERROR : ", e)
    

file_name= "data.txt"
search_word=input("enter the searching a word:  ")
replace_word = input("enter the replacing a word: ")

find_and_replace(file_name, search_word, replace_word)