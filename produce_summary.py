def print_produce_summary(the_file):
    '''Takes a file and prints a report of melons delivered'''

    # Open file
    the_file = open(the_file)
    # For each line in the file
    for line in the_file:
        # Remove trailing whitespace
        line = line.rstrip()
        # Tokenize string by splitting at "|"
        words = line.split('|')

        # Assign tokens to variables
        # Type of melon
        melon = words[0]
        # Number of melons
        count = words[1]
        # Price of melons
        amount = words[2]

        # Print statement describing type, number, and price of melons in delivery
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))

    # Close the file
    the_file.close()

# Print Day 1 produce summary
print("Day 1")
print_produce_summary("um-deliveries-20140519.txt")

# Print Day 2 produce summary
print("Day 2")
print_produce_summary("um-deliveries-20140520.txt")

# Print Day 3 produce summary
print("Day 3")
print_produce_summary("um-deliveries-20140521.txt")

