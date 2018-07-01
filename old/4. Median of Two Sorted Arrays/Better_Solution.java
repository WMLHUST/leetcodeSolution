public class Solution 
{
	public double findMedianSortedArrays(int[] nums1, int[] nums2) 
	{
		double now=0;
		double pre=0;
		int n = (nums1.length+nums2.length)/2+1;
		int i=0;
		int j=0;
		int k=0;
		while(k<n)
		{
			pre = now;
			if(i==nums1.length)
			{
				now = nums2[j++];
			}
			else if(j==nums2.length)
			{
				now = nums1[i++];
			}
			else now = nums1[i]<nums2[j]?nums1[i++]:nums2[j++];
			k++;
		}
		return (nums1.length+nums2.length)%2==1?now:(pre+now)/2;
	}
}