import os

import cv2


DATA_DIR = "./data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Try different camera indices if the default one doesn't work
camera_indices = [0, 1, 2]
cap = None

for index in camera_indices:
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Camera opened with index {index}")
        break
    else:
        cap.release()
        cap = None

if cap is None:
    print("Failed to open any camera.")
else:
    for j in range(number_of_classes):
        if not os.path.exists(os.path.join(DATA_DIR, str(j))):
            os.makedirs(os.path.join(DATA_DIR, str(j)))

        print("Collecting data for class {}".format(j))

        done = False
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break
            cv2.putText(
                frame,
                'Ready? Press "Q" ! :)',
                (100, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.3,
                (0, 255, 0),
                3,
                cv2.LINE_AA,
            )
            cv2.imshow("frame", frame)
            if cv2.waitKey(25) == ord("q"):
                break

        counter = 0
        while counter < dataset_size:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break
            # Process the frame
            cv2.imshow("frame", frame)
            cv2.waitKey(25)
            cv2.imwrite(os.path.join(DATA_DIR, str(j), "{}.jpg".format(counter)), frame)

            counter += 1

    cap.release()
    cv2.destroyAllWindows()
