Cài đặt 2 thuật toán Floyd và Bellman
Input: Ma trận cạnh kề (vô hướng hoặc có hướng) (Đồ thị có N đỉnh)
Output:
NxN dòng đầu tiên: in ra ma trận 2 chiều là giá trị của đường đi ngắn nhất giữa 2 cặp đỉnh bất kỳ
Dòng thứ N + 1 : N-1 giá trị là đường đi ngắn nhất từ đỉnh 1 tới tất cả các đỉnh còn lại.
Quy ước: A[i][j] = 0 : là không có cạnh giữa 2 đỉnh
Ví dụ:
Input: (với N=3)
0 1 0
0 0 2
-1 1 0

Output:
0 1 3
1 0 2
-1 0 0
1 3 

Note: Ouput của ví dụ để minh họa, có thể không chính xác :)