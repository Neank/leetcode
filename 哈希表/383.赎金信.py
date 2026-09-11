#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#

# @lc code=start
'''思路
遍历一遍ransonNote记录可用字符数量，遍历magazine时每用一个-1,
如果掉到0以下说明不够用，返回错误
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        nums1 = [0] * 26
        for str in magazine:
            nums1[ord(str) - 97] += 1
        for str in ransomNote:
            i = ord(str) - 97
            nums1[i] -= 1
            if nums1[i] < 0:
                return False
        return True
        
# @lc code=end

