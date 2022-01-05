import math

def get_adjacent_coords(coord, matrix_size, include_diagonal=False):
    # (1,1) -> x +1 and -1, x +1 and -1    (1,0),(1,2),(0,1),(2,1)
    # include diagonal -> x (0,0),(0,2),(2,0),(2,2)
    (x, y) = coord
    [x_max, y_max] = [i - 1 for i in matrix_size]
    if include_diagonal:
        adjacent_coords = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1),
                           (x - 1, y + 1), (x - 1, y)]
    else:
        adjacent_coords = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    return [item for item in adjacent_coords if item[0] >= 0 and item[1] >= 0 and item[0] <= x_max and item[1] <= y_max]


def get_distance(path):
    distance = 0
    for p_idx in range(len(path) - 1):
        x1 = path[p_idx][0]
        y1 = path[p_idx][1]
        x2 = path[p_idx + 1][0]
        y2 = path[p_idx + 1][1]
        distance = distance + math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 4)


def get_all_paths(matrix, origin=(0, 0), destination=(6, 6), include_diagonal=False):
    matrix_size = (len(matrix[0]), len(matrix))
    list_of_paths = [[origin]]
    list_of_new_paths = []
    while True:
        for path in list_of_paths:
            last_coord = path[-1]
            if last_coord == destination:
                list_of_new_paths.append(path)
            else:
                adjacent_coords = get_adjacent_coords(last_coord, matrix_size, include_diagonal)
                for adjacent_coord in adjacent_coords:
                    if matrix[adjacent_coord[1]][adjacent_coord[0]] and adjacent_coord not in path:
                        new_path = path.copy()
                        new_path.append(adjacent_coord)
                        list_of_new_paths.append(new_path)
        if list_of_paths == list_of_new_paths:
            break
        else:
            list_of_paths = list_of_new_paths.copy()
            list_of_new_paths = []
    all_paths_distance = [(get_distance(path) if include_diagonal else len(path) - 1, path) for path in list_of_paths]
    all_paths_distance.sort(key=lambda x: x[0])
    return all_paths_distance # returns a list of tuples of (distance, path)


def get_shortest_path(all_paths_distance):
    shortest_path = [path_tuple for path_tuple in all_paths_distance if path_tuple[0] == all_paths_distance[0][0]]
    return shortest_path


def get_longest_path(all_paths_distance):
    longest_path = [path_tuple for path_tuple in all_paths_distance if path_tuple[0] == all_paths_distance[-1][0]]
    return longest_path

if __name__ == '__main__':
    matrix = [[1, 1, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0, 1]]
    all_paths = get_all_paths(matrix, destination=(2,6))
    shortest_path = get_shortest_path(all_paths)
    print(shortest_path)
    
