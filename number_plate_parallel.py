import cv2
import multiprocessing as mp

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(1)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

def detect_plates(frame_queue, result_queue):
    plate_cascade = cv2.CascadeClassifier(harcascade)
    
    while True:
        img = frame_queue.get()
        if img is None:
            break

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
        
        for (x, y, w, h) in plates:
            area = w * h
            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                img_roi = img[y: y + h, x: x + w]
                result_queue.put(img_roi)

        result_queue.put(img)

def process_frame(frame_queue):
    while True:
        success, img = cap.read()
        if not success:
            frame_queue.put(None)
            break
        frame_queue.put(img)

def main():
    global count

    frame_queue = mp.Queue(maxsize=10)
    result_queue = mp.Queue(maxsize=10)

    # Start the plate detection process
    detection_process = mp.Process(target=detect_plates, args=(frame_queue, result_queue))
    detection_process.start()

    # Start capturing frames
    frame_capture_process = mp.Process(target=process_frame, args=(frame_queue,))
    frame_capture_process.start()

    while True:
        img = result_queue.get()
        if img is None:
            break

        cv2.imshow("Result", img)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_roi = result_queue.get()
            cv2.imwrite("plates/scanned_img_" + str(count) + ".jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            count += 1

    frame_capture_process.join()
    detection_process.join()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
