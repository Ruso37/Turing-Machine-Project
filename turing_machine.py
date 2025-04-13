
class TuringMachine:
    def __init__(self, 
                 states, 
                 input_symbols, 
                 tape_symbols, 
                 transitions, 
                 start_state, 
                 blank_symbol, 
                 accept_state, 
                 reject_state):
        self.states = states
        self.input_symbols = input_symbols
        self.tape_symbols = tape_symbols
        self.transitions = transitions  # Dict in the form: {(state, symbol): (new_state, new_symbol, direction)}
        self.start_state = start_state
        self.blank_symbol = blank_symbol
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.reset()

    def reset(self):
        self.current_state = self.start_state
        self.tape = []
        self.head_position = 0

    def load_tape(self, input_string):
        self.tape = list(input_string) + [self.blank_symbol] * 10
        self.head_position = 0
        self.current_state = self.start_state

    def step(self):
        symbol = self.tape[self.head_position]
        key = (self.current_state, symbol)
        if key in self.transitions:
            new_state, new_symbol, direction = self.transitions[key]
            self.tape[self.head_position] = new_symbol
            self.current_state = new_state
            self.head_position += 1 if direction == 'R' else -1
        else:
            self.current_state = self.reject_state

    def run(self, max_steps=1000):
        steps = 0
        while self.current_state != self.accept_state and self.current_state != self.reject_state:
            self.print_tape()
            self.step()
            steps += 1
            if steps > max_steps:
                print("Machine is looping... Halting manually.")
                break

        self.print_tape()
        if self.current_state == self.accept_state:
            print("✅ Accepted!")
        elif self.current_state == self.reject_state:
            print("❌ Rejected!")

    def print_tape(self):
        tape_str = ''.join(self.tape)
        pointer = ' ' * self.head_position + '^'
        print(f"[State: {self.current_state}]")
        print(tape_str)
        print(pointer)
        print('-' * 40)
