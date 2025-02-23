import cv2
import mediapipe as mp
import time

# Initialize Mediapipe Hand Detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize slide number
slide = 1
started = False  # Flag to track if the presentation has started

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Flip image for natural view
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process hand detection
    result = hands.process(rgb_image)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            x_list = [lm.x for lm in hand_landmarks.landmark]
            y_list = [lm.y for lm in hand_landmarks.landmark]
            min_x, max_x = min(x_list), max(x_list)

            # Detect Open Hand to Start
            finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
            if all(hand_landmarks.landmark[i].y < hand_landmarks.landmark[i-2].y for i in finger_tips):
                if not started:
                    print("Open Hand Detected: Starting Slide 1")
                    slide = 1
                    started = True
                else:
                    print(f"Slide {slide} Active")

            # Swipe Gestures
            if started:
                if min_x < 0.1:  # Swipe Left
                    slide = max(1, slide - 1)
                elif max_x > 0.9:  # Swipe Right
                    slide += 1  # Increase slide number
                
                print(f"Updated Slide: {slide}")

            # Write to file
            with open("slide.txt", "w") as f:
                f.write(str(slide))

            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display webcam feed
    cv2.imshow("Gesture Control", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit on 'q'
        break

cap.release()
cv2.destroyAllWindows()