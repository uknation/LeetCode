// OJ: https://leetcode.com/problems/search-a-2d-matrix-ii/
// Time: O(M + N)
// Space: O(1)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& A, int target) {
        int M = A.size(), N = A[0].size(), i = 0, j = N - 1;
        while (i < M && j >= 0) {
            if (A[i][j] == target) return true;
            if (A[i][j] < target) ++i; 
            else --j;
        }
        return false;
    }
};