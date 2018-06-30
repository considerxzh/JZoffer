# 题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 输入描述:
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
def Permutation(ss):
    if not ss:
        return None
    if len(ss)==1:
        return ss
    strore = []
    #遍历字符串，固定第一个元素，然后递归求解
    for i in range(len(ss)):
        for j in Permutation(ss[:i]+ss[i+1:]):
            strore.append(ss[i]+j)
    #set去重 sort排序
    return sorted(list(set(strore)))

if __name__=='__main__':
    ss = 'abcd'
    ss1 = Permutation(ss)
    print(ss1)