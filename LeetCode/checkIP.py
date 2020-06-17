class Solution:
    def validIPAddress(self, IP: str) -> str:
        iplist = IP.split(".")
        if len(iplist) == 4: 
            for ipX in iplist:
                if len(ipX) == 0 or (len(ipX) > 1 and ipX[0] == "0"): 
                    return "Neither"
                if ipX.isnumeric()==False or int(ipX) > 255: 
                    return "Neither"                
            return "IPv4"
        
        iplist = IP.split(":")
        if len(iplist) == 8:
            symbols = "0123456789abcdefABCDEF"
            for ipX in iplist:
                if len(ipX) == 0 or len(ipX) > 4: 
                    return "Neither"
                for elem in ipX:
                    if elem not in symbols: 
                        return "Neither"                 
            return "IPv6"      
        return "Neither"

sln = Solution()
print(sln.validIPAddress("256.256.256.256"))
print(sln.validIPAddress("255.0.1.2"))
print(sln.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
