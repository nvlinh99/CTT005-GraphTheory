Input: Ma trận kề
Output:
Dòng 1: Nếu có chu trình Euler thì in 1 hoặc Có đường đi Euler thì in 0 ngược lại -1 (nếu không có)
Dòng 2: In ra chu trình Euler (nếu có) hoặc đường đi Euler đầu tiên (nếu có) hoặc -1
Dòng 3: Nếu có chu trình Hamilton hoặc Có đường đi Hamilton thì in 0 ngược lại -1 (nếu không có)
Dòng 4: In ra chu trình Hamilton (nếu có) hoặc đường đi Hamilton đầu tiên (nếu có) hoặc -1

Ví dụ:
Input:
0 1 0 1 0
1 0 1 1 1
0 1 0 0 1
1 1 0 0 0
0 1 1 0 0
Output:
1
[(0, 3), (3, 1), (1, 4), (4, 2), (2, 1), (1, 0)]
0
0, 3, 1, 4, 2