# Import OpenCV2 for image processing -> sử dụng OpenCV2 để xử lý ảnh
import cv2
import os

# Start capturing video -> bắt đầu quay video
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face -> nhận diện object trong video bằng thuật toán Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, one face id -> một face id cho mỗi người
face_id = 0

# Initialize sample face image -> bắt đầu lẫy mẫu ảnh khuôn mặt
count = 0;

# Count ID
directory = 'dataset'
ID = 0
for root, dirs, files in os.walk(directory):
    ID += len(dirs)

print(ID)
ID = 6
path = directory + '/' + str(ID)
if not os.path.exists(path):
    os.makedirs(path)
imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
count = 0
for root, dirs, files in os.walk(path):
    count = len(files)

limit = count + 300
# Start looping
while(True):

    # Capture video frame ->chụp frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale -> chuyển frame qua dạng grayscale
    #gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles -> nhận diện các khung với các size khác nhau, ?
    faces = face_detector.detectMultiScale(image_frame, 1.3, 5)
    
    # Loops for each faces -> lặp với mỗi khuôn mặt
    for (x,y,w,h) in faces:
        count += 1
        cv2.imwrite(path + "/" + str(count) + ".png", image_frame)
        # Crop the image frame into rectangle -> crop frame thành hình chữ nhật
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Increment sample face image -> tăng mẫu khuôn mặt
        

        # Save the captured image into the datasets folder -> lưu ảnh vào datasets folder
        
        
        # Display the video frame, with bounded rectangle on the person's face -> hiển thị video frame với khung chữ nhật trên mặt
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms -> dừng quay video, nhấn 'q' ít nhất 100ms
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count> limit:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
