# @see https://github.com/criszhou/LeetCode-Python/blob/master/050.%20Pow(x%2C%20n).py
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        # e.g. x: 2, n: -2
        # x: 1/2 => 0.5, n: 2
        # 1の逆数にしておけば、別にマイナスにしなくて良い
        # x^(-n) => x^((-1)(n)) => x^(-1) * x^(n)
        if n < 0:
            x = 1.0 / x
            n = -n

        if n == 1:
            return x

        # '**' はべき乗
        # '//' は割り算の整数部
        if n % 2 == 1:
            # exponent: odd
            # ? なぜxを欠けて再起させている？
            # -> n は整数であり、n//2することで偶数を出せる
            # -> かつ xをかけることによって nをどんどん減らしていくことができる(n: 1 まで再起する)
            return x * self.myPow(x**2, n // 2)
        else:
            # exponent: even
            return self.myPow(x**2, n // 2)
