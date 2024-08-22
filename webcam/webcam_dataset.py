import cv2

def main():
    vid = cv2.VideoCapture(0)
    cnt = 0

    while True:
        _, frame = vid.read()
        cv2.imwrite(f'webcam_dataset/{cnt:06d}.png', frame)
        print(f'{cnt:06d}.png is saved')

        cv2.imshow('frame', frame)

        cnt += 1
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    vid.release()

if __name__ == '__main__':
    main()