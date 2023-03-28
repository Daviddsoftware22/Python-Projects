def password_creator(ch_numbers):
    count = 0
    ch_list = []
    password = ""
    d = ["1", "2", "3", "4", "5", "6", "7", "8", "9","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
        , "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    while count != ch_numbers:
        ch_list.append(random.choice(d))
        password += ch_list[count]
        count+=1
    return password

