# @see https://blog.devgenius.io/leetcode-69-sqrt-x-86679311b8a0
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        print(x)
        start = 0
        end = x / 2
        while start <= end:
            print(start)
            print(end)
            mid = int((start + end) / 2)
            square = mid**2
            print(square)
            if square == x:
                print("return mid (square == x)")
                print(mid)
                return mid
            # 🔵 midから近い値をどんどん探していく感じ
            # square == x　になれば、そのmidが sqrtと呼べる (sqrt == mid**2 だから)
            if square > x:
                print("square > x")
                end = mid - 1
            else:
                print("square < x")
                start = mid + 1

        # 割り切れなかったら、一番近い整数で、小数点を切り捨てて返す
        return end
