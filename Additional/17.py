def diceCombo():
    # your code here
    d = {}

    # Loop with d1 from 1 to 6
    for d1 in range(1,7):
        #Loop with d2 from 1 to 6
        for d2 in range (1,7):
            #newTuple <- ( d1, d2 ) # create the tuple
            sum = d1 + d2
            newTuple = (d1,d2)
            d[newTuple]=sum
    return d

def diceOdds(diceComboDict):
    # your code here
    odds={}
    for k in diceComboDict:
        for i in k:
            if i % 2 != 0:
                odds[k] = diceComboDict[k]
    return odds

def main():
    # your test code here
    dice_combo_dict = diceCombo()
    dice_odds = diceOdds(dice_combo_dict)
    print(dice_odds)

if __name__ == "__main__":
    main()