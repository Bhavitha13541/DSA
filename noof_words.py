from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(s.split()) for s in sentences)


if __name__ == "__main__":
    sentences = [
        "alice and bob love leetcode",
        "i think so too",
        "this is great thanks very much"
    ]

    obj = Solution()
    print(obj.mostWordsFound(sentences))

    # output:
    # 6
