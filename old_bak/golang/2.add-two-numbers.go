/*
 * @lc app=leetcode id=2 lang=golang
 *
 * [2] Add Two Numbers
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	c1 := l1
	c2 := l2
	var res ListNode
	cr := &res
	carry := 0
    for {
		if c1 == nil && c2 == nil {
			break
		}
		
		var c1Num int
		if c1 != nil{
			c1Num = c1.Val
			c1 = c1.Next
		}

		var c2Num int
		if c2 != nil {
			c2Num = c2.Val
			c2 = c2.Next
		}
		
		sum := c1Num + c2Num + carry
		if sum >= 10 {
			sum = sum - 10
			carry = 1
		} else {
			carry = 0
		}

		cr.Next = &ListNode {
			Val: sum,
		}
		cr = cr.Next
	}

	if carry > 0 {
		cr.Next = &ListNode {
			Val: carry,
		}
	}

	return res.Next
}

