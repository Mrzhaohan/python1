'''现在有一个列表，li = [1,2,3,'a','b','4','c'],有一典（此字典是
动态生成的，并不知道里面有多少键值对，所以用 dic = {} 模拟此字典 ）；
现在需要完成这样的操作：如果字典没有‘k1’这个键，那么就创建这个‘k1’这个键和
对应的值（该键值设为空列表），并将列表li中的索引位为奇数对应的元素，添加到‘k1’
这个键对应的值中'''
#li = [1, 2, 3, 'a', 'b', '4', 'c']
#dic = {}
#hc=[]
#for i in range(len(li)):
#    if i%2!=0:
#        b=li[i]
#        hc.append(b)
#dic['k1']=hc
#print(dic)
'''组合嵌套题，有如下列表，按照要求实现每一个功能
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
<1> 将列表lis中的‘tt’变成大写（两种方式）
<2> 将列表lis中数字3变成字符串‘100’（两种方式）
<3>将列表中‘1’变成数字101（两种方式）'''
#<1>(1)
#lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
#b=lis[0]
#c=b[1]
#d=c[2]
#e=d['k1']
#f=e[0]
#f=f.upper()
#print(f)
#<1>(2)
#lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
#a='{}'.format(lis)
#b=a.split('\'')
#n=0
#for i in b:
#    n+=1
#    if i=='tt':
#        b[n-1]=i.upper()
#print(b)
'''请删除字典中的键'k5',如果不存在键'k5',则输出"对不起！不存在你要删除的元素"'''
#c='y'
#z={}
#while c == 'y':
#    a=input('请输入键：')
#    b=input('请输入值：')
#    c=input('是否继续？y继续')
#    z[a]=b
#    flag=False
#print(z)
#d='{}'.format(z)
#e=d.split('\'')
#for i in e:
#    if i =='k5':
#        z.pop('k5')
#        print(z)
#        break
#else:
#    print("对不起！不存在你要删除的元素")
'''统计文本文件“KMSWHS.txt”中所有单词出现的频率，将排在前十位的单词以漂亮的形式打印出来。'''
a=open('./KMSWHS.txt','r')
b={}
while True:
    c=a.readline()
    d=c.split(' ')
    for i in d:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    if c=='':
        break
a.close()
h={}
flag=True
for f in range(10):
    for e in b.keys():
        if flag:
            max_number=b[e]
            max_key=e
            flag=False
            continue
        else:
            if b[e] > max_number:
                max_number=b[e]
                max_key=e
    h[max_key]=max_number
    print(b)
    b.pop(max_key)
print(h)
'''给定一个字典的键，可以找到对应的值，但是，反过来根据值去找键却不行，而且还有可能有多个键映射到一个值上。现在，实现一个函数，根据给定的值返回对应的键，如果有多个就返回一个列表。'''
#z={}
#e=[]
#hc={}
#x=''
#c='y'
#while c == 'y':
#    a=input('请输入键：')
#    b=input('请输入值：')
#    z[a]=b
#    c=input('是否继续？y继续')
#for i,v in z.items():
#    print(i,v)
#    e.append(i)
#    e.append(v)
#print(e)
#for k in range(len(e)):
#    if k%2!=0:
#        x=e[k-1]
#        for f in range(k+2,len(e)):
#            if e[k]==e[f]:
#                x=x+','+e[f-1]
#                hc[k]=x
#print(hc)
