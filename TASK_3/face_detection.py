import cv2

# Load image
image = cv2.imread("person.jpg")

# Check if image loaded
if image is None:
    print("Error: person.jpg not found. Make sure the image is in the same folder.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Print number of faces
print("Number of faces detected:", len(faces))

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show result
cv2.imshow("Face Detection Result", image)

cv2.waitKey(0)
cv2.destroyAllWindows()