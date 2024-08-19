import csv
from pynput.keyboard import Key, Listener


reader = csv.DictReader(open('data.csv', 'r'))
rows = [row for row in reader]
current_rank = max([int(row['rank']) for row in rows])
hotkey = None

def write_to_txt(rank):
    with open('data.txt', 'w') as f:
        f.write(f"{rows[rank - 1]['user']} - {rows[rank - 1]['time']}")

write_to_txt(current_rank)

def on_press(key):
    global current_rank
    global hotkey
    if hotkey and key == hotkey:
        print('Moving to next entry...')
        current_rank -= 1
        write_to_txt(current_rank)
    elif not hotkey:
        hotkey = key
        print(f'{key} set as hotkey')

def on_release(key):
    pass

print('Press which key you want to use as hotkey to move to next user')

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
