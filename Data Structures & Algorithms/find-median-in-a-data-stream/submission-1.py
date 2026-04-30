class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        

    def findMedian(self) -> float:
        n = len(self.arr)
        if n%2==1:
            return self.arr[int(n//2)]
        else:
            k = int(n//2)
            return (self.arr[k-1]+self.arr[k])/2




        
        