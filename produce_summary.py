def print_produce_summary(the_file):
    the_file = open(the_file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))

    the_file.close()

print("Day 1")
print_produce_summary("um-deliveries-20140519.txt")

print("Day 2")
print_produce_summary("um-deliveries-20140520.txt")

print("Day 3")
print_produce_summary("um-deliveries-20140521.txt")

