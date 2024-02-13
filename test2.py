from pynput import keyboard
import logging


#logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
logging.basicConfig(filename=("mouse_log2.txt"), level=logging.DEBUG, format='%(message)s')

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    key_name = get_key_name(key)
    print('Key {} pressed.'.format(key_name))
    logging.info('Key {} pressed.'.format(key_name))

def on_release(key):
    key_name = get_key_name(key)
    #print('Key {} released.'.format(key_name))
    #logging.info('Key {} released.'.format(key_name))

    if key_name == 'Key.esc':
        print('Exiting...')
        logging.info('Key {} pressed.'.format(key_name))
        return False

with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()