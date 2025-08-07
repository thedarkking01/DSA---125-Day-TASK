class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        w=sentence.split(" ")
        for i in range(len(w)):
            if w[i][0]!=w[i-1][-1]:
                return False
        return True
    
# iterative solution(space optimized)
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]