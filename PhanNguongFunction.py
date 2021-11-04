import cv2
import numpy as np
from matplotlib import pyplot as plt 
        

def find_global_thresholding(input, epsilon = 1): 
    # Bước 1: Khởi tạo giá trị T
    t = [np.mean(input)]
    while (True):
        # Bước 2. Xác định 2 nhóm điểm ảnh
        c1, c2 = [], [] # Định nghĩa nhóm c1 va c2 
        for i in range(input.shape[0]):
            for j in range(input.shape[1]):
                if (input[i,j] < t[-1]):
                    c1.append(input[i,j])
                else:
                    c2.append(input[i,j])
        # Bước 3: Tính trung bình về mức xám của C1 và C2 -> μ1 và μ2
        u1, u2 = np.mean(c1), np.mean(c2)
        
        # Bước 4:Tính giá trị mới của T
        t.append(((u1+ u2)/2))
        if(abs(t[-1]-t[-2]) < epsilon):
            break
    print("Ngưỡng tìm được: ",t)
    return t 

if __name__ == "__main__": 
    img= cv2.imread("test1.tif", 0)  # reading image in gray scale
    threshold = find_global_thresholding(input = img, epsilon = 3)
    ret, thresh1 = cv2.threshold(img, threshold[-1], 255, cv2.THRESH_BINARY)
    print(ret)
    cv2.imshow(winname='Dau vao', mat = img)
    cv2.imshow(winname='Ket qua', mat = thresh1)
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
