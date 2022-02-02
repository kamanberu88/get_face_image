import cv2
import os



def save_frame_camera_key():
    cascade_path = "./haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_path)
    color = (0, 255, 0)  # 検出した顔を囲む四角形の色
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    x = input('you name')  # 名前を入れて

    dir_path = 'data/tmo/{}'.format(x)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    #os.makedirs(dir_path,exist_ok=True)
    base_path = os.path.join(dir_path, '{}').format(x)

    count= 0
    while True:
        ret, image = cap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rect = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(64, 64))
        if len(rect) > 0:
            for x, y, w, h in rect:
                cv2.rectangle(image, (x, y), (x + w, y + h), color)
                trim=image[y:y+h,x:x+w] #トリミングした画像


        cv2.imshow('detected', image)
        cv2.imwrite('{}_{}.{}'.format(base_path, count, 'jpg'), trim)

        k=cv2.waitKey(100)&0xff
        if k==27:
            break
        elif count>=100:
            break


    cap.release()  ###動画ファイル閉じる、もしくはキャプチャデバイスを終了させます。
    cv2.destroyAllWindows()

save_frame_camera_key()
