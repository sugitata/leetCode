# @see https://zhenyu0519.github.io/2020/07/24/lc207/
import collections

# Directed acyclic graph (DAG) and Topological sorts question
# @see https://en.wikipedia.org/wiki/Directed_acyclic_graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ? なんだこれは？
        # -> https://qiita.com/xza/items/72a1b07fcf64d1f4bdb7#defaultdict-%E3%81%AE-%E5%88%A9%E7%94%A8
        # setという関数に従ってdictionaryを作成することができる
        # for all courses with their prerequisites -> 前提条件に対する全てのコース
        courses = collections.defaultdict(set)
        # all prerequisites with their courses -> コースに対する全ての前提条件
        pres = collections.defaultdict(set)
        # course -> index
        # pre -> value
        # @see https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
        for course, pre in prerequisites:
            # e.g. numCourses: 2, prerequisites: [[1, 0], [0, 1]]
            courses[course].add(pre)  # [0: [1, 0], 1: [0, 1]]
            pres[pre].add(course)  # [[1, 0]: 0, [0, 1]: 1]
        # ? どういうこと？
        # -> [1 ... numCourses] において、 courses[n] (そのコース番号における前提条件) が存在してない
        # -> 前提条件が存在しないコースを抽出している
        # e.g. 0, 1どちらもcoursesにあるので、全部コース持ってる -> noPreCourses: []
        noPreCourses = [n for n in range(numCourses) if not courses[n]]
        count = 0
        # 前提条件を持ってないコースたちを走査
        while noPreCourses:
            # queueを取り出す
            noPre = noPreCourses.pop()
            # ? countって何？
            count += 1
            for course in pres[noPre]:
                courses[course].remove(noPre)
                if not courses[course]:
                    # ? 何をしている？
                    noPreCourses.append(course)
        # e.g. 0 == 2 -> false
        return count == numCourses
