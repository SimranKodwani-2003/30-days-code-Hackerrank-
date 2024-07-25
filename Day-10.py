# ****************Binary Number*******
if __name__ == '__main__':
    n = int(input())
binary = bin(n)[2:]
print(max(map(len, binary.split('0'))))