class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        news=[]
        newt=[]
        for char in s:
            if char!='#':
                news.append(char)
            else:
                if news:
                    news.pop()
        
        for char in t:
            if char!='#':
                newt.append(char)
            else:
                if newt:
                    newt.pop()
        
        if(news==newt):
            return True
        else:
            return False
        