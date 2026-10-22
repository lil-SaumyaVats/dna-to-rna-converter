dna = input("Enter a DNA sequence: ")
dna = dna.upper()

if dna == "":
    print("Please enter a DNA sequence")
    exit()

for letter in dna:
    if letter not in "ATGC":
        print("Invalid DNA sequence..")
        exit()

print("Valid DNA sequence")

rna = dna.replace("T", "U")
print("RNA:", rna)


