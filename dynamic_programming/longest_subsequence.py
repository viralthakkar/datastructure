class LongestCommon:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.m = len(self.str1)
        self.n = len(self.str2)
        self.dp = []
        self.current = []
        self.previous = []
    
    def initialization(self):
        self.dp = [[0 for _ in range(self.n+1)] for _ in range(self.m+1)]

        # Space Utilization Approach
        self.current = [0 for _ in range(self.n+1)]
        self.previous = [0 for _ in range(self.n+1)]
    
    def get_length_substring(self) -> int:
        self.initialization()

        max_length = 0

        for i in range(1, self.m + 1):
            self.current = [0 for _ in range(self.n+1)]
            for j in range(1, self.n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.current[j] = self.previous[j - 1] + 1
                    max_length = max(max_length, self.current[j])
                else:
                    self.current[j] = 0

            self.previous = self.current

        return max_length

    def get_length_subsequence(self):
        self.initialization()

        for i in range(1, self.m + 1):
            self.current = [0 for _ in range(self.n + 1)]
            for j in range(1, self.n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.current[j] = self.previous[j - 1] + 1
                else:
                    self.current[j] = max(self.current[j - 1], self.previous[j])

            self.previous = self.current

        return self.current[-1]

    def edit_distance(self):
        self.initialization()

        for i in range(1, self.n + 1):
            self.dp[0][i] = i

        for i in range(1, self.m + 1):
            self.dp[i][0] = i

            for j in range(1, self.n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.dp[i][j] = self.dp[i - 1][j - 1]
                else:
                    self.dp[i][j] = min(self.dp[i][j - 1], self.dp[i - 1][j - 1], self.dp[i-1][j]) + 1

        return self.dp[self.m][self.n]


if __name__ == '__main__':
    s1 = ["educative", "bcdcdcd", "arefun", "yourocks", "abc", "abcde"]
    s2 = ["education", "aacdcdcd", "isfun", "youawesome", "def", "ace"]

    for i in range(len(s1)):
        lc = LongestCommon(s1[i], s2[i])
        print(f"{s1[i]} - {s2[i]} Substring Length - {lc.get_length_substring()}")

        print("Second Problem")

        lc = LongestCommon(s1[i], s2[i])
        print(f"{s1[i]} - {s2[i]} SubSequence Length - {lc.get_length_subsequence()}")

    print("Edit Distance")

    s1 = ["horse", "sam", "intention"]
    s2 = ["ros", "sum", "execution"]

    for i in range(len(s1)):
        lc = LongestCommon(s1[i], s2[i])
        print(f"{s1[i]} - {s2[i]} Edit Distance is - {lc.edit_distance()}")
