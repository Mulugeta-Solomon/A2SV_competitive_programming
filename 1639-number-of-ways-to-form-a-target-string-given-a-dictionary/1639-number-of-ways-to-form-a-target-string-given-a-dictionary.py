class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        word_len, target_len = len(words[0]), len(target)

        freq = [[0] * 26 for _ in range(word_len)]
        for word in words:
            for i in range(word_len):
                freq[i][ord(word[i]) - ord('a')] += 1

        dp = [[0] * (target_len + 1) for _ in range(word_len + 1)]

        for curr_word in range(word_len + 1):
            dp[curr_word][0] = 1
        
        for curr_word in range(1, word_len + 1):
            for curr_target in range(1, target_len + 1):
                dp[curr_word][curr_target] = dp[curr_word - 1][curr_target]

                curr_pos = ord(target[curr_target - 1]) - ord('a')
                dp[curr_word][curr_target] += (freq[curr_word - 1][curr_pos] * dp[curr_word - 1][curr_target - 1]) % MOD
                dp[curr_word][curr_target] %= MOD
        
        return dp[word_len][target_len]