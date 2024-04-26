class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        for i in candies:
            c=candies[i]+extraCandies
            if(c>max(candies)):
                result.append(True)
            else:
                result.append(False)
        