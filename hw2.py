dna = input("DNA: ")
base = input("base: ")

if dna.isdigit() or base.isdigit():
    print("This is not DNA String")
    exit()

valid = set("ACGT")

for ch in dna:
        if ch.upper() not in valid:
            print("This is not DNA String")
            exit()

if base.upper() not in valid:
        print("This is not DNA String")
        exit()

count = 0
base = base.upper()

for c in dna:
        print("c:", c)
        if c. upper() == base:
            print("Ture if test")
            count += 1
print(f"There are {count} times that the base {base} occur in this DNA.")
