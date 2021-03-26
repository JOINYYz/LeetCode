class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.stream = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey = idKey -1
        self.stream[idKey] = value
        if self.stream[self.ptr] == None:
            return []
            
        else:
            tmp = self.ptr
            output = []
            #注意index溢出
            while self.ptr+1 < len(self.stream) and self.stream[self.ptr+1] != None:
                self.ptr+=1
            # list[0:0] = []
            if tmp == self.ptr:
                output.append(self.stream[tmp])
             #注意索引位置
            if tmp < self.ptr:
                output.extend(self.stream[tmp:self.ptr+1])
            self.ptr+=1
        return output


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
