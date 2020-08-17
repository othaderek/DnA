class Solution:
    def defangIPaddr(self, address):
        # turn address into list
        ip_list = list(address)
        
        for i,char in enumerate(ip_list):
            if char == ".":
                ip_list[i] = "[.]"
                
        ip_list = "".join(ip_list)
        return ip_list

s1 = Solution()

print(s1.defangIPaddr("1.1.1.1"))
