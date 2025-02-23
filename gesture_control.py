import cv2
import mediapipe as mp

# Initialize Mediapipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

def write_gesture(gesture):
    """ Write detected gesture to slide.txt """
    with open("E:\\DevFolioHack1\\slide.txt", "w") as f:
        f.write(gesture)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get key landmarks
            landmarks = hand_landmarks.landmark
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]

            # Open Hand Detection
            if (index_tip.y < landmarks[5].y) and (thumb_tip.x < landmarks[3].x):
                write_gesture("OPEN_HAND")
            
            # Close Fist Detection
            elif all(landmarks[i].y > landmarks[5].y for i in range(8, 21)):
                write_gesture("CLOSE_FIST")

            # Swipe Right Detection
            elif index_tip.x - landmarks[5].x > 0.1:
                write_gesture("SWIPE_RIGHT")

            # Swipe Left Detection
            elif landmarks[5].x - index_tip.x > 0.1:
                write_gesture("SWIPE_LEFT")

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
