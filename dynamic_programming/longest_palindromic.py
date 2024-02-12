class LongestPalindromic:
    def __init__(self, str1):
        self.str1 = str1
        self.m = len(self.str1)
        self.n = self.m
        self.dp = []
        self.current = []
        self.previous = []

    def initialization(self):
        self.dp = [[0 for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            self.dp[i][i] = 1

        # Space Utilization Approach
        self.current = [0 for _ in range(self.n)]
        self.previous = [0 for _ in range(self.n)]

    def get_length_substring(self) -> int:
        self.initialization()

        for i in range(self.m-1, -1, -1):
            for j in range(i+1, self.n):
                if self.str1[i] == self.str1[j]:
                    substring_length = j - i + 1

                    if substring_length == 2 or substring_length - 2 == self.dp[i + 1][j - 1]:
                        self.dp[i][j] = substring_length
                    else:
                        self.dp[i][j] = max(self.dp[i + 1][j], self.dp[i][j - 1])
                else:
                    self.dp[i][j] = max(self.dp[i + 1][j], self.dp[i][j - 1])

        return self.dp[0][self.n - 1]

    def get_length_subsequence(self):
        self.initialization()

        for i in range(self.m-1, -1, -1):
            self.current = [0 for _ in range(self.n)]
            self.current[i] = 1

            for j in range(i+1, self.n):
                if self.str1[i] == self.str1[j]:
                    self.current[j] = self.previous[j - 1] + 2
                else:
                    self.current[j] = max(self.current[j - 1], self.previous[j])

            self.previous = self.current

        return self.current[-1]


if __name__ == '__main__':
    strings = ['abcbda', 'tworacecars', 'pqrssrqp', 'mnop', 'bbbbbbbbbbbbbbbbbbbb', 'bbbab']

    for i in range(len(strings)):
        lc = LongestPalindromic(strings[i])
        print(f"{strings[i]} Substring Length - {lc.get_length_subsequence()}")

        print("Second Problem")

        lc = LongestPalindromic(strings[i])
        print(f"{strings[i]} SubSequence Length - {lc.get_length_substring()}")
