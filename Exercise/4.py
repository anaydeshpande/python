# Based on above problem we will have following number of rabbits
# Plugin n =1 (for January), n=2 (for Feb and so on) in above problem 3 and you will get following
# month | No. of rabbits (population)
# 1     | 1
# 2     | 1
# 3     | 2
# 4     | 3
# 5     | 5
# 6     | 8
# 7     | 13
# 8     | 21
# 9     | 34
#10     | 55
#11     | 89
#12     | 144

# Function to find how many rabbits will be there after n months
# rabbits live only 4 months

def fibDieEvery4(n):
    # female rabbits live for only 4 months
    m = 4
    # female rabbit is mature 2 months after birth
    if n < 3:
        return 1
    elif n <= m:
        return fibDieEvery4(n-1) + fibDieEvery4(n-2)
    else:
        return fibDieEvery4(n-1) + fibDieEvery4(n-2) - fibDieEvery4(n-5)

def main():
    no_of_rabbits_remain = fibDieEvery4(5)
    print(no_of_rabbits_remain)

if __name__ == "__main__":
    main()