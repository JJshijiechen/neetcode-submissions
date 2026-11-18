class Solution:  # 使用题目要求的类名
    def getSum(self, a: int, b: int) -> int:  # 返回 a 与 b 的和
        mask = 0xFFFFFFFF  # 保留低 32 位，模拟固定宽度整数
        sign_bit = 0x80000000  # 32 位整数的符号位
        a &= mask  # 将 a 转成 32 位表示，包括负数
        b &= mask  # 将 b 转成 32 位表示，包括负数
        while b != 0:  # b 在每轮代表尚未处理的进位
            carry = ((a & b) << 1) & mask  # 两个位置都为 1 时，产生向左移动一位的进位
            a = (a ^ b) & mask  # 异或得到暂时不考虑进位的和
            b = carry  # 下一轮把进位加入暂时的和
        if a < sign_bit:  # 最高位为 0，结果是非负数
            return a  # 直接返回非负结果
        return ~(a ^ mask)  # 最高位为 1，将 32 位表示转回 Python 负整数