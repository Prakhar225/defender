import cv2
import pyautogui
import numpy as np
import threading
import time

class ObjectDetector(threading.Thread):
    def __init__(self, template_path):
        super().__init__()
        self.template = cv2.imread(template_path)
        self.stopped = threading.Event()

    def find_object(self, screenshot):
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        template_gray = cv2.cvtColor(self.template, cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screenshot, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        h, w = template_gray.shape
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        return center_x, center_y

    def click_at(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def run(self):
        while not self.stopped.wait(0.1):
            try:
                screenshot = pyautogui.screenshot()
                object_x, object_y = self.find_object(np.array(screenshot))
                self.click_at(object_x, object_y)
            except Exception as e:
                print(f"Error: {e}")

    def stop(self):
        self.stopped.set()


def main():
    detector = ObjectDetector('template_image.png')
    detector.start()

    # Run some other code here if needed

    # Let the program run for 60 seconds
    time.sleep(60)

    # Stop the object detection thread
    detector.stop()
    detector.join()

if __name__ == "__main__":
    main()
