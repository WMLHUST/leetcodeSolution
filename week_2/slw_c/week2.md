# Week2

## 106. [从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

根据一棵树的中序遍历与后序遍历构造二叉树。



C 实现

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* buildTreeImp(int* inorder, int instart, int inend, int* postorder, int poststart, int postend)
{
    if (instart > inend || poststart > postend) {
        return NULL;
    }
    
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = postorder[postend];
    
    int mid;
    for (mid = instart; mid <= inend; mid++) {
        if (inorder[mid] == postorder[postend]) {
            break;
        }
    }
    
    int leftLen = mid - instart;
    node->left = buildTreeImp(inorder, instart, instart + leftLen - 1, postorder, poststart, poststart + leftLen - 1);
    node->right = buildTreeImp(inorder, instart + leftLen + 1, inend, postorder, poststart + leftLen, postend - 1);
    
    return node;
}

struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize)
{
    return buildTreeImp(inorder, 0, inorderSize - 1, postorder, 0, postorderSize - 1);
}

```



## 108. [将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

```
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree



C 实现

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* helper(int* nums, int start, int end) 
{
    if (start > end) {
        return NULL;
    }

    int mid = (start + end) >> 1;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = nums[mid];
    root->left = helper(nums, start, mid - 1);
    root->right = helper(nums, mid + 1, end);
    return root;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize)
{
    return helper(nums, 0, numsSize - 1);
}
```



## 121. [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```


示例 2:

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock



C 实现

```c
int maxProfit(int* prices, int pricesSize)
{
    if (pricesSize <= 0) return 0;
    
    int min, minPos, max;
    min = prices[0];
    minPos = 0;
    max = 0;
    
    for (int i = 1; i < pricesSize; i++) {
        if (i > minPos && prices[i] - min  > max) {
            max = prices[i] - min;
        }
        if (prices[i] < min) {
            min = prices[i];
            minPos = i;
        }
    }
    
    return max;
}
```



## 122. [买卖股票的最佳时机II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

```
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii



C 实现

```c
/* 思路：每笔交易最大收益：最高价-最低价。交易完成更新最低价和最高价 */

int maxProfit(int* prices, int pricesSize)
{
    if (pricesSize == 0) {
        return 0;    
    }
    
    int min = prices[0];
    int minPos = 0;
    int max = prices[0];
    int maxPos = 0;
    int profit = 0;
    
    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] < max && maxPos > minPos) {
            profit += (max - min);
            minPos = i;
            min = prices[i];
            maxPos = i;
            max = prices[i];
            continue;
        }
        
        if (prices[i] <  min) {
            min = prices[i];
            minPos = i;
            max = prices[i];
            maxPos = i;
        }
        
        if (prices[i] > max) {
            max = prices[i];
            maxPos = i;
        }
    }
    
    if (max > min && maxPos > minPos) {
        profit += max - min;
    }
    
    return profit;
}c
```





## 123 [买卖股票的最佳时机III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

```
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii



C++ 实现

```c++
/*
 * 思路：先顺序遍历一遍求A[i]：表示(0,i)范围内一次交易的最大利润，
 *      然后逆序遍历一遍求B[j]：表示(j, n)范围内一次交易的最大利润，
 *      求max{A[i] + B[i + 1]} i = {0,...,n}
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        if(len<=1) return 0;
        int max_profit;
        vector<int> profits;
        profits.resize(len);
        
        int min_price = prices[0];
        max_profit = 0;
        for(int i=1; i<len; i++)
        {
            if(prices[i] - min_price > max_profit)
            {
                max_profit = prices[i] - min_price;
            }
            profits[i] = max_profit;
            if(prices[i] < min_price)
                min_price = prices[i];
        }
        
        int max_price = prices[len-1];
        int max_profit_i_n = 0;
        for(int i=len-2; i>=2; i--){
            if(max_price - prices[i] > max_profit_i_n)
            {
                max_profit_i_n = max_price - prices[i];
            }
            if(max_price < prices[i])
                max_price = prices[i];
            max_profit = max_profit > (max_profit_i_n + profits[i-1])? max_profit:max_profit_i_n + profits[i-1];
        }
        
        return max_profit;
        
    }
};
```



## 129. [求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)

给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。



C 实现

```c
    /**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int path[1024];
int pos = 0;
long long ans = 0;

void sumNumbersImp(struct TreeNode* root)
{
    if (root == NULL) return;
    
    path[pos++] = root->val;
    if (root->left == NULL && root->right == NULL) {
        int sum = 0;
        for (int i = 0; i < pos; i++) {
            sum = sum*10 + path[i];
        }
        ans += sum;
        pos--;
        return;
    }            
    
    sumNumbersImp(root->left);
    sumNumbersImp(root->right);
    pos--;
    
    return;
}

int sumNumbers(struct TreeNode* root){
    ans = 0;
    pos = 0;
    sumNumbersImp(root);
    return ans;
}
```



## 67. [二进制求和](https://leetcode-cn.com/problems/add-binary/)

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为**非空**字符串且只包含数字 `1` 和 `0`。

示例 1:

```
输入: a = "11", b = "1"
输出: "100"
```


示例 2:

```
输入: a = "1010", b = "1011"
输出: "10101"
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary



C 实现

```c
static inline void reverse(char* s, int len) 
{
    char tmp;
    for (int i = 0; i < len - 1 - i; i++) {
        tmp = s[i];
        s[i] = s[len - 1 - i];
        s[len - 1 - i] = tmp;
    }
}

char * addBinary(char * a, char * b)
{
    int lena = strlen(a);
    int lenb = strlen(b);
    
    char* ans = (char*)malloc(sizeof(char) * ((lena > lenb ? lena : lenb)  + 2));
    
    int i = lena - 1;
    int j = lenb - 1;
    int carry = 0;
    int pos = 0;
    int digit;
    while (i >= 0 && j >= 0) {
        digit = (a[i] - '0') + (b[j] - '0') + carry;
        ans[pos++] = digit%2 + '0';
        carry = digit/2;
        i--;
        j--;
    }
    
    char* p;
    int k = -1;
    if (i >= 0) {
        p = a;
        k = i;
    }
    else if (j >= 0) {
        p = b;
        k = j;
    }
    
    while (k >= 0) {
        digit = p[k] - '0' + carry;
        ans[pos++] = digit%2 + '0';
        carry = digit/2;
        k--;
    }
    if (carry) {
        ans[pos++] = '1';
    }
    reverse(ans, pos);
    ans[pos] = '\0';
    
    return ans;
}
```



## 85. [最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

```
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle



C 实现

```c
/* 思路: 
 * 1.使用累积和法和方法求子矩阵的和
 * 2.使用累积和法统计子矩阵0的个数，0的个数为0表示一个只包含1的子矩阵
 */

int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize)
{
    if (matrix == NULL || matrixSize == 0) {
        return 0;
    }
    
    int colSize = matrixColSize[0];
    int **z, **sum;
    int i,j,h,k;
    int ans = 0;

    z = (int**)malloc(sizeof(int*) * matrixSize);
    sum = (int**)malloc(sizeof(int*) * matrixSize);
    
    for (i = 0; i < matrixSize; i++) {
        z[i] = (int*)malloc(sizeof(int) * colSize);
        sum[i] = (int*)malloc(sizeof(int) * colSize);
        for (j = 0; j < colSize; j++) {
            z[i][j] = 0;
            sum[i][j] = 0;
        }
    }
    
    for (i = 0; i < matrixSize; i++) {
        for (j = 0; j < matrixColSize[i]; j++) {
            z[i][j] = '0' - matrix[i][j] + 1;
            sum[i][j] = matrix[i][j] - '0';
            
            if (i > 0) {
                z[i][j] += z[i - 1][j]; // add from left
                sum[i][j] += sum[i - 1][j];
            }
            if (j > 0) {
                z[i][j] += z[i][j - 1]; // add from top
                sum[i][j] += sum[i][j - 1];
            }
            if (i > 0 && j > 0) {
                z[i][j] -= z[i - 1][j - 1];
                sum[i][j] -= sum[i - 1][j - 1];
            }
        }
    }
    
    for (i = 0; i < matrixSize; i++) {
        for (j = 0; j < colSize; j++) {
            if (matrix[i][j] == '0') continue;
            for (h = i; h < matrixSize; h++) {
                for (k = j; k < colSize; k++) {
                    if (matrix[h][k] == '0') break;
                    int zeroSum = z[h][k];
                    int oneSum = sum[h][k];
                    if (i > 0) {
                        zeroSum -= z[i - 1][k];
                        oneSum -= sum[i - 1][k];
                    }
                    if (j > 0) {
                        zeroSum -= z[h][j - 1];
                        oneSum -= sum[h][j - 1];
                    }
                    if (i > 0 && j > 0) {
                        zeroSum += z[i - 1][j - 1];
                        oneSum += sum[i - 1][j - 1];
                    }
                    
                    if (zeroSum == 0 && oneSum > ans) {
                        ans = oneSum;
                    }
                }
            }
        }
    }
    
    return ans;
}
```

