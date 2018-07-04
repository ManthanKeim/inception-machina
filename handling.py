
try:
    p = 32
    #b = p/0

    f = open("ab.txt")
    for line in f:
        print(line)
except Exception as e:
    print(e)

# except (FileNotFoundError,ZeroDivisionError):
#     print("FILE NOT")
# except ZeroDivisionError:
#     print("ZERO ERROR")

#p = 0/0

