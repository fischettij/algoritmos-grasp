from grasp import Solution, _get_adyecents_not_visited, insert_sorted_list, mod_index, selection, local_search

def test_get_adyecents_not_visited():
    matrix = [
        [0,2,6,2],
        [3,0,3,1],
        [99,3,0,1],
        [23,7,9,0],
    ]

    result = _get_adyecents_not_visited(matrix,2,[False, False, False, False])
    expected = [
        (2,3,1),
        (2,1,3),
        (2,0,99),
    ]
    assert result == expected

    result = _get_adyecents_not_visited(matrix,2,[False, True, False, False])
    expected = [
        (2,3,1),
        (2,0,99),
    ]
    assert result == expected


def test_selection():
    selection_strategy = selection(3, 50)

    input = [0 for i in range(10)]
    result = selection_strategy(input)
    expected = 5
    assert expected == len(result)

    input = [0 for i in range(4)]
    result = selection_strategy(input)
    expected = 3
    assert expected == len(result)

    input = [0 for i in range(3)]
    result = selection_strategy(input)
    expected = 3
    assert expected == len(result)

    input = [0 for i in range(2)]
    result = selection_strategy(input)
    expected = 2
    assert expected == len(result)

def test_mod_index():
    a = [0,1,2]
    actual = mod_index(0,len(a),1)
    assert actual == 1

    actual = mod_index(1,len(a),1)
    assert actual == 2

    actual = mod_index(2,len(a),1)
    assert actual == 0

    # in this case 3 is over the array but the function works because index 3 is like index 0
    actual = mod_index(3,len(a),1)
    assert actual == 1

def test_local_search():
    m = [
        [0, 9, 1, 5, 1],
        [9, 0, 8, 2, 3],
        [1, 8, 0, 9, 6],
        [5, 2, 9, 0, 2],
        [1, 3, 6, 2, 0],
    ]
    cost = 28
    solution = Solution([0,1,2,3,4], cost)
    new_solution = local_search(m, solution, 1)
    assert new_solution.road == [1,0,2,3,4]
    assert new_solution.cost == 23

def test_insert_sorted_list():
    lst = []
    insert_sorted_list(lst, (0,0,7))
    insert_sorted_list(lst, (0,0,3))
    insert_sorted_list(lst, (0,0,5))
    insert_sorted_list(lst, (0,0,9))
    insert_sorted_list(lst, (0,0,4))
    insert_sorted_list(lst, (0,0,1))
    insert_sorted_list(lst, (0,0,6))
    insert_sorted_list(lst, (0,0,8))
    insert_sorted_list(lst, (0,0,2))
    insert_sorted_list(lst, (0,0,0))
    expected = [
        (0,0,0),
        (0,0,1),
        (0,0,2),
        (0,0,3),
        (0,0,4),
        (0,0,5),
        (0,0,6),
        (0,0,7),
        (0,0,8),
        (0,0,9)
    ]
    assert lst == expected