from game.Process import state_info, transition, Process


def main():
    UP = 'goes up'
    DOWN = 'goes down'
    LEFT = 'goes left'
    RIGHT = 'goes right'
    STOP = 'stops'

    p1, p2 = Process('Snake1'), Process('Snake2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.stop, STOP)
    transition(p2, p2.stop, STOP)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.down, DOWN)
    transition(p2, p2.up, UP)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.left, LEFT)
    transition(p2, p2.right, RIGHT)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.stop, STOP)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.stop, STOP)
    [state_info(p) for p in (p1, p2)]


if __name__ == '__main__':
    main()
