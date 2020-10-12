from state_machine import acts_as_state_machine, after, before, InvalidStateTransition, Event, State


@acts_as_state_machine
class Process:
    created = State(initial=True)
    goes_up = State()
    goes_down = State()
    goes_left = State()
    goes_right = State()
    stops = State()

    stop = Event(from_states=(created, goes_up, goes_down, goes_left, goes_right), to_state=stops)
    down = Event(from_states=(goes_up, stops), to_state=goes_down)
    up = Event(from_states=(goes_down, stops), to_state=goes_up)
    left = Event(from_states=(goes_up, goes_down, goes_right, stops), to_state=goes_left)
    right = Event(from_states=(goes_up, goes_down, goes_left, stops), to_state=goes_right)

    def __init__(self, name):
        self.name = name

    @after('up')
    def up_info(self):
        print(f'{self.name} goes up')

    @after('down')
    def down_info(self):
        print(f'{self.name} goes down')

    @after('left')
    def left_info(self):
        print(f'{self.name} goes left')

    @after('right')
    def right_info(self):
        print(f'{self.name} goes right')

    @before('stop')
    def stop_info(self):
        print(f'{self.name} stops')


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print(f'Error: transition of {process.name} from {process.current_state} to {event_name} failed')


def state_info(process):
    print(f'state of {process.name}: {process.current_state}')
