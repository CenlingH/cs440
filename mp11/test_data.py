actions_list = [
    [3, 3, 3, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1, 1, 3, 3, 0, 0, 0, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 2, 2, 2, 2, 2, 0, 3, 3,
     3, 2, 2],
    [3, 3, 3, 2, 2, 2, 2, 2, 0, 0, 0, 2, 1, 1, 3, 3, 0, 0, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 3, 0, 0, 0, 0, 2,
     2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0,
     3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 1],
    [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [3, 3, 3, 3, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
        1, 1, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0],
    [3, 3, 3, 3, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 1, 3, 3, 0, 0, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0,
     0, 2, 2, 2],
    [3, 3, 3, 3, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 2, 2, 2, 2,
     1, 1, 3, 3, 3, 3, 3, 3, 0, 0, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 3, 3, 3, 1, 1, 2, 2, 2, 2, 2, 2,
     2, 2, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 0, 0, 2, 2, 2, 2]
]

envs = [
    [1, 1, [(2, 1), (3, 1)], 6, 7, 1, 2], [1, 1, [(2, 1), (3, 1)],
                                           16, 2, 1, 2], [1, 1, [(2, 1), (3, 1)], 9, 5, 1, 2],
    [1, 1, [(2, 1), (3, 1)], 5, 2, 1, 2], [
        1, 1, [(2, 1), (2, 2), (1, 2)], 14, 3, 3, 3],
    [1, 1, [(2, 1), (2, 2), (1, 2)], 14, 7, 3, 3], [
        1, 1, [(2, 1), (2, 2), (1, 2)], 1, 6, 3, 3],
    [1, 1, [(2, 1), (2, 2), (1, 2)], 5, 7, 3, 3], [
        1, 1, [(1, 2), (1, 3)], 2, 7, 2, 1],
    [1, 1, [(1, 2), (1, 3)], 12, 8, 2, 1], [1, 1, [(1, 2), (1, 3)],
                                            7, 8, 2, 1], [1, 1, [(1, 2), (1, 3)], 5, 1, 2, 1],
    [1, 5, [(1, 4), (1, 3)], 15, 3, 2, 5], [1, 5, [(1, 4), (1, 3)],
                                            4, 5, 2, 5], [1, 5, [(1, 4), (1, 3)], 10, 1, 2, 5],
    [1, 5, [(1, 4), (1, 3)], 1, 6, 2, 5], [1, 5, [(2, 5), (3, 5)],
                                           10, 6, 1, 4], [1, 5, [(2, 5), (3, 5)], 3, 4, 1, 4],
    [1, 5, [(2, 5), (3, 5)], 11, 3, 1, 4], [1, 5, [(2, 5), (3, 5)],
                                            6, 4, 1, 4], [1, 5, [(1, 6), (1, 7)], 9, 4, 2, 5],
    [1, 5, [(1, 6), (1, 7)], 4, 7, 2, 5], [1, 5, [(1, 6), (1, 7)],
                                           9, 2, 2, 5], [1, 5, [(1, 6), (1, 7)], 12, 1, 2, 5],
    [1, 8, [(1, 7), (1, 6)], 15, 8, 2, 8], [1, 8, [(1, 7), (1, 6)],
                                            2, 7, 2, 8], [1, 8, [(1, 7), (1, 6)], 11, 4, 2, 8],
    [1, 8, [(1, 7), (1, 6)], 15, 6, 2, 8], [1, 8, [(2, 8), (3, 8)],
                                            16, 6, 4, 8], [1, 8, [(2, 8), (3, 8)], 6, 4, 4, 8],
    [1, 8, [(2, 8), (3, 8)], 3, 2, 4, 8], [1, 8, [(2, 8), (3, 8)],
                                           7, 7, 4, 8], [9, 1, [(10, 1), (11, 1)], 2, 4, 5, 5],
    [9, 1, [(10, 1), (11, 1)], 3, 3, 5, 5], [
        9, 1, [(10, 1), (11, 1)], 6, 2, 5, 5],
    [9, 1, [(10, 1), (11, 1)], 3, 6, 5, 5], [9, 1, [(8, 1), (7, 1)],
                                             10, 8, 5, 5], [9, 1, [(8, 1), (7, 1)], 6, 6, 5, 5],
    [9, 1, [(8, 1), (7, 1)], 9, 4, 5, 5], [9, 1, [(8, 1), (7, 1)],
                                           3, 5, 5, 5], [9, 1, [(9, 2), (9, 3)], 14, 2, 5, 5],
    [9, 1, [(9, 2), (9, 3)], 15, 5, 5, 5], [9, 1, [(9, 2), (9, 3)],
                                            5, 4, 5, 5], [9, 1, [(9, 2), (9, 3)], 12, 4, 5, 5],
    [9, 5, [(9, 4), (9, 3)], 4, 4, 5, 5], [9, 5, [(9, 4), (9, 3)],
                                           9, 6, 5, 5], [9, 5, [(9, 4), (9, 3)], 12, 8, 5, 5],
    [9, 5, [(9, 4), (9, 3)], 11, 8, 5, 5], [
        9, 5, [(10, 5), (11, 5)], 12, 6, 5, 5],
    [9, 5, [(10, 5), (11, 5)], 6, 3, 5, 5], [
        9, 5, [(10, 5), (11, 5)], 15, 5, 5, 5],
    [9, 5, [(10, 5), (11, 5)], 11, 2, 5, 5], [9, 5, [(8, 5), (7, 5)],
                                              2, 1, 5, 5], [9, 5, [(8, 5), (7, 5)], 5, 7, 5, 5],
    [9, 5, [(8, 5), (7, 5)], 9, 2, 5, 5], [9, 5, [(8, 5), (7, 5)],
                                           10, 7, 5, 5], [9, 5, [(9, 6), (9, 7)], 6, 1, 5, 5],
    [9, 5, [(9, 6), (9, 7)], 1, 8, 5, 5], [9, 5, [(9, 6), (9, 7)],
                                           4, 7, 5, 5], [9, 5, [(9, 6), (9, 7)], 9, 4, 5, 5],
    [9, 5, [(10, 5), (10, 6), (9, 6), (8, 6), (8, 5),
            (8, 4), (9, 4), (10, 4)], 6, 7, 5, 5],
    [9, 5, [(10, 5), (10, 6), (9, 6), (8, 6), (8, 5),
            (8, 4), (9, 4), (10, 4)], 13, 7, 5, 5],
    [9, 5, [(10, 5), (10, 6), (9, 6), (8, 6), (8, 5),
            (8, 4), (9, 4), (10, 4)], 10, 3, 5, 5],
    [9, 5, [(10, 5), (10, 6), (9, 6), (8, 6), (8, 5),
            (8, 4), (9, 4), (10, 4)], 3, 2, 5, 5],
    [9, 8, [(9, 7), (9, 6)], 7, 3, 5, 5], [9, 8, [(9, 7), (9, 6)],
                                           9, 4, 5, 5], [9, 8, [(9, 7), (9, 6)], 1, 2, 5, 5],
    [9, 8, [(9, 7), (9, 6)], 10, 3, 5, 5], [
        9, 8, [(10, 8), (11, 8)], 3, 5, 5, 5],
    [9, 8, [(10, 8), (11, 8)], 3, 6, 5, 5], [
        9, 8, [(10, 8), (11, 8)], 16, 8, 5, 5],
    [9, 8, [(10, 8), (11, 8)], 9, 3, 5, 5], [
        9, 8, [(8, 8), (7, 8)], 12, 2, 5, 5],
    [9, 8, [(8, 8), (7, 8)], 10, 7, 5, 5], [9, 8, [(8, 8), (7, 8)],
                                            1, 6, 5, 5], [9, 8, [(8, 8), (7, 8)], 7, 2, 5, 5],
    [16, 1, [(15, 1), (14, 1)], 14, 3, 14, 2], [
        16, 1, [(15, 1), (14, 1)], 9, 7, 14, 2],
    [16, 1, [(15, 1), (14, 1)], 12, 3, 14, 2], [
        16, 1, [(15, 1), (14, 1)], 8, 8, 14, 2],
    [16, 1, [(16, 2), (16, 3)], 11, 4, 14, 5], [
        16, 1, [(16, 2), (16, 3)], 2, 6, 14, 5],
    [16, 1, [(16, 2), (16, 3)], 6, 5, 14, 5], [
        16, 1, [(16, 2), (16, 3)], 9, 2, 14, 5],
    [16, 5, [(16, 4), (16, 3)], 15, 8, 14, 6], [
        16, 5, [(16, 4), (16, 3)], 9, 7, 14, 6],
    [16, 5, [(16, 4), (16, 3)], 3, 2, 14, 6], [
        16, 5, [(16, 4), (16, 3)], 14, 8, 14, 6],
    [16, 5, [(15, 5), (14, 5)], 3, 5, 14, 4], [
        16, 5, [(15, 5), (14, 5)], 10, 3, 14, 4],
    [16, 5, [(15, 5), (14, 5)], 2, 1, 14, 4], [
        16, 5, [(15, 5), (14, 5)], 5, 5, 14, 4],
    [16, 5, [(16, 6), (16, 7)], 8, 7, 14, 5], [
        16, 5, [(16, 6), (16, 7)], 16, 2, 14, 5],
    [16, 5, [(16, 6), (16, 7)], 3, 8, 14, 5], [
        16, 5, [(16, 6), (16, 7)], 1, 7, 14, 5],
    [16, 8, [(16, 7), (16, 6)], 10, 2, 14, 7], [
        16, 8, [(16, 7), (16, 6)], 4, 7, 14, 7],
    [16, 8, [(16, 7), (16, 6)], 2, 3, 14, 7], [
        16, 8, [(16, 7), (16, 6)], 14, 1, 14, 7],
    [16, 8, [(15, 8), (14, 8)], 12, 8, 5, 5], [
        16, 8, [(15, 8), (14, 8)], 15, 3, 5, 5],
    [16, 8, [(15, 8), (14, 8)], 4, 5, 5, 5], [
        16, 8, [(15, 8), (14, 8)], 15, 7, 5, 5],
    [16, 8, [(15, 8), (15, 7), (16, 7)], 7, 2, 5, 5], [
        16, 8, [(15, 8), (15, 7), (16, 7)], 5, 6, 5, 5],
    [16, 8, [(15, 8), (15, 7), (16, 7)], 1, 2, 5, 5], [
        16, 8, [(15, 8), (15, 7), (16, 7)], 14, 8, 5, 5]
]

discret_results = [
    (2, 2, 1, 1, 0, 0, 0, 1), (2, 2, 1, 1, 0, 0, 0, 1), (2,
                                                         2, 1, 1, 0, 0, 0, 1), (2, 2, 1, 1, 0, 0, 0, 1),
    (2, 2, 1, 1, 0, 1, 0, 1), (2, 2, 1, 1, 0, 1, 0, 1), (0,
                                                         2, 1, 1, 0, 1, 0, 1), (2, 2, 1, 1, 0, 1, 0, 1),
    (2, 2, 1, 1, 0, 1, 0, 0), (2, 2, 1, 1, 0, 1, 0, 0), (2,
                                                         2, 1, 1, 0, 1, 0, 0), (2, 0, 1, 1, 0, 1, 0, 0),
    (2, 1, 1, 0, 1, 0, 0, 0), (2, 0, 1, 0, 1, 0, 0, 0), (2,
                                                         1, 1, 0, 1, 0, 0, 0), (0, 2, 1, 0, 1, 0, 0, 0),
    (2, 2, 1, 1, 0, 0, 0, 1), (2, 1, 1, 1, 0, 0, 0, 1), (2,
                                                         1, 1, 1, 0, 0, 0, 1), (2, 1, 1, 1, 0, 0, 0, 1),
    (2, 1, 1, 0, 0, 1, 0, 0), (2, 2, 1, 0, 0, 1, 0, 0), (2,
                                                         1, 1, 0, 0, 1, 0, 0), (2, 1, 1, 0, 0, 1, 0, 0),
    (2, 0, 1, 2, 1, 0, 0, 0), (2, 1, 1, 2, 1, 0, 0, 0), (2,
                                                         1, 1, 2, 1, 0, 0, 0), (2, 1, 1, 2, 1, 0, 0, 0),
    (2, 1, 1, 2, 0, 0, 0, 1), (2, 1, 1, 2, 0, 0, 0, 1), (2,
                                                         1, 1, 2, 0, 0, 0, 1), (2, 1, 1, 2, 0, 0, 0, 1),
    (1, 2, 0, 1, 0, 0, 0, 1), (1, 2, 0, 1, 0, 0, 0, 1), (1,
                                                         2, 0, 1, 0, 0, 0, 1), (1, 2, 0, 1, 0, 0, 0, 1),
    (2, 2, 0, 1, 0, 0, 1, 0), (1, 2, 0, 1, 0, 0, 1, 0), (0,
                                                         2, 0, 1, 0, 0, 1, 0), (1, 2, 0, 1, 0, 0, 1, 0),
    (2, 2, 0, 1, 0, 1, 0, 0), (2, 2, 0, 1, 0, 1, 0, 0), (1,
                                                         2, 0, 1, 0, 1, 0, 0), (2, 2, 0, 1, 0, 1, 0, 0),
    (1, 1, 0, 0, 1, 0, 0, 0), (0, 2, 0, 0, 1, 0, 0, 0), (2,
                                                         2, 0, 0, 1, 0, 0, 0), (2, 2, 0, 0, 1, 0, 0, 0),
    (2, 2, 0, 0, 0, 0, 0, 1), (1, 1, 0, 0, 0, 0, 0, 1), (2,
                                                         0, 0, 0, 0, 0, 0, 1), (2, 1, 0, 0, 0, 0, 0, 1),
    (1, 1, 0, 0, 0, 0, 1, 0), (1, 2, 0, 0, 0, 0, 1, 0), (0,
                                                         1, 0, 0, 0, 0, 1, 0), (2, 2, 0, 0, 0, 0, 1, 0),
    (1, 1, 0, 0, 0, 1, 0, 0), (1, 2, 0, 0, 0, 1, 0, 0), (1,
                                                         2, 0, 0, 0, 1, 0, 0), (0, 1, 0, 0, 0, 1, 0, 0),
    (1, 2, 0, 0, 1, 1, 1, 1), (2, 2, 0, 0, 1, 1, 1, 1), (2,
                                                         1, 0, 0, 1, 1, 1, 1), (1, 1, 0, 0, 1, 1, 1, 1),
    (1, 1, 0, 2, 1, 0, 0, 0), (0, 1, 0, 2, 1, 0, 0, 0), (1,
                                                         1, 0, 2, 1, 0, 0, 0), (2, 1, 0, 2, 1, 0, 0, 0),
    (1, 1, 0, 2, 0, 0, 0, 1), (1, 1, 0, 2, 0, 0, 0, 1), (2,
                                                         0, 0, 2, 0, 0, 0, 1), (0, 1, 0, 2, 0, 0, 0, 1),
    (2, 1, 0, 2, 0, 0, 1, 0), (2, 1, 0, 2, 0, 0, 1, 0), (1,
                                                         1, 0, 2, 0, 0, 1, 0), (1, 1, 0, 2, 0, 0, 1, 0),
    (1, 2, 2, 1, 0, 0, 1, 0), (1, 2, 2, 1, 0, 0, 1, 0), (1,
                                                         2, 2, 1, 0, 0, 1, 0), (1, 2, 2, 1, 0, 0, 1, 0),
    (1, 2, 2, 1, 0, 1, 0, 0), (1, 2, 2, 1, 0, 1, 0, 0), (1,
                                                         2, 2, 1, 0, 1, 0, 0), (1, 2, 2, 1, 0, 1, 0, 0),
    (1, 2, 2, 0, 1, 0, 0, 0), (1, 2, 2, 0, 1, 0, 0, 0), (1,
                                                         1, 2, 0, 1, 0, 0, 0), (1, 2, 2, 0, 1, 0, 0, 0),
    (1, 0, 2, 0, 0, 0, 1, 0), (1, 1, 2, 0, 0, 0, 1, 0), (1,
                                                         1, 2, 0, 0, 0, 1, 0), (1, 0, 2, 0, 0, 0, 1, 0),
    (1, 2, 1, 0, 0, 1, 0, 0), (0, 1, 1, 0, 0, 1, 0, 0), (1,
                                                         2, 1, 0, 0, 1, 0, 0), (1, 2, 1, 0, 0, 1, 0, 0),
    (1, 1, 2, 2, 1, 0, 0, 0), (1, 1, 2, 2, 1, 0, 0, 0), (1,
                                                         1, 2, 2, 1, 0, 0, 0), (1, 1, 2, 2, 1, 0, 0, 0),
    (1, 0, 2, 2, 0, 0, 1, 0), (1, 1, 2, 2, 0, 0, 1, 0), (1,
                                                         1, 2, 2, 0, 0, 1, 0), (1, 1, 2, 2, 0, 0, 1, 0),
    (1, 1, 2, 2, 1, 0, 1, 0), (1, 1, 2, 2, 1, 0, 1,
                               0), (1, 1, 2, 2, 1, 0, 1, 0), (1, 0, 2, 2, 1, 0, 1, 0)
]