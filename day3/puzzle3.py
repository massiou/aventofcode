def data_to_list(data_file):
    """
    Get data
    """
    output = []
    with open(data_file) as f:
        data = f.readlines()
        for line in data:
            current_diag = line.strip()
            output.append(current_diag)
    return output


def computation(data):
    """"
    :param data: [description]
    :type data: [type]
    """
    # Initialize variables
    lenght = len(data)
    output = [0] * len(data[0])
    for c_data in data:
        for index, number in enumerate(c_data):
            output[index] += int(number)

    gamma = [1 if x > lenght/2 else 0 for x in output]
    epsilon = [0 if x > lenght/2 else 1 for x in output]

    gamma = ''.join(str(x) for x in gamma)
    epsilon = ''.join(str(x) for x in epsilon)
    print(int(gamma, 2) * int(epsilon, 2))
    return output, int(gamma, 2), int(epsilon, 2)


def get_most_common(data, index=0):
    """
    :param data: [description]
    :type data: [type]
    :param index: [description]
    :type index: [type]
    """
    # Initialize variables
    if not data:
        raise Exception(f"No data to process")

    lenght = len(data)
    output = [0] * len(data[0])
    for c_data in data:
        output[index] += int(c_data[index])
    most_common = 1 if output[index] >= lenght/2 else 0 

    r_data = keep_data(most_common, index, data)

    return int(most_common), r_data

def get_less_common(data, index=0):
    """
    :param data: [description]
    :type data: [type]
    :param index: [description]
    :type index: [type]
    """
    if not data:
        raise Exception(f"No data to process")
    # Initialize variables
    lenght = len(data)
    output = [0] * len(data[0])
    for c_data in data:
        output[index] += int(c_data[index])

    less_common = 0 if output[index] <= lenght/2 else 1 

    r_data = keep_data(less_common, index, data)

    return int(less_common), r_data

def keep_data(bit_criteria, bit_index, data):
    """
    :param criteria: [description]
    :type criteria: [type]
    """
    output = []
    for c_data in data:
        if int(c_data[bit_index]) == bit_criteria:
            output.append(c_data)
    return output


if __name__ == "__main__":
    data = data_to_list("data.txt")
    k = data
    output = [0] * len(data[0].strip())
    while len(k) > 1:
        print(len(k))
        for index in range(len(output)):
            m, k = get_most_common(k, index)
    oxy_gen = int(k[0], 2)
    print(oxy_gen)

    k = data
    output = [0] * len(data[0].strip())
    while len(k) > 1:
        print(len(k))
        for index in range(len(output)):
            m, k = get_less_common(k, index)
    co2 = int(k[0], 2)

    print(oxy_gen * co2)

