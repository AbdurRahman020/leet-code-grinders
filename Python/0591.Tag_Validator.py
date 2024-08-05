class Solution:
    def isValid(self, code: str) -> bool:
        # check if the code starts and ends with '<' and '>'
        if code[0] != '<' or code[-1] != '>':
            return False
        
        # variables to track whether code contains a tag and the stack for tag validation
        contains_Tag, tag_Stack = False, []  
        
        # function to check if a string represents a valid CDATA section
        def isValid_CDATA(s: str) -> bool:
            # check if the string starts with the CDATA section marker '[CDATA['
            return s.find('[CDATA[') == 0
        
        # function to check if a tag name is valid and matches with its corresponding end tag
        def isValid_TagName(tag_Name: str, isEndTag: bool) -> bool:
            nonlocal contains_Tag
            # check if the tag name is empty or too long
            if not tag_Name or len(tag_Name) > 9:
                return False
            
            # check if all characters in the tag name are uppercase
            if any(not ch.isupper() for ch in tag_Name):
                return False
            
            # if the tag isn't end tag, validate it against the last opened tag in the stack
            if isEndTag:
                # check if there's an open tag in the stack
                return tag_Stack and tag_Stack.pop() == tag_Name
            
            # for start tag, mark that code contains a tag, push it to the stack
            contains_Tag = True
            tag_Stack.append(tag_Name)
            return True
        
        # iterate through the characters of the code
        i = 0
        while i < len(code):
            # if there's no open tag in the stack, but code contains a tag, it's invalid
            if not tag_Stack and contains_Tag:
                return False
            
            # check the current character
            if code[i] == '<':
                # check if it's a CDATA section
                if tag_Stack and code[i+1] == '!':
                    # find the closing marker for the CDATA section
                    close_Index = code.find(']]>', i+2)
                    
                    # if CDATA section is invalid, return False
                    if close_Index == -1 or not isValid_CDATA(code[i+2:close_Index]):
                        return False
                # check if it's an end tag
                elif code[i+1] == '/':
                    # find the closing angle bracket of the end tag
                    close_Index = code.find('>', i+2)
                    # if end tag is invalid or doesn't match with last open tag, return False
                    if close_Index == -1 or not isValid_TagName(code[i+2:close_Index], True):
                        return False
                 # otherwise, it's a start tag
                else:
                    # find the closing angle bracket of the start tag
                    close_Index = code.find('>', i+1)
                    # if start tag is invalid, return False
                    if close_Index == -1 or not isValid_TagName(code[i+1:close_Index], False):
                        return False
                
                # move the pointer to after the current tag
                i = close_Index
            
            # move to the next character
            i += 1
        
        # after parsing all tags, if there are still open tags or no tags were found, it's invalid    
        return not tag_Stack and contains_Tag

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))
    print(s.isValid("<DIV>>> ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))
    print(s.isValid("<A> <B> </A> </B>"))