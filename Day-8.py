# *******************Dictionary and maps************
n = int(input().strip())
phonebook = {}
for _ in range(n):
    entry = input().strip().split()
    name = entry[0]
    phone = entry[1]
    phonebook[name] = phone
while True:
    try:
        query = input().strip()
        if query in phonebook:
            print(f"{query}={phonebook[query]}")
        else:
            print("Not found")
    except EOFError:
        break
