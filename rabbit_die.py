
def mortal_rabbits(n):
    sequence = [1, 1]
    m = 4

    for i in range(n - 2):
        new_num = 0
        if i + 2 < m:
            #Normal fibonacci - No deaths yet
            new_num = sequence[i] + sequence[i + 1]
        else:
            #Different reoccurence relation - Accounting for death
            for j in range(m - 1):
                new_num += sequence[i - j]

        sequence.append(new_num)

    return sequence

def main():
    print mortal_rabbits(12)

if __name__ == "__main__":
    main()



