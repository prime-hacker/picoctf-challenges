import string

message = [104,290,356,313,262,337,354,229,146,297,118,373,221,359,338,321,288,79,214,277,131,190,377]
for num in message:
    mod_inv = pow(num, -1, mod=41) 
    if mod_inv in range(1,27):
        print(string.ascii_lowercase[mod_inv-1],end="")
    elif mod_inv in range(27,37):
        print(string.digits[mod_inv%27], end="")
    elif mod_inv == 37:
        print("_", end="")
    else:
        print(mod_inv, end="")