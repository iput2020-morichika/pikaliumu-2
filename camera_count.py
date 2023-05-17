import cv2
def take_picture():
    # 内蔵カメラを使って画像を取得する
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    # カメラを解放する
    cap.release()
    # 画像を返す
    return img
def adjust_brightness(img, brightness=0):
    # 画像をグレースケールに変換する
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ヒストグラムを平坦化する
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    # 明るさを調整する
    adjusted = cv2.convertScaleAbs(img, alpha=1, beta=brightness)
    # 画像を返す
    return adjusted
# 顔検出器を読み込む
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_count = 0
while True:
    # 画像を撮影する
    img = take_picture()
    # 画像の明るさを調整する
    bright_img = adjust_brightness(img, brightness=50)
    # 顔を検出する
    gray = cv2.cvtColor(bright_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 顔の数をカウントする
    face_count = len(faces)
    # 顔を四角で囲む
    for (x,y,w,h) in faces:
        cv2.rectangle(bright_img,(x,y),(x+w,y+h),(255,0,0),2)
    # 画像と顔の数を表示する
    cv2.putText(bright_img, f"Face count: {face_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Picture", bright_img)
    # キー入力を待つ
    key = cv2.waitKey(1)
    # 'q'を押したら終了する
    if key == ord('q'):
        break
# ウィンドウを閉じる
cv2.destroyAllWindows()