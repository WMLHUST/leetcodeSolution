public class Solution {
	public int lengthOfLongestSubstring(String s) 
	{			
		int preCur = 0;
		
		int result = 0;
		int[] posArray = new int['~' - 0 + 1];
		for (int i = 0; i < posArray.length; i++) {
			posArray[i] = -1;
		}
		
		for (int i = 0; i < s.length(); i++)
		{
			char ch = s.charAt(i);
			
			if(posArray[ch] >= preCur)
			{
				//最近一次出现的位置在pre后面
				result = result>(i-preCur) ? result : (i-preCur);

				preCur = posArray[ch] + 1;					
				posArray[ch] = i;
			}
			posArray[ch] = i;
		}
		
		result = result>(s.length()-preCur) ? result : (s.length()-preCur);
		
		return result;
	}
}