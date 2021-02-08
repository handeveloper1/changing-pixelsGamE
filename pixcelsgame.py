
import cv2
import numpy as np
import pyautogui
import keyboard
from pynput.mouse import Controller as Controller
from pynput.mouse import Button
import time


if __name__ == '__main__':
    print('Starting...')


    mouse = Controller()
    enabled = False
    tm = int(round(time.time() * 1000))
    fps = 1
    fps1 = 0


    while True:
       
        img = pyautogui.screenshot(region=(955, 535, 10, 10))
       
        img = np.array(img)
        frame = np.array(img).sum()

     
        if keyboard.is_pressed('f'):
            print('Predicting...')
            frame1 = np.array(img).sum()
            if enabled == True:
                enabled = False
            else:
                enabled = True
            
            # wait 0.2 seconds  double clicking
            time.sleep(0.2)

       
        if enabled == True:
          
            if frame1 > (frame+1000) or frame1 < (frame-1000): # cs:go 1000, Valorant 500
                mouse.press(Button.left)
                time.sleep(0.1)
                mouse.release(Button.left)
                enabled = False
                print('Shot')

            if frame1 > (frame+100) or frame1 < (frame-100): # cs:go 100, Valorant 50
                frame1 = np.array(img).sum()

        # do some math in order to get the fps value
        if int(round(time.time() * 1000))-tm > 1000:
            fps1 = fps
            tm = int(round(time.time() * 1000))
            fps = 0
        fps += 1
            
       
        r = 200.0 / img.shape[1]
        dim = (200, int(img.shape[0] * r))
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # q for quit
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("screenshot", img)
        if cv2.waitKey(1) == ord("q"):
            break
            cv2.destroyAllWindows()
