class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[]]
        if len(strs) == 1:
            return [strs]
        anagrams = []
        words = {}
        for word in strs:
            letters = {}
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
            if letters not in anagrams:
                anagrams.append(letters)
                index = anagrams.index(letters)
                words[index] = [word]
            else:
                index = anagrams.index(letters)
                words[index].append(word)

        return list(words.values())
