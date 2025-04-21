import cv2
import mediapipe as mp

# setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# open camera
cap = cv2.VideoCapture(0)

# init. hands
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # flip & convert frame
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark

                # finger landmarks
                tips_ids = [4, 8, 12, 16, 20]

                # thumb
                if landmarks[tips_ids[0]].x < landmarks[tips_ids[0] - 1].x:
                    finger_count += 1

                # others
                for id in range(1, 5):
                    if landmarks[tips_ids[id]].y < landmarks[tips_ids[id] - 2].y:
                        finger_count += 1

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # display held up fingers
        cv2.rectangle(frame, (0, 0), (150, 80), (0, 0, 0), -1)
        cv2.putText(frame, f'Ujjak: {finger_count}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                    1.5, (255, 255, 255), 3)

        cv2.imshow("Teszt 1", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # esc to quit
            break

cap.release()
cv2.destroyAllWindows()
