import cv2
from mss import mss, tools
import torch
from PIL import Image, ImageGrab
import time

class Vision:
    def capture_screen(monitor):
        x1 = 960 - 620
        x2 = 960 + 620

        y1 = 540 - 420
        y2 = 540 + 420

        # img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        # img.save('./tools/ss_cache/screen.jpg')
        img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        img.save('./tools/ss_cache/screen.jpg')

    def load_dnn(path):
        # torch.hub.set_dir('D:\Desktop\CSGO-Aimbot')
        model = torch.hub.load('ultralytics_yolov5_master', 'custom', path=path, source='local')
        return model
    
    def read_img(path):
        img = cv2.imread(path)
        return img
    
    def show_img(img):
        cv2.imshow('Screen', img)
        cv2.waitKey(0)
    
    def detection(model, img, confidence, img_size):
        img = cv2.resize(img, (img_size, img_size))
        model.conf = confidence
        results = model([img], size=img_size)
        cord = results.xyxy[0]

        area_vals = []

        for i in range(len(cord)):
            cord[i][0] *= (1920/img_size)
            cord[i][1] *= (1080/img_size)
            cord[i][2] *= (1920/img_size)
            cord[i][3] *= (1080/img_size)
            
            area_vals.append((cord[i][2]-cord[i][0])*(cord[i][3]-cord[i][1]))

        try:
            return cord[area_vals.index(max(area_vals))]
        except:
            return []


    def draw_rectangle(cord, img):
        img = cv2.imread(img)
        for i in range(len(cord)):
            row = cord[i]
            x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
            rectangle_color = (0, 255, 0)
            cv2.rectangle(img, (x1, y1), (x2, y2), rectangle_color, 2)
        
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
