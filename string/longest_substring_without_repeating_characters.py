# @see https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0
        for end in range(len(s)):
            # すでにその文字をendで見ていたら (seenにその文字が入ってたら)
            if s[end] in seen:
                # start位置を変更しておく
                start = seen[s[end]] + 1

            # 次のループのために、チェックし終わったendのインデックスを保存しておく { end_s: index }
            seen[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length
