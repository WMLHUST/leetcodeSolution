public class Solution 
{
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    	double result = 0;
    	
    	int nums1_len = nums1.length;
    	int nums2_len = nums2.length;
    	
    	if(0 == nums1_len)
    	{
    		if (1 == nums2_len) 
    		{
    			return nums2[0];
			}
    		else
    		{
    			int median_2 = nums2_len / 2;
        		if(0 == nums2_len % 2)
        		{
        			return (nums2[median_2 - 1] + nums2[median_2]) / 2.0;
        		}
        		else
        		{
        			return (nums2[median_2]);
        		}
			}
    	}
    	else if (0 == nums2_len) 
    	{
    		if(1 == nums1_len)
    		{
    			return nums1[0];
    		}
    		else
    		{
    			int median_1 = nums1_len / 2;
    			if (0 == nums1_len % 2)
    			{
    				return (nums1[median_1 - 1] + nums1[median_1]) / 2.0;
    			}
    			else
    			{
    				return (nums1[median_1]);
    			}
			}
		}
    	else if(1 == nums1_len && 1 == nums2_len)
    	{
    		return (nums1[0] + nums2[0]) / 2.0;
		}
    	
    	int median_i = (nums1_len + nums2_len) / 2;
    	int nums1_i = -1;
    	int nums2_i = -1;
    	for (int i = 0; i < median_i; i++)
    	{
    		if (nums1_i + 1 > nums1_len - 1)
    		{
    			nums2_i++;
			}
    		else if (nums2_i + 1 > nums2_len - 1)
    		{
    			nums1_i++;
			}
    		else 
    		{
    			if (nums1[nums1_i + 1] <= nums2[nums2_i + 1])
    			{
    				nums1_i++;
				}
    			else
    			{
    				nums2_i++;
				}
			}
		}
    	
//    	System.out.println("1i = " + nums1_i + ", 2i = " + nums2_i);
    	
    	if ((nums1_len + nums2_len) % 2 == 0)
    	{
    		//even
    		if (nums1_i + 1 == nums1_len)
    		{
    			if (-1 == nums2_i) 
    			{
    				result = (nums1[nums1_i] + nums2[nums2_i + 1]) / 2.0;
				}
    			else if (nums1[nums1_i] > nums2[nums2_i])
    			{
    				result = (nums1[nums1_i] + nums2[nums2_i + 1]) / 2.0;
				}
    			else
    			{
    				result = (nums2[nums2_i] + nums2[nums2_i + 1]) / 2.0;
    			}
			}
    		else if(nums2_i + 1 == nums2_len)
    		{
    			if (-1 == nums1_i) 
    			{
    				result = (nums1[nums1_i + 1] + nums2[nums2_i]) / 2.0;
				}
    			else if (nums2[nums2_i] > nums1[nums1_i])
				{
					result = (nums2[nums2_i] + nums1[nums1_i + 1]) / 2.0;
				}
				else
				{
					result = (nums1[nums1_i] + nums1[nums1_i + 1]) / 2.0;
				}
			}
    		else
    		{
    			if (nums1[nums1_i + 1] < nums2[nums2_i + 1])
    			{
    				nums1_i++;
				}
    			else 
    			{
					nums2_i++;
				}
    			
    			if (-1 == nums1_i) 
    			{
					result = (nums2[nums2_i - 1] + nums2[nums2_i]) / 2.0;
				}
    			else if(-1 == nums2_i)
    			{
					result = (nums1[nums1_i - 1] + nums1[nums1_i]) / 2.0;
				}
    			else if(nums2_i != 0 && nums1[nums1_i] < nums2[nums2_i - 1])
    			{
    				result = (nums2[nums2_i - 1] + nums2[nums2_i]) / 2.0;
    			}
    			else if(nums2_i == 0 && nums2[nums2_i] < nums1[nums1_i - 1])
    			{
    				result = (nums1[nums1_i - 1] + nums1[nums1_i]) / 2.0;
    			}
    			else if(nums1_i != 0 && nums2[nums2_i] < nums1[nums1_i - 1])
    			{
    				result = (nums1[nums1_i - 1] + nums1[nums1_i]) / 2.0;
    			}
    			else if(nums1_i == 0 && nums1[nums1_i] < nums2[nums2_i - 1])
    			{
    				result  = (nums2[nums2_i - 1] + nums2[nums2_i]) / 2.0;
    			}
    			else
    			{
    				result = (nums1[nums1_i] + nums2[nums2_i]) / 2.0;
				}
			}
    		
		}
    	else 
    	{
			//Odd total count
    		if (nums1_i + 1 == nums1_len) 
    		{
    			result = nums2[nums2_i + 1];
			}
    		else if(nums2_i + 1 == nums2_len)
    		{
    			result = nums1[nums1_i + 1];
    		}
    		else
    		{
				if (nums2[nums2_i + 1] > nums1[nums1_i + 1]) 
    			{
    				result = nums1[nums1_i + 1];
				}
    			else
    			{
    				result = nums2[nums2_i + 1];
				}
			}
		}
    	
    	return result;
    }
}