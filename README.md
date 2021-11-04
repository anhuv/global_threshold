# global_threshold

## Algorithm
* Bước 1: Khởi tạo giá trị T (trung bình, điểm giữa, …)
* Bước 2: Xác định 2 nhóm điểm ảnh C1 nếu f(x,y) > T và C2 nếu f(x,y) ≤ T
* Bước 3: Tính trung bình về mức xám của C1 và C2 -> μ1 và μ2
* Bước 4:Tính giá trị mới của T = 1/2 (μ1 + μ2) Lặp lại Bước 2 cho đến khi T ổn định 
