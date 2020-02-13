import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 0.0001
button = Button.left
start_stop_key = KeyCode(char='o')
exit_key = KeyCode(char='p')



print('▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▄▄▄▄   ▄▀▀▄ ▄▄   ▄▀▀▀▀▄')
print('█   █   █ █ █   ▐ █   ▀▄ ▄▀ █ █    ▌ █  █   ▄▀ █      █')   
print('▐  █▀▀▀▀     ▀▄   ▐     █   ▐ █      ▐  █▄▄▄█  █      █')
print('   █      ▀▄   █        █     █         █   █  ▀▄    ▄▀')
print(' ▄▀        █▀▀▀       ▄▀     ▄▀▄▄▄▄▀   ▄▀  ▄▀    ▀▀▀▀')
print('█          ▐          █     █     ▐   █   █')
print('▐                     ▐     ▐         ▐   ▐')
print('[+]-Initializing...-[+]')

time.sleep(2)

print('Psych0 Autoclicker v1.0')
print('')
print('')
print('Press O to start and stop the autoclicker.')
print('Press P to close the autoclicker.')




class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print('Autoclicking Stopped.')
        else:
            print('Autoclicking Started.')
            click_thread.start_clicking()
    elif key == exit_key:
        print('Closing.')
        time.sleep(2)
        click_thread.exit()
        listener.stop()



        
        


with Listener(on_press=on_press) as listener:
    listener.join()