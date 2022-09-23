import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-W", type=int)
parser.add_argument("-w", type=int, nargs='+')

args = parser.parse_args()

Weight = args.w
capacity = args.W

sums = []


def optimal_weight(Weight, capacity, patrial=[]):
    s = sum(patrial)
    if s <= capacity:
        sums.append(s)
    for i in range(len(Weight)):
        n = Weight[i]
        remaining = Weight[i + 1:]
        optimal_weight(remaining, capacity, patrial + [n])


if __name__ == '__main__':
    optimal_weight(Weight, capacity)

    
