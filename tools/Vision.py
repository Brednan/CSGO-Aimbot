import cv2
from mss import mss
import torch


class Vision:
    def capture_screen(monitor):
        with mss() as mss_instance:
            mss_instance.shot(mon=monitor, output='./tools/ss_cache/screen.jpg')

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
    
    def detection(model, img, confidence):
        img = cv2.resize(img, (640, 640))
        model.conf = confidence
        results = model([img], size=640)
        cord = results.xyxy[0]

        for i in range(len(cord)):
            cord[i][0] *= (1920/640)
            cord[i][1] *= (1080/640)
            cord[i][2] *= (1920/640)
            cord[i][3] *= (1080/640)

        return cord


    def draw_rectangle(cord, img):
        for i in range(len(cord)):
            row = cord[i]
            x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
            rectangle_color = (0, 255, 0)
            cv2.rectangle(img, (x1, y1), (x2, y2), rectangle_color, 2)
        
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
