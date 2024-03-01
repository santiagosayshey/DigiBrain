# Part 1

> [!activity] Activity 1
> (1 point) There is a secret passphrase embedded in the file called "**test.txt**" in the folder `/home/student/linux_basics/q01`. The secret can be found **following** the line that begins with the word "**And**" and ends with "**it**". Use grep with regular expression to locate this line and the line following it. What is the passphrase?

> [!solution] Solution
```bash
grep -A 1 '^And.*it$' /home/student/linux_basics/q01/test.txt
And give't Iago: what he will do with it
csf2024s1_{lanceteer-versify-phlogogenous}
```


> [!explanation] Explanation
> The solution uses `grep` with the `-A 1` option to find a line in `test.txt` starting with "And" and ending with "it", then prints this line and the one following it. The regular expression `'^And.*it$'` matches lines that meet these criteria. 

<hr>

> [!activity] Activity 2
> (1 point) In the folder `/home/student/linux_basics/q02`, there is a file called "**here.txt**" that contains passphrases. Find the passphrase that occur exactly **14 times**.


> [!solution] Solution
```bash
sort here.txt | uniq -c | grep -w '^ *14'
14 csf2024s1_{lanceteer-versify-phlogogenous}
```


> [!explanation] Explanation
> 1. `sort here.txt`: Sorts the contents of `here.txt`.
> 2. `uniq -c`: Counts the occurrences of each unique line.
> 3. `grep -w '^ *14'`: Filters lines starting with "14" to find the passphrase occurring exactly 14 times.
> - Each command is piped into the next to further filter the result.


<hr>

> [!activity] Activity 3
> (1 point) There are lots of files in `/home/student/linux_basics/q03`. What is the name of the file whose SHA256 sum is 389f0d2df51e5553118e2de48b40e1cc67ae2b477cf6d27ca1faf1c548f78f0c ?


> [!solution] Solution
```shell
#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <sha256sum>"
    exit 1
fi

directory=$1
hash=$2

# Verify the directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory does not exist."
    exit 1
fi

# Navigate to the directory
cd "$directory"

# Iterate through each file in the directory
found=0
for file in *; do
    # Calculate the SHA256 hash and compare
    if openssl dgst "$file" | grep -q "$hash"; then
        echo "File with SHA256 $hash is: $file"
        found=1
        break
    fi
done

# If the file was not found
if [ "$found" -eq 0 ]; then
    echo "No file with SHA256 $hash found in $directory."
fi
```

```bash
chmod +x SHA_finder.sh
./SHA_finder.sh /home/student/linux_basics/q03 389f0d2df51e5553118e2de48b40e1cc67ae2b477cf6d27ca1faf1c548f78f0c

File with SHA256 389f0d2df51e5553118e2de48b40e1cc67ae2b477cf6d27ca1faf1c548f78f0c is: 
csf2024s1_{undersense-consenting-komondorok}
```

> [!explanation] Explanation
> - **Purpose**: The script `SHA_finder.sh` verifies files in a designated directory against a specified SHA256 hash.
> - **Process**:
>   - Iterates through each file in the directory.
>   - Calculates the SHA256 hash of each file using `openssl dgst`.
>   - Compares the calculated hash with the provided hash.
> - **Output**:
>   - If a match is found, it outputs the filename containing the matching hash.
>   - If no match is found, it notifies the user accordingly.

<hr>

> [!activity] Activity 4
1 point) Generate a list of passwords from the source file words.txt. Use "l33t" conversion so that a=>4, e=>3, i=>1, and o=>0. For example "hello world" becomes "h3ll0 w0rld". There is a file encrypted using gpg (Gnu Privacy Protection) under `/home/student/linux_basics/q04`, using the command `gpg -c --batch --passphrase <pass>`. Unfortunately, we have forgotten the password. Use the "l33t" converted password list to brute-force the encrypted file**.** This may take a few minutes. **Please provide both the correct password and the content of the decrypted file**.


> [!solution] Solution
```shell
#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <encrypted_file> <source_file>"
    exit 1
fi

encrypted_file="$1"
source_file="$2"

echo "Starting decryption attempts..."

while IFS= read -r word; do
    leet_word=$(echo "$word" | tr 'aeio' '4310')
    
    # Attempt to decrypt the file using the converted word as the passphrase and suppress error messages

	if decrypted_content=$(gpg --decrypt --batch --passphrase "$leet_word" "$encrypted_file" 2>/dev/null); then
	    echo "Attempted to decrypt with password: $leet_word - Success!"
        echo "Decrypted content:"
        echo "$decrypted_content"
        exit 0
    else
        echo "Attempted to decrypt with password: $leet_word - Failed"
    fi
done < "$source_file"

echo "Decryption failed: No valid passphrase found after $attempt_count attempts."
exit 1
```

```shell
chmod +x decrypt.sh
./decrypt.sh "/home/student/linux_basics/q04/secret.txt.gpg" "/home/student/linux_basics/q04/words.txt"
Starting decryption attempts...
Attempted to decrypt with password: m4rk - Failed
Attempted to decrypt with password: supp0s3 - Failed
Attempted to decrypt with password: 4cc3pt4bl3 - Failed
Attempted to decrypt with password: bus1n3ss - Failed
Attempted to decrypt with password: 34rspl1tt1ng - Failed
Attempted to decrypt with password: l3v3l - Failed
Attempted to decrypt with password: l4ck4d41s1c4l - Failed
Attempted to decrypt with password: qu1ll - Failed
Attempted to decrypt with password: 3v4n3sc3nt - Failed
Attempted to decrypt with password: gr4t3ful - Failed
Attempted to decrypt with password: 3r3ct - Failed
Attempted to decrypt with password: 0b3s3 - Failed
Attempted to decrypt with password: d14b3t3s - Failed
Attempted to decrypt with password: sm3ll - Failed
Attempted to decrypt with password: st33p - Failed
Attempted to decrypt with password: br4k3 - Failed
Attempted to decrypt with password: pl0t - Failed
Attempted to decrypt with password: f4d3 - Failed
Attempted to decrypt with password: sk4t3 - Failed
Attempted to decrypt with password: r1p3 - Failed
Attempted to decrypt with password: gr0uchy - Failed
Attempted to decrypt with password: sc4r3cr0w - Failed
Attempted to decrypt with password: 04f1sh - Failed
Attempted to decrypt with password: m4l1c10us - Failed
Attempted to decrypt with password: v31n - Failed
Attempted to decrypt with password: p4rt - Failed
Attempted to decrypt with password: 4b4ft - Failed
Attempted to decrypt with password: 4tt4ch - Failed
Attempted to decrypt with password: h3lpful - Failed
Attempted to decrypt with password: 3c0n0m1c - Failed
Attempted to decrypt with password: ch1v4lr0us - Failed
Attempted to decrypt with password: r0d - Failed
Attempted to decrypt with password: d3l1c10us - Failed
Attempted to decrypt with password: f41thful - Failed
Attempted to decrypt with password: d3r4ng3d - Failed
Attempted to decrypt with password: s0und - Failed
Attempted to decrypt with password: sc4r3 - Failed
Attempted to decrypt with password: sw1ft - Failed
Attempted to decrypt with password: sp3ct4cul4r - Failed
Attempted to decrypt with password: s1nc3r3 - Failed
Attempted to decrypt with password: d0ll - Failed
Attempted to decrypt with password: 1ncr3d1bl3 - Failed
Attempted to decrypt with password: dr0p - Failed
Attempted to decrypt with password: gr1p - Failed
Attempted to decrypt with password: m1n14tur3 - Failed
Attempted to decrypt with password: pr0t3st - Failed
Attempted to decrypt with password: 1nst1nct1v3 - Failed
Attempted to decrypt with password: 3nj0y - Failed
Attempted to decrypt with password: 4b0und1ng - Failed
Attempted to decrypt with password: pr0t3ct1v3 - Failed
Attempted to decrypt with password: 3xclus1v3 - Failed
Attempted to decrypt with password: c0w4rdly - Failed
Attempted to decrypt with password: w4ry - Failed
Attempted to decrypt with password: cl0s3 - Failed
Attempted to decrypt with password: m3lt - Failed
Attempted to decrypt with password: b1rth - Failed
Attempted to decrypt with password: 1nc0m3 - Failed
Attempted to decrypt with password: tr1ck - Failed
Attempted to decrypt with password: 3ggs - Failed
Attempted to decrypt with password: s1d3 - Failed
Attempted to decrypt with password: 3nt3r - Failed
Attempted to decrypt with password: 0bs0l3t3 - Failed
Attempted to decrypt with password: p34r - Failed
Attempted to decrypt with password: s4ck - Failed
Attempted to decrypt with password: c4rt - Failed
Attempted to decrypt with password: fl4shy - Failed
Attempted to decrypt with password: supp0rt - Failed
Attempted to decrypt with password: bl4d3 - Failed
Attempted to decrypt with password: d3scr1b3 - Failed
Attempted to decrypt with password: d1sl1k3 - Failed
Attempted to decrypt with password: t00thp4st3 - Failed
Attempted to decrypt with password: 4fr41d - Failed
Attempted to decrypt with password: b3w1ld3r3d - Failed
Attempted to decrypt with password: k1nd - Failed
Attempted to decrypt with password: hyst3r1c4l - Failed
Attempted to decrypt with password: l0v3 - Failed
Attempted to decrypt with password: s3r10us - Failed
Attempted to decrypt with password: t0ugh - Failed
Attempted to decrypt with password: c4t - Failed
Attempted to decrypt with password: sh4d3 - Failed
Attempted to decrypt with password: cr0ss - Failed
Attempted to decrypt with password: k3y - Failed
Attempted to decrypt with password: pr0b4bl3 - Failed
Attempted to decrypt with password: m4g1c - Failed
Attempted to decrypt with password: 1nn4t3 - Failed
Attempted to decrypt with password: 1ns1d10us - Failed
Attempted to decrypt with password: 4qu4t1c - Failed
Attempted to decrypt with password: t3sty - Failed
Attempted to decrypt with password: w1r3 - Failed
Attempted to decrypt with password: ch1n - Failed
Attempted to decrypt with password: j01n - Failed
Attempted to decrypt with password: 0b31s4nt - Failed
Attempted to decrypt with password: 1mp3rf3ct - Failed
Attempted to decrypt with password: 0ss1f13d - Failed
Attempted to decrypt with password: fr1ght3n3d - Failed
Attempted to decrypt with password: c0nc3ntr4t3 - Success!
Decrypted content:
csf2024s1_{refreshments-systole-unflaky}
```

> [!explanation] Explanation
> - **Purpose**: The script aims to recover the passphrase used to encrypt a file (`secret.txt.gpg`) by brute-forcing it using a list of passwords generated from a source file (`words.txt`) with a "l33t" conversion.
> - **Process**:
>   - Iterates through each word in the source file, converting it to "l33t" format.
>   - Attempts to decrypt the encrypted file using `gpg` with the converted word as the passphrase.
> - **Output**
>   - If successful, prints the password used and the decrypted content of the file.
>   - If unsuccessful, continues with the next converted word.

<hr>


> [!activity] Activity 5
> (1 point) Find the flag hidden (encoded?) in the file `/home/student/linux_basics/q05/secret.txt.` Looks like the cyber.py (Hint: the file cyber.py was used to generate the file...)


> [!solution] Solution
```shell
#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <encrypted_file>"
    exit 1
fi

encrypted_file="$1"
echo "Starting decryption"

while IFS= read -r line; do
    p=$(echo "$line" | cut -c 1-4 | sed 's/^0*//')
    p=$((p + 6))
    letter=$(echo "$line" | cut -c "$p")
    echo -n "$letter"
done < "$encrypted_file"
echo
```

```shell
chmod +x secret_finder.sh
./secret_finder.sh "/home/student/CF-S2-2024/linux_basics/q05/secret.txt"
Starting decryption
csf2024s1_{amalings-ladrone-coregonidae}
```

> [!explanation] Explanation
> - **Purpose**: The script aims to recover the encoded input from the secret text file
> - **Process**:
>   - Examining the python script used to generate `secret.txt`, it becomes obvious that the script takes a string as input, and for each character of the input, generates a line of 100 characters, where there's a random amount of characters before each character in the input
>    - The first 4 characters of each line indicate the number of characters before the desired letter
>    - For each line inside secret.txt, we `cut` the first 4 characters out and use `sed` to extract the number by removing any padded zeroes.
>    - This number is increased by 6. 5 to remove the first 4 numbers as well as the colon, and an extra 1 because we want the character after the first x padded characters. 
> - **Output**
>   - For each line, once we find out desired `p` (number of padded characters before the wanted character) we use `cut` to extract the `p'th` character of each line to *decode* the message.
>   - We also use the `-n` flag to not `echo` each character on a new line


<hr>

> [!activity] Activity 6
> (1 point) There are lots of sub-directories and files under `/home/student/linux_basics/q06`. Find the file containing the secret. The file has size of exactly **47** bytes long.


> [!solution] Solution
```shell
find linux_basics/q06 -type f -size 47c
linux_basics/q06/folder05/folder027/folder005/source_folder/secret.txt

cat linux_basics/q06/folder05/folder027/folder005/source_folder/secret.txt
csf2024s1_{drybrained-unsolubleness-quintilent}
```

> [!explanation] Explanation
> - **Purpose**: Locate a file of size 47 bytes.
> - **Process**:
>   - Utilizes the `find` command to search for files within the specified directory (`linux_basics/q06`) with a size of exactly 47 bytes (`-size 47c`).
>   - Outputs the content of the secret file using `cat`

<hr>


> [!activity] Activity 7
> (1 point) Execute `/home/student/linux_basics/q07/a.out` and try to guess the secret.


> [!solution] Solution
```shell
./linux_basics/q07/a.out
What is the secret?
csf2024s1_{polyandrism-dissentient-dawdlingly}
congrats!!
```


> [!explanation] Explanation
> - First tried executing the binary to see if there were any hints. Nothing other than `What is the secret?`
> - On a whim, decided to look inside the binary file for any hints. Didn't expect to find anything useful, but found a string similar to answers found in other exercises - `csf2024s1_{polyandrism-dissentient-dawdlingly}`
> - Tried inputting this string and it worked!


<hr>


> [!activity] Activity 8
> (1 point) There is an encoded secret in /home/student/linux_basics/q08 folder. Decode to get the secret.


> [!solution] Solution
```shell
cat linux_basics/q08/secret.enc
Y3NmMjAyNHMxX3t3aW1sdW5nZS1hcHBsYXVkZXItdW5wZXRhbGxlZH0K

cat /home/student/linux_basics/q08/secret.enc | base64 --decode
csf2024s1_{wimlunge-applauder-unpetalled}
```


> [!explanation] Explanation
Upon examining the output from the `cat` command for the file `linux_basics/q08/secret.enc`, two observations led to the idea that it was Base64 encoded. 
> - First, the character set used in the string matches the Base64 alphabet, which includes letters (both uppercase and lowercase), digits, plus, and slash. This is a primary indicator of Base64 encoding. 
> - Second, the string's length being a multiple of 4 further supports this, as Base64 encoded outputs adhere to this length pattern. 
>
> Given these hints, the use of `base64 --decode` to decode the string seemed the most logical step.

# Part 2


> [!activity] Activity 1
> (1 point) Go to `/home/student/crypto/q01` on the HacklabVM (either via the graphical interface or via SSH). The file `secret.txt.enc` has been "encrypted" using this simple crypter code below (see mycrypto.py in the same directory). "Decrypt" the file and find the secret. 
> - Is this a good encryption? 
> - What is the key space?

> [!solution] Solution
```shell
$ python3 crypto/q01/mycrypto.py crypto/q01/secret.txt.enc

/* Output Contents*/
csf2024s1_{outtravel-sargassumaishes-monolocular}
```


> [!explanation] Explanation
> Upon examining the python script used to encode the secret text file, it becomes obvious that it uses a basic XOR encoder with a seed to encode. XOR encoding operates on a simple principle: if you take a piece of data $A$ and a key $B$, and apply XOR ($A \oplus B = C$), you get an encoded output $C$. The magic of XOR is that applying the operation again with the same key ($C \oplus B$) brings back the original data $A$.
> 
> The script also uses a default seed - `312024` when one is not provided. The obvious next step was to deduce that this default seed was indeed used to encode (because what else could be used in this context?), and that the encoded file can be *decoded* by encoding it again.
> 
> This decoding process is mathematically represented as follows: If the original encoding was $A \oplus B = C$, then decoding involves applying $C \oplus B$. Since XOR is its own inverse, we get back $A$. 
> 
> **Is this a good encryption?**  
> No, this is not good encryption. The dependency on a predictable input argument of 'seed' for key generation, rather than utilizing a purely random seed, compromises the encryption's security. This predictability allows for the possibility of brute-forcing the keys. Additionally, the simplicity of using XOR for encryption makes it vulnerable to chosen plaintext attacks, where the encryption key can be easily deduced by XORing known plaintext with its corresponding ciphertext.
> 
> **What is the key space?**  
> While Python 3's lack of limitation on the range of integers suggests a large key space, the actual effectiveness of this key space is severely diminished by the encryption scheme's reliance on a predictable 'seed' for key generation. This means that despite theoretically having a large key space, the practical security it offers is much lower because an attacker can systematically guess or brute-force the seed, effectively reducing the key space to a manageable size for attackers.

<hr>


> [!activity] Activity 2
> (1 point) A short, plaintext message has been encrypted using Textbook RSA (using the public exponent) with the same parameters used in the workshop. The encrypted message can be found in /home/student/crypto/q02 folder. Decrypt the secret.   


> [!solution] Solution
```python
import binascii

# Given RSA parameters
n = int("9B51C20306EDE535C8FCAADBC3F3515E52A0D005703DD449BEC66B23E2932313", 16)
p = int("C5A047A7C52ED3A2875F7D76C47B555F", 16)
q = int("C93268355C09197BBF1659B5522FFACD", 16)
e = int("010001", 16)
d = int("0D067636BAC6088AD2281E4BFFCACFEFEF9BC1A69FB9E701063DFBAAB436E4C1", 16)

def int_to_string(number):
    bin = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')
    return binascii.b2a_qp(bin).decode("utf-8")
ciphertext_int = int("50543d1e0fda637c109bb32c706dbaec8d8d20ce001cca02f8576a4852a072c9", 16)

# Decrypting the ciphertext
plaintext_int = pow(ciphertext_int, d, n)

# Converting the decrypted integer back to string
plaintext = int_to_string(plaintext_int)

print(plaintext)
```

```shell
$ python3 decrypt.py
csf2024s1_{voteptarius}
```

> [!explanation] Explanation
> In solving the challenge to decrypt a secret message encrypted using Textbook RSA, I utilized the RSA parameters that were provided.
>
> To achieve this, I first defined the RSA parameters in the Python script: the modulus $n$, the prime numbers $p$ and $q$, the public exponent $e$, and crucially, the private exponent $d$. These parameters were all given in hexadecimal format. The private exponent $d$ is especially important because it's used alongside the modulus $n$ to decrypt the message.
>
> I converted the ciphertext from hexadecimal to an integer to prepare it for decryption. This conversion is necessary because the RSA algorithm operates on numerical data. Using the RSA decryption formula: $$plaintext = ciphertext^d \mod n$$I applied the `pow` function in Python to the ciphertext integer, using $d$ and $n$ as arguments. This operation decrypted the ciphertext, yielding the original plaintext message: `csf2024s1_{voteptarius}`.

<hr>


> [!activity] Activity 3
> (1 point) Find the message hidden inside this [encrypted bitmap image](https://myuni.adelaide.edu.au/courses/95262/files/14689587?wrap=1 "2000x2000_256-color-1.bmp.encrypted.zip") .You don't need to decrypt.


> [!explanation] Explanation
> - Workshop 2 included an exercise to highlight the issues with ECB encoding, especially in the cases of the image. Since we we're not given the original image to extract headers from, I tried using the original image headers from the workshop. This did not work. I was quite stuck for a while on this, until noticing the name of the encrypted image - `2000x2000_256-color.bmp.` 
> - I created a python script to generate a gradient bmp image of size 2000x2000 at a colour depth of 256 bits. (probably an easier way to do this!). Then I copied the headers  from this generated image, and the rest of the encrypted image into a new file to reveal the ECB encoded image: 

![[out.bmp]]

> [!solution] Solution
```python
from PIL import Image
import numpy as np

# Define image dimensions and colors
width, height = 2000, 2000
colors = 256

# Create an image with a gradient of 256 colors
image = Image.new("P", (width, height))
palette = []

for i in range(colors):
    palette.extend([i, i, i])  # Grayscale gradient
image.putpalette(palette)

# Generate gradient
for y in range(height):
    for x in range(width):
        image.putpixel((x, y), (x * colors // width) % colors)

# Save the image as BMP
bmp_path = "generated_2000x2000_256color.bmp"
image.save(bmp_path, "BMP")
bmp_path
```

```shell
$ python3 ECB_exploit.py
$ dd if=headers.bmp count=54 ibs=1 >> out.bmp
54+0 records in
0+1 records out
54 bytes copied, 0.000276128 s, 196 kB/s
$ dd if=2000x2000_256-color.bmp.encrypted skip=54 ibs=1 >> out.bmp
4001034+0 records in
7814+1 records out
4001034 bytes (4.0 MB, 3.8 MiB) copied, 1.80308 s, 2.2 MB/s
```


<hr>


> [!activity] Activity 4
> (1 points) Go to `/home/student/crypto/q04` and find the file ciphertext.txt, which was created using one of the classical ciphers. Find out what the original text is. What is the key used?


> [!explanation] Explanation
> This question is a doozy. My first thought was to perform some kind of frequency analysis on the text to see what letter combinations are most frequent. 

```python
import sys

def frequency_analysis(text, n):
    letter_freq = {}
    for i in range(len(text) - n + 1):
        char = text[i:i+n].lower()
        if all(c.isalpha() for c in char):
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1
    freq_array = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    return freq_array

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <number of letters>")
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])

    try:
        with open(filename, 'r') as file:
            text = file.read()
        freq_array = frequency_analysis(text, n)
        for combination, freq in freq_array:
            print(f"'{combination}': {freq}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The number of letters must be a valid integer.")

if __name__ == "__main__":
    main()
```

Testing with $n = 3$, we get the following results:

```shell
$ python3 freq.py "crypto/q04/ciphertext.txt" 3
'xut': 15
'cos': 11
'irz': 6
'ctj': 5
'ynj': 4
'rts': 3
'snr': 3
'jte': 3
...
```


> [!explanation] Explanation
> We have some clear winners! `xut` comes in with a score of 15. `cos` with 11. The two most frequent 3-letter words in English are `the` and `was`. For a second, lets assume that `xut` and `cos` translate to `the` and `was`. This means:
> - $x=t$
> - $u=h$
> - $t=e$
> - $c=w$
> - $o=a$
> - $s=s$
> 
> Using these changes, let's run `sed` to replace the words and see what comes out:

```shell
$ cat crypto/q04/ciphertext.txt | sed 's/XUT/THE/g' | sed 's/COS/WAS/g'
IX WAS THE NTSX NY XIMTS, IX WAS THE CNJSX NY XIMTS, IX WAS THE OZT NY CISRNM, IX WAS THE OZT NY YNNLISURTSS, IX WAS THE TCNEU NY NTLITY, IX WAS THE TCNEU NY IREJTRWLIXB, IX WAS THE STOSNR NY LIZUX, IX WAS THE STOSNR NY ROJKRTSS, IX WAS THE SCJIRZ NY UNCT, IX WAS THE CIRXTJ NY RTSCOIJ, CT UOR TVTJBXUIRZ NTYNJT WS, CT UOR RNXUIRZ NTYNJT WS, CT CTJT OLL ZNIRZ RIJTEX XN UTOVTR, CT CTJT OLL ZNIRZ RIJTEX THE NTHEJ COB - IR SUNJX, THE CTJINR WAS SN YOJ LIKT THE CJTSTRX CTJINR, XUOX SNMT NY IXS RNISITSX OWXUNJIXITS IRSISXTR NR IXS NTIRZ JTETIVTR, YNJ ZNNR NJ YNJ TVIL, IR THE SWCTJLOXIVT RTZJTT NY ENMCOJISNR NRLB.
```


> [!explanation] Explanation
> Now we're getting somewhere! Of course we could go further with the analysis, and probably find that `ix` translates to `it`, `ntsx` translates to `best`, etc, but every literature nerd on the planet would be yelling **DICKENS!** at this point. Because my favourite piece of media ever is *The Last of Us Part II*, I've obviously read every piece of work that inspired it ... including *A Tale of Two Cities*.
> 
>- **Theory:** This encoded text is the opening paragraph to **Charles Dickens' A Tale of Two Cities**. I've read it enough times to recognise the very similar structure and commas used. Not to mention the frequency analysis pin pointing `the` and `was`. At this point, I think I can confidently say this was encoded using a **Substituion Cipher**!


> [!QUOTE] A Tale of Two Cities - Opening Paragraph
> It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.


> [!solution] Solution
> Let's write a script to finish the tuple list and find the substitution key. Using this set, we can treat it as the key, encode our plain text and determine if the key is correct or not. 

```python
decrypted_text = ("It was the best of times, it was the worst of times, "
                  "it was the age of wisdom, it was the age of foolishness, "
                  "it was the epoch of belief, it was the epoch of incredulity, "
                  "it was the season of Light, it was the season of Darkness, "
                  "it was the spring of hope, it was the winter of despair, "
                  "we had everything before us, we had nothing before us, "
                  "we were all going direct to Heaven, we were all going direct the other way "
                  "- in short, the period was so far like the present period, "
                  "that some of its noisiest authorities insisted on its being received, "
                  "for good or for evil, in the superlative degree of comparison only.")

encrypted_text = ("IX COS XUT NTSX NY XIMTS, IX COS XUT CNJSX NY XIMTS, "
                  "IX COS XUT OZT NY CISRNM, IX COS XUT OZT NY YNNLISURTSS, "
                  "IX COS XUT TCNEU NY NTLITY, IX COS XUT TCNEU NY IREJTRWLIXB, "
                  "IX COS XUT STOSNR NY LIZUX, IX COS XUT STOSNR NY ROJKRTSS, "
                  "IX COS XUT SCJIRZ NY UNCT, IX COS XUT CIRXTJ NY RTSCOIJ, "
                  "CT UOR TVTJBXUIRZ NTYNJT WS, CT UOR RNXUIRZ NTYNJT WS, "
                  "CT CTJT OLL ZNIRZ RIJTEX XN UTOVTR, CT CTJT OLL ZNIRZ RIJTEX XUT NXUTJ COB "
                  "- IR SUNJX, XUT CTJINR COS SN YOJ LIKT XUT CJTSTRX CTJINR, "
                  "XUOX SNMT NY IXS RNISITSX OWXUNJIXITS IRSISXTR NR IXS NTIRZ JTETIVTR, "
                  "YNJ ZNNR NJ YNJ TVIL, IR XUT SWCTJLOXIVT RTZJTT NY ENMCOJISNR NRLB.")

# Lowercase and remove spaces
decrypted_processed = "".join(decrypted_text.lower().split())
encrypted_processed = "".join(encrypted_text.lower().split())

# Ensure lengths match after processing
assert len(decrypted_processed) == len(encrypted_processed), "Lengths do not match."

# Pair each character
pairs = list(zip(decrypted_processed, encrypted_processed))
unique_pairs = set(pairs)
filtered_unique_pairs = {pair for pair in pairs if pair[0] != pair[1]}

def substitution_cipher_encrypt(text, key_set):
    # Create a dictionary from the key set for easier lookup
    key_dict = {k: v for k, v in key_set}
    
    # Encrypt the text
    new_text = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in key_dict:
            # Substitute if the character is in the key
            encrypted_char = key_dict[lower_char]
        else:
            # If no substitution is found, keep the original character
            encrypted_char = char
        new_text += encrypted_char
    
    return new_text

encrypted = substitution_cipher_encrypt(decrypted_text, filtered_unique_pairs)
print(encrypted)
```

```shell
$ python3 tuple.py
('f', 'y')
('c', 'e')
('u', 'w')
('d', 'r')
('g', 'z')
('r', 'j')
('y', 'b')
('b', 'n')
('h', 'u')
('a', 'o')
('e', 't')
('w', 'c')
('n', 'r')
('p', 'c')
('o', 'n')
('t', 'x')

Ix cos xut ntsx ny ximts, ix cos xut cnjsx ny ximts, ix cos xut ozt ny cisrnm, ix cos xut ozt ny ynnlisurtss, ix cos xut tcneu ny ntlity, ix cos xut tcneu ny irejtrwlixb, ix cos xut stosnr ny Lizux, ix cos xut stosnr ny rojkrtss, ix cos xut scjirz ny unct, ix cos xut cirxtj ny rtscoij, ct uor tvtjbxuirz ntynjt ws, ct uor rnxuirz ntynjt ws, ct ctjt oll znirz rijtex xn utovtr, ct ctjt oll znirz rijtex xut nxutj cob - ir sunjx, xut ctjinr cos sn yoj likt xut cjtstrx ctjinr, xuox snmt ny ixs rnisitsx owxunjixits irsisxtr nr ixs ntirz jtetivtr, ynj znnr nj ynj tvil, ir xut swctjloxivt rtzjtt ny enmcojisnr nrlb.
```


> [!explanation] Explanation
> And there we have it!
> - **Decoded Text:** It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.
> - **Key**: [f : y, c : e, u : w, d : r, g : z, r : j, y : b, b : n, h : u, a : o, e : t, w : c, n : r, p : c, o : n, t : x]


<hr>


> [!activity] Activity 5
> 1 point) Download this [shadow file](https://myuni.adelaide.edu.au/courses/95262/files/14689590?wrap=1 "shadow-2") `(/etc/shadow)` from an old Linux system. Crack the password for the user account called "yoda" (the last entry).


> [!explanation] Explanation
> This one is pretty straightforward. First we extract the hashed password from the shadow file.
> - `$1$1V8SfbzZ$No6X4H.b1.lqGRv2yLYNv0`
> 
> Then we extract the wordlist, and run `hashcat` with the hashed password against the wordlist.  
> - `hashcat -m 500 -o out hash rockyou.txt --force`


> [!solution] Solution
```shell
samchau@SamPC:~/q05$ hashcat -m 500 -o out hash rockyou.txt --force
hashcat (v5.1.0) starting...

OpenCL Platform #1: The pocl project
====================================
* Device #1: pthread-AMD Ryzen 7 3700X 8-Core Processor, 4096/13924 MB allocatable, 16MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Single-Hash
* Single-Salt

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

* Device #1: build_opts '-cl-std=CL1.2 -I OpenCL -I /usr/share/hashcat/OpenCL -D LOCAL_MEM_TYPE=2 -D VENDOR_ID=64 -D CUDA_ARCH=0 -D AMD_ROCM=0 -D VECT_SIZE=8 -D DEVICE_TYPE=2 -D DGST_R0=0 -D DGST_R1=1 -D DGST_R2=2 -D DGST_R3=3 -D DGST_ELEM=4 -D KERN_TYPE=500 -D _unroll'
* Device #1: Kernel m00500-pure.c1da9768.kernel not found in cache! Building may take a while...
* Device #1: Kernel amp_a0.7b4bd2c2.kernel not found in cache! Building may take a while...
Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)
Hash.Target......: $1$1V8SfbzZ$No6X4H.b1.lqGRv2yLYNv0
Time.Started.....: Fri Mar  1 14:13:05 2024 (1 sec)
Time.Estimated...: Fri Mar  1 14:13:06 2024 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     8477 H/s (12.52ms) @ Accel:512 Loops:62 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 8192/14344385 (0.06%)
Rejected.........: 0/8192 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:992-1000
Candidates.#1....: 123456 -> whitetiger

Started: Fri Mar  1 14:12:53 2024
Stopped: Fri Mar  1 14:13:07 2024
```

```shell
samchau@SamPC:~/q05$ cat out
$1$1V8SfbzZ$No6X4H.b1.lqGRv2yLYNv0:spiderman1
```

**14 Seconds!!!**

