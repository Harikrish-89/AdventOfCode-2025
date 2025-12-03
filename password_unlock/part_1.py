from password_unlock.circular_dial_lock import CircularDialedLock

lock = CircularDialedLock(0)
for i in range(1,100):
    lock.append_last(i)

lock.set_current(50)

# input_actions = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82',]
input_actions = []
with open('input.txt','r') as f:
    for line in f:
        input_actions.append(line.strip())

password = 0
print(f"Initial dial value {lock.current.value}")
for action in input_actions:
    direction= action[0]
    value = int(action[1:])
    if direction == 'L':
        lock.traverse_left(value)
        print(f"After left {value} times",lock.current.value)
    if direction == 'R':
        lock.traverse_right(value)
        print(f"After right {value} times",lock.current.value)
    if lock.current.value == 0:
        password = password + 1

print("Password:",password)
