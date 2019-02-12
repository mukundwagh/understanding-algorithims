import datetime
import sys

def min_coins(coins, amount, tree, dp):
    all_nodes = {}

    if amount <=0 :
        return tree
    else:
        if dp and amount in tree.keys():
            return tree
        else:
            min = sys.maxsize
            for c in coins:
                if amount < c:
                    all_nodes[c] = sys.maxsize

                elif amount == c:
                    all_nodes[c] = 1
                else:
                    tree = min_coins(coins, amount - c, tree, dp)
                    all_nodes[c] = 1 + tree[amount-c]

                if all_nodes[c] < min:
                    min = all_nodes[c]
            tree[amount] = min
            print(amount, min)
    return tree


if __name__ == '__main__':
    coins = [1]
    amount = 0
    tree = {}

    # a = datetime.datetime.now()
    # print(min_coins(coins, amount, tree, False))
    # b = datetime.datetime.now()
    # print("--- %s millli seconds ---" % ((b - a).total_seconds()*1000))

    c = datetime.datetime.now()
    print(min_coins(coins, amount, tree, True)[amount])
    d = datetime.datetime.now()
    print("--- %s millli seconds ---" % ((d - c).total_seconds() * 1000))
