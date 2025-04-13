
from turing_machine import TuringMachine

# Palindrome checker for binary strings using X as marker

states = {
    'q_start', 'q_check_0', 'q_check_1', 'q_right',
    'q_left', 'q_accept', 'q_reject', 'q_skip'
}

input_symbols = {'0', '1'}
tape_symbols = {'0', '1', 'X', '_'}
blank = '_'
start = 'q_start'
accept = 'q_accept'
reject = 'q_reject'

transitions = {
    # Start: read leftmost character
    ('q_start', '0'): ('q_check_0', 'X', 'R'),
    ('q_start', '1'): ('q_check_1', 'X', 'R'),
    ('q_start', 'X'): ('q_accept', 'X', 'R'),
    ('q_start', '_'): ('q_accept', '_', 'R'),

    # Move right to end to find matching symbol
    ('q_check_0', '0'): ('q_check_0', '0', 'R'),
    ('q_check_0', '1'): ('q_check_0', '1', 'R'),
    ('q_check_0', 'X'): ('q_check_0', 'X', 'R'),
    ('q_check_0', '_'): ('q_left', '_', 'L'),

    ('q_check_1', '0'): ('q_check_1', '0', 'R'),
    ('q_check_1', '1'): ('q_check_1', '1', 'R'),
    ('q_check_1', 'X'): ('q_check_1', 'X', 'R'),
    ('q_check_1', '_'): ('q_left', '_', 'L'),

    # Go back and check match for 0 or 1
    ('q_left', '0'): ('q_right', 'X', 'L'),
    ('q_left', '1'): ('q_right', 'X', 'L'),
    ('q_left', 'X'): ('q_left', 'X', 'L'),

    # Move to next unmatched symbol
    ('q_right', '0'): ('q_right', '0', 'L'),
    ('q_right', '1'): ('q_right', '1', 'L'),
    ('q_right', 'X'): ('q_right', 'X', 'L'),
    ('q_right', '_'): ('q_start', '_', 'R'),

    # Mismatches (invalid ending characters)
    ('q_check_0', '1'): ('q_check_0', '1', 'R'),
    ('q_check_1', '0'): ('q_check_1', '0', 'R'),
    ('q_left', '_'): ('q_reject', '_', 'R'),
    ('q_left', 'X'): ('q_left', 'X', 'L'),
}

tm = TuringMachine(
    states=states,
    input_symbols=input_symbols,
    tape_symbols=tape_symbols,
    transitions=transitions,
    start_state=start,
    blank_symbol=blank,
    accept_state=accept,
    reject_state=reject
)

input_string = input("Enter a binary string to check for palindrome: ")
tm.load_tape(input_string)
tm.run()
