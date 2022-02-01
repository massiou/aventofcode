def data_convert(data_file):
    grids_list = []
    with open(data_file, 'r') as f:
        data = f.readlines()
        output_number = data[0].split(",")
        for line in data[1:]:
            if line != "\n":
                line = line.split()
                grids_list.append(line)
    
    return output_number, grids_list


class Grid(object):
    def __init__(self, grid):
        self.grid = grid
        self.grid_size = len(grid)

    def is_number_in_grid(self, number):
        for i in range(len(self)):
            for j in range(len(self)):
                if grid[i][j] == number:
                    return True
                return True
        return False


if __name__ == '__main__':
    data_file = 'data.txt'
    output_number, grids_list = data_convert(data_file)
    for gr in grids_list:
        grid = Grid(gr)

    print(output_number)
    print(grids_list)