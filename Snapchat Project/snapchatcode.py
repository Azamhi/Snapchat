import cv2
import cvzone
# Initialize video capture

vid = cv2.VideoCapture(0)

# Load Haar cascade and overlay image
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

overlay = cv2.imread('star.png', cv2.IMREAD_UNCHANGED)


while True:


    ret, frame = vid.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert frame to grayscale
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = cascade.detectMultiScale(gray_scale)

    for (x, y, w, h) in faces:


        # Resize the overlay
        overlay_resize = cv2.resize(overlay, (int(w * 1.6), int(h * 1.6)))

        # Adjust position (ensure it doesn't go out of bounds)
        x_offset = max(0, x - 45)
        y_offset = max(0, y - 75)

        # Apply overlay
        frame = cvzone.overlayPNG(frame, overlay_resize, [x_offset, y_offset])

    # Display the frame
    cv2.imshow('SnapChat', frame)

    # Break the loop when 'w' key is pressed
    if cv2.waitKey(10) == ord('w'):
        break

# Release resources

# frees the webcam resources
vid.release()

# Destroys all the opnecv windows
cv2.destroyAllWindows()
