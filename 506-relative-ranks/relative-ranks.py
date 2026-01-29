class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [None] * len(score) 

        #first make heap
        max_heap=[]
        for i, s in enumerate(score):
            heappush(max_heap, (-s,i))

        #store in ans
        num=1
        while max_heap:
            s,i=heappop(max_heap)

            if num<4:
                ans[i]=rank[num-1]
            else:
                ans[i]=str(num)
            num+=1
        return ans
        