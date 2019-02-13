
def countAll(text):
    # your code here
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict={}
    for char in text:
        if char in ups:
            char = char.lower()
            if char in dict:
                dict["%s" %char]= dict["%s" %char] +1
            else:
                dict["%s" %char] = 1
        elif char in lows:
            if char in dict:
                dict["%s" %char]= dict["%s" %char] +1
            else:
                dict["%s" %char] = 1
    return dict

def main():
    # your test code here
    dict = countAll("BaNaNa")
    print dict

if __name__ == "__main__":
    main()