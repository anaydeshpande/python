def check_inventory(inventory, low):
    list=[]
    # your code here
    for i in inventory:
        val = inventory['%s' %i]
        if val < low:
            list.append(i)
    return list

def main():
    # your test code here
    anay_inventory = {"apple": 10, "banana": 3}
    inventory_list = check_inventory(anay_inventory,6)

if __name__ == "__main__":
    main()