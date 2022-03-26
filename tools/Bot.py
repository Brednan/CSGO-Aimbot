from tools.Mechanisms import Mechanisms
from tools.Vision import Vision
import time
import traceback
import numpy as np

class Bot:
    def __init__(self, monitor, toggle_key):
        self.monitor = monitor
        self.model = Vision.load_dnn('ffa_model/last.pt')
        self.active = False
        self.quit = False
        self.toggle_key = toggle_key
        self.start_time = time.time()

    def handle_keypress(self, event):
        if event.name == self.toggle_key:
            self.handle_toggle()
        elif event.name == 'n':
            self.handle_quit()

    def detect_enemy(self): 
        Vision.capture_screen(self.monitor)
        img = Vision.read_img('./tools/ss_cache/screen.jpg')
        cord = Vision.detection(self.model, img, confidence=0.6, img_size=640)
        return cord
    
    def handle_toggle(self):
        if self.active == False:
            self.active = True
            print('Toggled on!')
                
        elif self.active == True:
            self.active = False
            print('Toggled off!')
    
    def handle_quit(self):
        self.quit = True
        print('quitting')
        
    def bot_sequence(self):
        while self.quit == False:
            if self.active == True:
                try:
                    target_location = self.detect_enemy()
                    if len(target_location) > 0:
                        row = target_location
                        x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
                        center_location = ((x2 + x1)/2, (y2 + y1)/2)
                        # Vision.draw_rectangle(target_location, './tools/ss_cache/screen.jpg')
                        print(f'[{time.time() - self.start_time}] located target ({row[4]})')
                        Mechanisms.aim_at_target(center_location)

                except:
                    print('Error detecting enemy!')





