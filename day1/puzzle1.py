"""
--- Day 1: Sonar Sweep ---
"""

def data_to_list(data_file):
    """
    Get data
    """
    output = []
    with open(data_file) as f:
        data = f.readlines()
        for line in data:
            output.append(int(line.strip()))
    return output

def solver(data, slide_window=3):
    """
    :param data: list of ints
    :param slide_window: int
    :return: int
    """
    count = 0
    for index, _ in enumerate(data[:-slide_window]):
        current_window = data[index:index+slide_window]
        next_window = data[index+ 1:index+slide_window+1]
        if sum(current_window) < sum(next_window):
            count +=1
            print(f"{current_window} is greater than {next_window}")
    return count

if __name__ == "__main__":
    data = data_to_list("data.txt")
    count = solver(data)
    print(count)
