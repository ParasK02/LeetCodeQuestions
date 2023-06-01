class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length = len(word1) + len(word2) 
        out = ""
        for x in range(0,length):
            out += word1[x]
            out+= word2[x]

            if x == len(word1)-1:
                out+=word2[x+1:len(word2)]
                return out

            elif x == len(word2)-1:
                out+=word1[x+1:len(word1)]
                return out
        return out
