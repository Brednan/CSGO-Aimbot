import cv2
from mss import mss, tools
import torch
from PIL import Image, ImageGrab
import time
import math

class Vision:
    def capture_screen(self):
        x1 = 960 - 620
        x2 = 960 + 620

        y1 = 540 - 420
        y2 = 540 + 420

        # img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        # img.save('./tools/ss_cache/screen.jpg')
        img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        img.save('./tools/ss_cache/screen.jpg')

    def load_dnn(self, path):
        # torch.hub.set_dir('D:\Desktop\CSGO-Aimbot')
        model = torch.hub.load('ultralytics_yolov5_master', 'custom', path=path, source='local')
        return model
    
    def read_img(self, path):
        img = cv2.imread(path)
        return img
    
    def show_img(self, img):
        cv2.imshow('Screen', img)
        cv2.waitKey(0)
    
    def detection(self, model, img, confidence, img_size, distance):
        img = cv2.resize(img, (img_size, img_size))
        model.conf = confidence
        results = model([img], size=img_size)
        cord = results.xyxy[0]

        for i in range(len(cord)):
            cord[i][0] *= 1920/img_size
            cord[i][1] *= 1080/img_size
            cord[i][2] *= 1920/img_size
            cord[i][3] *= 1080/img_size

        try:
            closest = self.get_closest(cord, distance)
            if closest != None:
                return cord[closest]
            else:
                return []

        except:
            return []

    def draw_rectangle(self, cord, img):
        img = cv2.imread(img)

        x1, y1, x2, y2 = int(cord[0]), int(cord[1]), int(cord[2]), int(cord[3])
        rectangle_color = (0, 255, 0)
        cv2.rectangle(img, (x1, y1), (x2, y2), rectangle_color, 2)
        
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def get_closest(self, coords, max_distance):
        #List of x and y coordinates added up in each location
        total_coords = []

        for c in coords:
            #Center of rectangle around detected object
            x_center = int((c[0]+c[2]))/2
            y_center = int((c[1]+c[3]))/2

            distance = abs((x_center + y_center) - (960 + 540))
            total_coords.append(distance)

        if min(total_coords) < max_distance:
            return total_coords.index(min(total_coords))
        else:
            return []
