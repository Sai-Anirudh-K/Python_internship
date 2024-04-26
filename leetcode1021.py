class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        st=""
        for i in s:
            if i=="(":
                if count==0:
                    pass
                else:
                    st+=i
                count+=1

            if i==")":
                if count==1:
                    pass
                else:
                    st+=i
                count-=1
        print(st)
o=Solution()
o.removeOuterParentheses("(()())(())")