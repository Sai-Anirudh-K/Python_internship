class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=="(":
                st.append(i)
            if i==")":
                if s[-1]!="(":
                    c= False
                else:
                    st.append(i)
                    c=True
            if i=="[":
                st.append(i)
            if i=="]":
                if s[-1]!="[":
                    c= False
                else:
                    st.append(i)
                    c=True
            if i=="{":
                st.append(i)
            if i=="}":
                if s[-1]!="{":
                    c= False
                else:
                    st.append(i)
                    c=True
        print(c) 
o=Solution()
o.isValid("()")