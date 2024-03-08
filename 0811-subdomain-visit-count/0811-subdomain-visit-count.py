class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        look_up = {}
        
        for cpdomain in cpdomains:
            n, domains = cpdomain.split()
            n, domains = int(n), domains.split('.')

            # print(n, domains)

            for i in range(len(domains)):
                domain = '.'.join(domains[i:])
                
                if domain in look_up:
                    look_up[domain] = look_up[domain] + n
                else: 
                    look_up[domain] = n
        
        # print(look_up)

        result = [str(look_up[domain]) + ' ' + domain for domain in look_up]

        return result
                
             

        