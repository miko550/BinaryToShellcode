# BinaryToShellcode
Pyhton code that convert available made payload to hex shellcode format adn it byte number

currently available is {0x5a, 0x6f, 0x75, 0x6b, 0xe2, 0x6f .....}

USAGE
```
pyhton3 shellconvert.py payload.bin
```

TODO
- make this format "\xe8\x00\x00\x00\x00\x58\x55\x89\xe"
- save result on file
- add agrument to select format

UPDATE
- 31/05/2021 - just find out this call hex dump and you can use linux command `xxd` [I'm an inline-style link](https://www.tutorialspoint.com/unix_commands/xxd.htm)
