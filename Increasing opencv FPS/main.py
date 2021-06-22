from WebcamVideoStream import WebcamVideoStream
from FPS import FPS
import argparse
import imutils
import cv2
import pytesseract as pt


def process_text(frame):
    img_height, img_width, _ = frame.shape
    config = r"--oem 3 --psm 6 outputbase digits"
    boxes = pt.image_to_data(image=frame, config=config)
    print(boxes)
    # Getting the positions(x, y), box width, height
    for x, i in enumerate(boxes.splitlines()):  # Enumerate: to keep track of count of iterators we don't want the count
        if x != 0:
            # print(i)
            i = i.split()
            print(i)
            if len(i) == 12:
                x, y, w, h = int(i[6]), int(i[7]), int(i[8]), int(i[9])
                # Making the rectangle around the text
                cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 0, 255), thickness=1)
                cv2.putText(frame, i[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 50), thickness=2)
    return frame


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
                help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
                help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=5).start()
# fps = FPS().start()
# loop over some frames...this time using the threaded stream
while True:
    # grab the frame from the threaded video stream
    frame = vs.read()

    # frame = cv2.imread("images/2.jpg")
    # Increasing performance
    # frame = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
    # frame = imutils.resize(frame, width=400)

    # Detecting Words & Digits
    frame = process_text(frame)

    # check to see if the frame should be displayed to our screen
    if args["display"] > 0:
        frame = imutils.resize(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow("Result", frame)
        key = cv2.waitKey(1) & 0xFF
    # update the FPS counter
    # fps.update()

# fps.stop()
# print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
# print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# # do a bit of cleanup
# cv2.destroyAllWindows()
# vs.stop()
