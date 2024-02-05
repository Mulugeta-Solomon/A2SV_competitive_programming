class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang_ip = ""
        for item in address:
            if item == ".":
                defang_ip += "[" + "." + "]"
            else:
                defang_ip += item
            
        return defang_ip


        