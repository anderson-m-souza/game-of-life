from life import main, next_board_state, render


def next_board_state_tests():

    def test_state(initial, expected, name):
        actual_state = next_board_state(initial)

        if expected == actual_state:
            print("Passed", end=". ")
        else:
            print("Failed", end=". ")
        print(name)

        print("Initial state:")
        render(initial)

        print("Expected state:")
        render(expected)

        print("Actual state:")
        render(actual_state)

        print(end='\n')
        

    name1 = "Any dead cell with 0 live neighbors should remain dead."
    initial_state1 = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
    ]
    expected_state1 = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
    ]
    test_state(initial_state1, expected_state1, name1)
 
    name2 = "Any live cell with 0 live neighbors should become dead."
    initial_state2 = [
            [1,0,1,0,1],
            [0,0,0,0,0],
            [1,0,1,0,1],
            [0,0,0,0,0],
            [1,0,1,0,1]
    ]
    expected_state2 = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
    ]
    test_state(initial_state2, expected_state2, name2)
 
    name3 = "Any live cell with 1 live neighbor should become dead."
    initial_state3 = [
            [1,1,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
            [1,0,0,0],
            [1,0,0,0],
            [0,0,0,1],
            [0,0,1,0]
    ]
    expected_state3 = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
    ]
    test_state(initial_state3, expected_state3, name3)
    
    name4 = ("Any dead cell with 3 live neighbors should become alive. "
             "Any live cell with 2 live neighbors should stay alive.")
    initial_state4 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_state4 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    test_state(initial_state4, expected_state4, name4)

    name5 = ("Any live cell with 3 live neighbors should stay alive. "
             "Any live cell with more than 3 live neighbors should become dead.")
    initial_state5 = [
        [1,1,1],
        [1,1,1],
        [0,0,1]
    ]
    expected_state5 = [
        [1,0,1],
        [1,0,0],
        [0,0,1]
    ]
    test_state(initial_state5, expected_state5, name5)

 
def main(): 
    print("Running next_board_state tests...", end="\n\n")
    next_board_state_tests()


if __name__ == "__main__":
    main()
