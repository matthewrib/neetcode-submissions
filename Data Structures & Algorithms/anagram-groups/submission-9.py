class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs: # to go through each item in strs
            count = [0] * 26
            for char in string: # to go through each char in strs
                count[ord(char) - ord('a')] += 1 
            result[tuple(count)].append(string)
        return list(result.values())
