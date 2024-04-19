class ListNode:
    def __init__(self, url = "", next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr, None)
        self.curr = self.curr.next
        
    def back(self, steps: int) -> str:
        curr = self.curr
        x = 0

        while curr and curr.next and x < steps:
            curr = curr.next
            x += 1
        
        self.curr = curr
        return self.curr.next

        

    def forward(self, steps: int) -> str:
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)