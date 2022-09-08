# Intro
A cryptographic challenge on picoCTF that has the concept of modular multiplicative inverse.

# Flag
`picoCTF{1nv3r53ly_h4rd_8a05d939}`

# Walkthrough
1. The challenge gave the steps to do for each character of the encrypted message so I first read about the concept of modular multiplicative inverse
2. Then I searched on a function that out-of-the-box calculates the M. I. of any number
3. Then I mapped the result as specified and left unspecified numbers as is

# Code
```python
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
```