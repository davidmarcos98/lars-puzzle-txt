import csv
from pynput.keyboard import Key, Listener


reader = csv.DictReader(open('data.csv', 'r'))
rows = [row for row in reader]
current_rank = max([int(row['rank']) for row in rows])

def write_to_txt(rank):
    with open('data.txt', 'w') as f:
        f.write(f"{rows[rank - 1]['user']} - {rows[rank - 1]['time']}")

write_to_txt(current_rank)

def on_press(key):
    global current_rank
    if (key == Key.f4):
        print('Moving to next entry...'.format(
            key))
        current_rank -= 1
        write_to_txt(current_rank)


def on_release(key):
    if key == Key.esc:
        print('{0} release'.format(
            key))
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
