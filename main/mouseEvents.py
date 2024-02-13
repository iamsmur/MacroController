from pynput.mouse import Listener
import logging
import sys
logging.basicConfig(filename=("mouse_log2.txt"), level=logging.DEBUG, format='%(message)s')

def on_move(x, y):
    logging.info('movedTo : {0} {1}'.format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('{2} : {0} {1}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    #logging.info('scrolledAt ({0} {1}) ({2} {3})'.format(x, y, dx, dy))
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()