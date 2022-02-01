def data_to_list(data_file):
    """
    Get data
    """
    output = []
    with open(data_file) as f:
        data = f.readlines()
        for line in data:
            command, value = line.split()
            output.append((command, int(value)))
    return output


def move(horizontal, depth, aim, command, value):
    """
    Move the position
    """
    if command == 'forward':
        horizontal += value
        depth += value * aim
    elif command == 'down':
        aim += value
    elif command == 'up':
        aim -= value
        print(aim)
    return horizontal, depth, aim



if __name__ == "__main__":
    data = data_to_list("data.txt")
    print(data)

    horizontal, depth, aim = (0, 0, 0)
    for command, value in data:
        horizontal, depth, aim = move(horizontal, depth, aim, command, value)
        print(horizontal, depth, aim)
