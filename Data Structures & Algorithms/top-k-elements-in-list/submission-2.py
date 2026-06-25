class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        frequent = []
        for num in nums:
            counts[num] += 1
        print(counts)
        print(counts.values())
        counts = sorted(counts.keys(), key=lambda x: counts[x], reverse = True)
        print(counts)
        return counts[0:k]