class Solution:
    def freqAlphabets(self, s: str) -> str:

        dec_str = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                dec_str += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                dec_str += chr(int(s[i]) + 96)
                i += 1

        return dec_str