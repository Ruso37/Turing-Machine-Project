
from turing_machine import TuringMachine

# Define the components
states = {'q0', 'q1', 'qa', 'qr'}
input_symbols = {'0', '1'}
tape_symbols = {'0', '1', '_'}
blank = '_'
start = 'q0'
accept = 'qa'
reject = 'qr'

# Define transitions
transitions = {
    ('q0', '1'): ('q1', '1', 'R'),
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '_'): ('qa', '_', 'R'),

    ('q1', '1'): ('q0', '1', 'R'),
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '_'): ('qr', '_', 'R'),
}

# Create the machine
tm = TuringMachine(states, input_symbols, tape_symbols, transitions, start, blank, accept, reject)

# Run it
input_string = input("Enter a binary string: ")
tm.load_tape(input_string)
tm.run()
