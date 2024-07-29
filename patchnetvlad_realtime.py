import torch
import torch.nn as nn
import cv2

from patchnetvlad.models.models_generic import get_backend, get_model
from patchnetvlad.tools import PATCHNETVLAD_ROOT_DIR
from match_two import match_two

def main():
    vid = cv2.VideoCapture(0)
    
    if vid.isOpened():
        while True:
            ret, img = vid.read()
            if ret:
                cv2.imshow('camera', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()