import cv2
import numpy as np
import urllib.request


class ESP32Cam:
    def __init__(self, url):
        self.url = url

    def get_frame(self):
        img_response = urllib.request.urlopen(self.url)
        img_array = np.array(bytearray(img_response.read()), dtype=np.uint8)
        frame = cv2.imdecode(img_array, -1)

        return frame

if __name__ == "__main__":
    url = 'http://192.168.213.104/cam-lo.jpg'  
    esp32cam = ESP32Cam(url)

    while True:
        frame = esp32cam.get_frame()

        if frame is not None:
            cv2.imshow("ESP32-CAM", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

