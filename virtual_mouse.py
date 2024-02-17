import cv2
import mediapipe as mp
import pyautogui


cam = cv2.VideoCapture(2)                       # opening the webcam
hand_detector = mp.solutions.hands.Hands()      # detecting the hand
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cam.read()                       # Frame of the window
    frame = cv2.flip(frame, 2)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)       
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(x,y)
                if id == 8:             # for tip of the index finger
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 0))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:             # For tip of the thumb
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 0)) P# poiinter of mouse
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    print('outside', abs(index_y-thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        print('Click')
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('ritesh', frame)
    
    cv2.waitKey(1)
    