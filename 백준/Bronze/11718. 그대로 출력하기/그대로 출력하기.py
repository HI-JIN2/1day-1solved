while True:
    try:
        a = input()
        if(a==""):
            break
        print(a)
    except EOFError:
        break