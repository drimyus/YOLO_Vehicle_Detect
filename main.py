# from yolo_tensor.yolo_tiny import *
from yolo_tensor.yolo_small import *

if __name__ == '__main__':

    input_type = 'image'  # 'video'  # 'video' # 'image'
    input_name = './data/images/test4.jpg'  # 'test_images/test1.jpg' # 'project_video.mp4'

    yolo = yolo_tf()

    if input_type == 'image':
        frame = cv2.imread(input_name)
        detect_from_file(yolo, frame)

        yolo_result = show_results(frame, yolo)
        cv2.imshow('result', yolo_result)
        cv2.waitKey(0)

    elif input_type == 'video':
        cap = cv2.VideoCapture(input_name)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output_small.avi', fourcc, 25.0, (480, 360))  # 480 x 360
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:

                detect_from_file(yolo, frame)

                yolo_result = show_results(frame, yolo)
                cv2.imshow('result', yolo_result)
                cv2.imwrite('result.jpg', yolo_result)
                break

                out.write(yolo_result)

                # cv2.waitKey(0)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
