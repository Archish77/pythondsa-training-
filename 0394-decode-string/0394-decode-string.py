class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []    
        str_stack = []   
        cur_str = ""      
        cur_num = 0       

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)  

            elif c == '[':
                num_stack.append(cur_num)   
                str_stack.append(cur_str)   
                cur_num = 0                
                cur_str = ""               

            elif c == ']':
                k = num_stack.pop()         
                prev = str_stack.pop()      
                cur_str = prev + cur_str * k  

            else:
                cur_str += c              
        return cur_str
