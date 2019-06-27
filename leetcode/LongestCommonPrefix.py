class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        if len(strs) == 0:
            return output
        elif len(strs) == 1:
            return strs[0]
        size = 0
        if len(strs[0]) < len(strs[1]):
            wordLen = strs[0]
        else:
            wordLen = strs[1]
        for i in range(len(wordLen)):
            if strs[0][i] == strs[1][i]:
                output+=str(strs[0][i])
            else:
                break
        #print(output)
        if len(strs) > 2:
            for i in range(2,len(strs)):
                size = 0
                #print(strs[i])
                if strs[i] != "":  
                    if len(strs[i]) <= len(output):
                        wordLen = strs[i]
                        #print(wordLen)
                    else:
                        wordLen = output
                        #print("first else is " ,wordLen)
                    print(output)
                    for j in range(len(wordLen)):
                        if len(wordLen) == 1:
                            #print(wordLen[0])
                            #print(output[0])
                            #print("j is i wordLen == 1 ",wordLen[j])
                            print(strs[i][0])
                            if output[0] == strs[i][0]:
                                output = wordLen[0]
                            else:
                                output =""
                            ##add more shit here
                        elif output[j] == strs[i][j]:
                            size+=1
                        else:
                            output=output[0:size]
                            size=0
                            break
                else:
                    output=""
        return output