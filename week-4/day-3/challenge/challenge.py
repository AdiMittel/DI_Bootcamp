user_input = input("Please enter a string that you want encrypted in ceasers cyper: ")
try:
    shift = int(input("Please enter how many letters you want to shift your cypher: "))
except:
   shift = int(input("Please enter how many letters you want to shift your cypher: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
cypher_code = ''
new_char = 0 
for i in user_input:
    if i.lower() in alphabet:
        new_char = alphabet.index(i) + shift
        cypher_code += alphabet[new_char % 26]
    else:
        cypher_code += i
print(f"{user_input} will be encoded to {cypher_code}")
print(f"{cypher_code} will be decripted to {user_input}")
#decrypt
reverse_a = "abcdefghijklmnopqrstuvwxyz"[::-1] 
new_char1 = 0
decyper_code = ""
for e in cypher_code:
    if e.lower() in reverse_a:
        new_char1 = reverse_a.index(e) + shift
        decyper_code += reverse_a[new_char1 % 26]
    else:
        decyper_code += e
print(decyper_code)