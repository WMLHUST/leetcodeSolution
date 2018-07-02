public class Solution 
{
	public ListNode addTwoNumbers(ListNode l1, ListNode l2)
	{
		ListNode headNode = null;
		ListNode listNode = null;
		int extra = 0;
		int val = 0;
		int l1_val = 0;
		int l2_val = 0;
		for (int i = 0; ; i++) 
		{			
			if (null == l1)	{
				l1_val = 0;
			}
			else {
				l1_val = l1.val;
			}
			
			if (null == l2)	{
				l2_val =0;
			}
			else {
				l2_val = l2.val;
			}
			
			int sum = l1_val + l2_val + extra;
			if(sum >= 10){
				val = sum % 10;
				extra = 1;
			}
			else{
				val = sum;
				extra = 0;
			}
			
			
			if (0 == i)	{
				//保存头结点
				l1.val = val;
				listNode = l1;
				headNode = listNode;
			}
			else{
				ListNode node = (l1 == null)?l2:l1;
				node.val = val;
				listNode.next  = node;	
				listNode = node;
				//System.out.println("get next node");
			}
			
			if (l1 != null) 
			{
				l1 = l1.next;
			}
			if (l2 != null)
			{
				l2 = l2.next;
			}
			
			if (l1 == null && l2 == null)
			{
				if(0 != extra)
				{
					listNode.next = new ListNode(extra);
				}
				
				break;
			}
		}
		
		return headNode;
	}
}
