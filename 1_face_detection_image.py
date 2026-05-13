import cv2

img = cv2.imread("images/face.jpg")

if img is None:
    print("ERROR: Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(70, 70)
    )

    print("Number of faces detected:", len(faces))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Face Detection", img)

    cv2.imwrite("images/face_detected.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()