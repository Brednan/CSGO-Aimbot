from cv2 import trace
from tools.Mechanisms import Mechanisms
from tools.Vision import Vision
import time
from ctypes import windll
import traceback

vision = Vision()

class Bot:
    def __init__(self, monitor, mode, distance):
        self.monitor = monitor
        self.active = False
        self.quit = False
        self.start_time = time.time()
        self.distance = distance
        
        if str.lower(mode) == 'all':
            self.model = vision.load_dnn('models/ffa_model/last.pt')
        
        elif str.lower(mode) == 't':
            self.model = vision.load_dnn('models/terrorist_model/last.pt')
        
        else:
            print('no mode specified!')
            quit()


    def detect_enemy(self): 
        vision.capture_screen()
        img = vision.read_img('./tools/ss_cache/screen.jpg')
        cord = vision.detection(self.model, img, confidence=0.55, img_size=640, distance=self.distance)
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
        while True:
            self.check_keypress()
            if self.active == True:
                try:
                    target_location = self.detect_enemy()
                    if len(target_location) > 0 and target_location != None:
                        row = target_location
                        x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
                        center_location = ((x2 + x1)/2, (y2 + y1)/2)
                        # vision.draw_rectangle(target_location, './tools/ss_cache/screen.jpg')
                        print(f'[{time.time() - self.start_time}] located target ({row[4]})')
                        Mechanisms.aim_at_target(center_location)

                except Exception as e:
                    print(traceback(e))

    def check_keypress(self):
        if windll.user32.GetKeyState(0x43) not in [0, 1]:
            if self.active == False:
                self.active = True
                print('Toggled On!')
                time.sleep(0.7)
            
            elif self.active == True:
                self.active = False
                print('Toggled Off!')
                time.sleep(0.7)


        if windll.user32.GetKeyState(0x70) not in [0, 1]:
            quit()

