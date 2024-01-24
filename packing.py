def can_fit(items, num_bags):
    bags = [0] * num_bags
    items.sort(reverse = True)

    for item in items:
        lightest_bag_index = bags.index(min(bags))

        if bags[lightest_bag_index] + item > 100:
            return False

        bags[lightest_bag_index] += item

    return True

print(can_fit([100, 100, 100, 100, 100], 5))
