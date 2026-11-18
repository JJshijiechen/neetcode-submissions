class Solution:  # 使用 LeetCode 要求的类名
    def minWindow(self, s: str, t: str) -> str:  # 返回包含 t 所有字符的最短子串
        if len(t) > len(s):  # 如果 t 比 s 还长，不可能找到符合要求的子串
            return ""  # 无解时返回空字符串
        need = [0] * 128  # 题目只有英文字母，用 ASCII 下标记录字符需求
        for char in t:  # 遍历 t，统计每个字符需要出现多少次
            need[ord(char)] += 1  # 增加当前字符的需求次数
        missing = len(t)  # 记录窗口总共还缺多少个字符，重复字符分别计数
        left = 0  # 窗口的左边界
        best_start = 0  # 当前最短答案的起点
        best_length = len(s) + 1  # 初始化为不可能达到的长度，表示尚未找到答案
        for right in range(len(s)):  # 逐步向右扩大窗口
            right_index = ord(s[right])  # 找到新加入字符在 need 中的位置
            if need[right_index] > 0:  # 如果窗口原本还缺这个字符
                missing -= 1  # 加入它后，总缺口减少一个
            need[right_index] -= 1  # 更新需求；负数表示该字符在窗口中有多余
            while missing == 0:  # 窗口有效时，尝试从左边缩短它
                window_length = right - left + 1  # 计算当前窗口长度
                if window_length < best_length:  # 如果当前窗口比已记录答案更短
                    best_start = left  # 记录新的答案起点
                    best_length = window_length  # 记录新的答案长度
                left_index = ord(s[left])  # 找到即将移出窗口的字符
                need[left_index] += 1  # 移出它，因此恢复一份需求
                if need[left_index] > 0:  # 正数说明移出后窗口缺少这个字符
                    missing += 1  # 窗口不再有效，下一轮需要继续向右扩大
                left += 1  # 无论移出的是否为多余字符，都推进左边界
        if best_length > len(s):  # 如果答案长度从未更新过
            return ""  # 表示不存在符合要求的子串
        return s[best_start:best_start + best_length]  # 截取并返回最短答案