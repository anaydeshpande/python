def check_inventory(inventory, low):
    list = []
    for k in inventory:
        value = inventory['%s' % k]
        print(value)
        if low:
            print(low)
            if value < low:
                list.append(k)
                print(list)
    return sorted(list)


def main():
    inventory = {'apple': 10, 'banana': 3}
    sorted_list = check_inventory(inventory, 2)
    print(sorted_list)

if __name__ == "__main__":
    main()