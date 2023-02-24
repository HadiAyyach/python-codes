from typing import List
def numToEng(n: int) -> str:
    numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
    tenth_words = ['','','twenty', 'thirty', 'forty','fifty','sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    n = str(n)
    length = len(n)
    result = ''
    if length == 1:
        return words[int(n)]
    if length == 2 :
        if n[0] == '1':
            result += teens[int(n[1])]
        else:
            if n[1] == '0':
                result += tenth_words[int(n[0])]
            else :
                result += tenth_words[int(n[0])]+ ' ' + words[int(n[1])]
    if length == 3 :
        if n[1] == '0' :
            result += words[int(n[0])] + ' hundred' + ' ' + words[int(n[2])]
        else :
            if n[2] == '0':
                result += words[int(n[0])] + ' hundred ' + tenth_words[int(n[1])]
            else:
                result += words[int(n[0])] + ' hundred ' + tenth_words[int(n[1])] + '-' + words[int(n[2])]
    return result

q = [703,999,460,20,19,777]
a = ['seven hundred three'
,'nine hundred ninety-nine'
,'four hundred sixty'
,'twenty','nineteen','seven hundred seventy-seven'
]
for i, v in enumerate(q) :
    print(numToEng(v)==a[i])
    #print(numToEng(v))
        
        