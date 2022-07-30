class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.index+1]
        self.stack.append(url)
        self.index += 1
        

    def back(self, steps: int) -> str:
        if self.index - steps >=0 :
            self.index -= steps
            return self.stack[self.index]
        else:
            self.index = 0
            return self.stack[0]

        
    def forward(self, steps: int) -> str:
        if self.index + steps <= len(self.stack)-1:           
            self.index += steps
            return self.stack[self.index]
        else:
            self.index = len(self.stack)-1
            return self.stack[self.index]

        


# Your BrowserHistory object will be instantiated and called as such:
browserHistory  = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com");
browserHistory.visit("youtube.com");  
print("back ",browserHistory.back(1))
print("back ",browserHistory.back(1))
print("back ",browserHistory.forward(1))
browserHistory.visit("linkedin.com"); 
print("forword ",browserHistory.forward(2))
print("back ",browserHistory.back(2))
print("back ",browserHistory.back(7))