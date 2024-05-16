import cv2 as cv
import hashlib as hash

def process_frame(frame):
    # grayscale conversion
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # hash object conversion
    hash_obj = hash.sha256(gray_frame.tobytes())
    # hexadecimal conversion
    hexadecimal = hash_obj.hexdigest()
    return hexadecimal

# TRNG source footage
capture = cv.VideoCapture('lava_lamp.mp4')

index=0
while True:
    index+=1
    isRead,frame = capture.read()
    if isRead != True:
        print("END OF FOOTAGE")
        capture.release()
        cv.destroyAllWindows
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray Scale Lamp", gray_frame)
    hexadecimal = process_frame(frame)
    frame_2 = cv.putText(frame, "Code: "+str(hexadecimal[:16])+"...", (85, 348), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    cv.imshow("Lava Lamp", frame_2)
    print(f"Frame {index}: Key: {hexadecimal}")
    if cv.waitKey(60) & 0xFF == ord('s'):
        break