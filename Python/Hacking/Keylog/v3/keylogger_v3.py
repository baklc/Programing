from pynput.keyboard import Key, Listener

def handlePress(key):
    print(key)

with Listener(on_press=handlePress) as listener:
    listener.join()