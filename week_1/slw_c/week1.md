# Week1

[TOC]

## 162. [寻找峰值](https://leetcode-cn.com/problems/find-peak-element)

峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element



C++实现

```c++
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        bool up = true;
        int n = nums.size();
        int s = 0, e = n - 1;
        int mid;
        
        while(s < e) {
            mid = (s + e)>>1;
            if (nums[mid] < nums[mid + 1]) {
                s = mid + 1; // 右边有峰值
            }
            else if (nums[mid] > nums[mid + 1]) {
                e = mid; //左边有峰值
            }
        }
        
        return s;
    }
};
```



##  167. [两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted)

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted

C语言实现

```C
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int s,e;
    s = 0;
    e = numbersSize - 1;
    
    int *res = (int*) malloc(sizeof(int) * 2);
    *returnSize = 2;
    
    while(s < e) {
        if (numbers[s] + numbers[e] < target) {
            s++;
        }
        else if (numbers[s] + numbers[e] > target) {
            e--;
        }
        else {
            res[0] = s + 1;
            res[1] = e + 1;
            break;
        }
    }
    
    if (s == e) {
        *returnSize = 0;
        return NULL;
    }
    
    return res;
}
```



## 141. [环形链表](https://leetcode-cn.com/problems/linked-list-cycle)

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle



C++ 实现

```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) return false;
        
        ListNode* p1 = head;
        ListNode* p2 = head->next;
        
        bool flag = false;
        while(p1 != NULL && p2 != NULL) {
            if (p2 == p1) {
                flag = true;
                break;
            }
            
            p2 = p2->next;
            if (p2 == p1) {
                flag = true;
                break;
            }
            if (p2 != NULL) p2 = p2->next;
            
            p1 = p1->next;
        }
        
        return flag;
    }
};
```



## 226. [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree)

翻转一棵二叉树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree



C++实现

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) return NULL;
        
        TreeNode* left = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(left);
        return root;
    }
};
```



## 103. [二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal)

给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回锯齿形层次遍历如下：

```
[
  [3],
  [20,9],
  [15,7]
]
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/



C++实现

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
/*
 解法：每层向左遍历和向右遍历都可以看作出栈和入栈操作
*/

#include <stack>
using namespace std;

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        stack<TreeNode*> left; // 从左至右
        stack<TreeNode*> right; // 从右至左
        TreeNode* p;
        vector<vector<int>> ans;
        
        left.push(root);
        int level = 0;
        while(!left.empty() || !right.empty()) {
            vector<int> levelVector;
            if (!(level % 2)) { 
                while(!left.empty()) {
                    p = left.top();
                    if (!p) {
                        left.pop();
                        continue;
                    }
                    levelVector.push_back(p->val);
                    right.push(p->left);
                    right.push(p->right);
                    left.pop();
                }
            }
            else {
                while(!right.empty()) {
                    p = right.top();
                    if (!p) {
                        right.pop();
                        continue;
                    }
                    levelVector.push_back(p->val);
                    left.push(p->right);
                    left.push(p->left);
                    right.pop();
                }
            }
            
            if (levelVector.size()) {
                ans.push_back(levelVector);
            }
            level++;
        }
        
        return ans;
    }
};
```



## 144. [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal)

C++ 实现

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

/*
class Solution {
public:
    void preTra(TreeNode * root, vector<int>& v)
    {
        if (!root) return;
        v.push_back(root->val);
        preTra(root->left, v);
        preTra(root->right, v);
        return;
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        preTra(root, ans);
        return ans;
    }
};
*/

#include <stack>
using namespace std;

class Solution {
public:
    
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> s;
        TreeNode* p;
        
        if (!root) return ans;

        s.push(root);
        while(!s.empty()) {
            p = s.top();
            s.pop();
            if (p) {
                ans.push_back(p->val);
                s.push(p->right);
                s.push(p->left);  
            }
        }
        return ans;
    }
};
```



## 145. [二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

C++ 实现

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
/*
class Solution {
public:
    void postTraver(TreeNode* root, vector<int>& ans) 
    {
        if (!root) return;
        postTraver(root->left, ans);
        postTraver(root->right, ans);
        ans.push_back(root->val);
    }
    
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        postTraver(root, ans);
        return ans;
    }
};
*/
#include <stack>
using namespace std;

typedef struct tagVisit {
    TreeNode* root;
    bool leftVisit;
    bool rightVisit;
}Visit;

class Solution {
public:
    
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<Visit> s;
        
        Visit v;
        v.root = root;
        v.leftVisit = false;
        v.rightVisit = false;
        s.push(v);
            
        while(!s.empty()) {
            Visit& v = s.top();
            if (v.root == NULL) {
                s.pop();
                continue;
            }
            
            if (v.leftVisit && v.rightVisit) {
                ans.push_back(v.root->val);
                s.pop();
            }
            else {
                v.leftVisit = true;
                v.rightVisit = true;
                
                Visit v1;
                v1.root = v.root->left;
                v1.leftVisit = false;
                v1.rightVisit = false;
                
                Visit v2;
                v2.root = v.root->right;
                v2.leftVisit = false;
                v2.rightVisit = false;
                s.push(v2);
                s.push(v1);
            } 
        }
        
        return ans;
    }
};
```



## 166. [分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal)

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal

```C++
#include <stdio.h>
#include <map>
#include <string>

using namespace std;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        long long n = numerator;
        long long d = denominator;
        string ans;
        char buffer [33];
        
        int singed = 1;
        if (n < 0) {
            n = n*(-1);
            singed  = -1;
        }
        if (d < 0) {
            d = d*(-1);
            singed *= (-1);
        }
        
        if (singed == -1 && n != 0) {
            ans.push_back('-');
        }
        
        if (n < d) ans.push_back('0');
        if(n >= d){
            sprintf(buffer, "%ld", n/d);
            ans.insert(ans.size(), buffer);
            n -= (n/d)*d;
        }
        
        if (!n) return ans;
        
        ans.push_back('.');
        
        map<int, int> nMap;
        int i = 1;
        int digit;
        int pos = ans.size() - 1;
        while (n && nMap.find(n) == nMap.end())
        {
            nMap[n] = i;
            digit = n*10/d;
            ans.push_back(digit + '0');
            n = n*10 - d*digit;
            i++;
        }
        
        if (nMap.find(n) != nMap.end()){
            ans.push_back(')');
            ans.insert(pos + nMap[n], 1, '(');
        }
        
        return ans;
    }
};
```



## 139. [单词拆分](https://leetcode-cn.com/problems/word-break)

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

```
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
```

示例 2：

```
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
```


示例 3：

```
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break



C实现

```c
#include <string.h>

bool wordBreak(char * s, char ** wordDict, int wordDictSize){
    int n = strlen(s);
    bool* dp = (bool*)malloc(sizeof(bool)*(n+1));
    
    for (int i = 0; i < n + 1; i++) {
        dp[i] = false;
    }
    
    dp[n] = true;
    
    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < wordDictSize; j++) {
            int len = strlen(wordDict[j]);
            if (i + len - 1 < n  
                && !strncmp(s + i, wordDict[j], len)
                && dp[i + len]) {
                dp[i] = true;
            }
        }
    }
    
    return dp[0];
}
```



## 198. [打家劫舍](https://leetcode-cn.com/problems/house-robber)

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

```
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

示例 2:

```
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber



C++ 实现

```c++
/*
  dp方程： f[i] = max{f[i + 2] + a[i], f[i + 1]}
*/
#include <algorithm>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        
        int size = nums.size();
        vector<int> dp(size, 0);
        dp[size - 1] = nums[size - 1];
        dp[size - 2] = max(nums[size - 2], nums[size - 1]);
        
        for (int i = size - 3; i >= 0; i--) {
            dp[i] = max(dp[i + 2] + nums[i], dp[i + 1]);
        }
        
        return dp[0];
    }
};
```



## 213. [打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii)

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

```
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```


示例 2:

```
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii



C++ 实现

```c++
/*
    偷第一间：a[0] + f(2), f[n - 1] = 0
    不偷第一间：f[1], f[n - 1] = a[n - 1]
    
    f[i] = max{a[i] + f[i + 2], f[i + 1]}
*/

#include <algorithm>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int ans1, ans2;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return max(nums[0], nums[1]);

        vector<int> dp(n, 0);
        
        // 偷第一间
        dp[n - 1] = 0;
        dp[n - 2] = nums[n - 2];
        for(int i = n - 3; i >= 2; i--) {
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1]);
        }
        ans1 = nums[0] + dp[2];
        
        // 不偷第一间
        dp[n - 1] = nums[n - 1];
        dp[n - 2] = max(nums[n - 2], nums[n - 1]);
        for (int i = n - 3; i >= 1; i--) {
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1]);
        }
        ans2 = dp[1];
        
        return max(ans1, ans2);
    }
};
```



## 264. [丑数 II](https://leetcode-cn.com/problems/ugly-number-ii)

编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

```
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```


说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii



C 实现

```c
#define MAX_NUM 1700

int nthUglyNumber(int n)
{
    int *u = (int*)malloc(sizeof(int) * MAX_NUM);
    
    int pos;
    int t2 = 0;
    int t3 = 0;
    int t5 = 0;
    
    u[0] = 1;
    pos = 1;
    while (pos < n) {
        int m2 = u[t2] * 2;
        int m3 = u[t3] * 3;
        int m5 = u[t5] * 5;
        
        int min = m2;
        if (m3 < min) min = m3;
        if (m5 < min) min = m5;
        
        u[pos++] = min;
        
        if (min == m2) t2++;
        if (min == m3) t3++;
        if (min == m5) t5++;
    }
    
    int result = u[pos - 1];
    free(u);
    
    return result;
}
```



## 326. [3的幂](https://leetcode-cn.com/problems/power-of-three/)

给定一个整数，写一个函数来判断它是否是 3 的幂次方。



C++ 实现

```c++
class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) return false;
        
        while(n%3 == 0) {
            n /= 3;
        }
        
        return n==1;
    }
};
```



## 202. [快乐数](https://leetcode-cn.com/problems/happy-number)

编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

```
输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number



C++ 实现

```c++
#include <set>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        int input = n;
        set<int> s;
        do
        {
            s.insert(n);
            int temp = 0;
            int digit;
            while (n) {
                digit = n % 10;
                temp += digit*digit;
                n /= 10;
            }
            n = temp;
        }while(s.find(n) == s.end() && n != 1);
        
        return n == 1;
    }
};
```



## 231. [2的幂](https://leetcode-cn.com/problems/power-of-two)

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。



C++ 实现

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n == 0) return false;      
        int i = 0;
        int count = 0;
        while(n && count <= 1) {
            if (n & 1) {
                count++;
            }
            
            n >>= 1;
        }
        
        return !(n & 1) && count == 1 ? true : false;
    }
};
```



## 100. [相同的树](https://leetcode-cn.com/problems/same-tree)

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。



C++ 实现

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    bool isPreSame(TreeNode* p, TreeNode* q) 
    {
        if (p == NULL && q == NULL) return true;
        if (p == NULL || q == NULL) return false;
        
        return ((p->val == q->val) && isPreSame(p->left, q->left) && isPreSame(p->right, q->right));
    }
    
    
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return isPreSame(p,q);
    }
};
```

