from re import A
from tools.Vision import Vision
import keyboard
import threading

monitor = int(input('Monitor: '))
model = Vision.load_dnn('model/last.pt')

def detect_enemy(): 
    Vision.capture_screen(monitor)
    img = Vision.read_img('./tools/ss_cache/screen.jpg')
    cord = Vision.detection(model, img, confidence=0.15)
    Vision.draw_rectangle(cord, img)

while True:
    if keyboard.read_key() == 'q':
        if threading.active_count() < 4:
            threading.Thread(target=detect_enemy).start()
    if keyboard.read_key() == 'n':
        break

