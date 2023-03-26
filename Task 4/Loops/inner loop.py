for i in range(5):
    for j in range(5):
        if i*j == 6:
            print("Breaking inner loop")
            break
    print("Breaking outer loop")
    break
