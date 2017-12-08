# from yolo_tensor.yolo_tiny import *
from yolo_tensor.yolo_small import *

if __name__ == '__main__':

    input_type = 'video'  # 'video'  # 'video' # 'image'
    # input_name = './data/videos/wetransfer-40665b/2017-12-05-19h52m03s-newton-y-homero.mp4'  # 'test_images/test1.jpg' # 'project_video.mp4'
    input_name = './data/videos/test.MOV'

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
        out = cv2.VideoWriter('output_.avi', fourcc, 25.0, (480, 270))  # 480 x 360
        cnt = 0
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:

                detect_from_file(yolo, frame)

                yolo_result = show_results(frame, yolo)

                yolo_result = cv2.resize(yolo_result, (int(yolo_result.shape[1] / 1), int(yolo_result.shape[0] / 1)))
                cv2.imshow('result', yolo_result)

                out.write(yolo_result)

                # cv2.waitKey(0)
                cnt += 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.imwrite("result{}.jpg".format(cnt), yolo_result)
                    break

            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
