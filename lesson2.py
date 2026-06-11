C_Y = int("2026")
A = int(input("Which year did you were born?"))
print(f"your age is {C_Y - A} ")
#----------------------------------------------------------
my_favorit_languages = ['English', 'Persian', 'Korean', 'German', 'Chinese']
print(f"""right now, I'm learning {my_favorit_languages[3]}
and I'm really happy about that^^ """)
my_favorit_languages.append('French')
my_favorit_languages.insert(1,'Italian')
print(my_favorit_languages)

del my_favorit_languages[1]
print(my_favorit_languages)

popped_lang = my_favorit_languages.pop()
print(popped_lang)
