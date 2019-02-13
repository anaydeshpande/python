
oldList=[]
def diceCombo():
    # your code here
    d = {}
    newList=[]
    # Loop with d1 from 1 to 6
    for d1 in range(1,7):
        #Loop with d2 from 1 to 6
        for d2 in range (1,7):
            #newTuple <- ( d1, d2 ) # create the tuple
            sum = d1 + d2
            oldList.append(sum)
            newtuple = (d1,d2)
            newList = sum + newtuple


    print "NewList",newList
    return d

def diceOdds(diceComboDict):
    # your code here
    odds={}
    for k in diceComboDict:
        value = len(diceComboDict)/36
        odds[k] = value
    return odds

def main():
    # your test code here
    dice_combo_dict = diceCombo()
    dice_odds = diceOdds(dice_combo_dict)
    print(dice_odds)

if __name__ == "__main__":
    main()

