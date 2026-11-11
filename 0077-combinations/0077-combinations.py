class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start: int, current_comb: list[int]):
            if len(current_comb) == k:
                result.append(list(current_comb))
                return
            for i in range(start,n+1):
                current_comb.append(i)
                backtrack(i+1,current_comb)
                current_comb.pop()
        backtrack(1,[])
        return result