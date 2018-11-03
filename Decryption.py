alphabet='abcdefghijklmnopqrstuvwxyz'
key=int(input("Enter the Key:"))
msg=input("Enter a Message:")
new_msg=' '
for character in msg:
    if character in alphabet:
        pos=alphabet.find(character)
        new_pos=(pos-key)%26
        new_char=alphabet[new_pos]
        new_msg=new_msg+new_char
    else:
        new_msg+=character
print(new_msg)
    
