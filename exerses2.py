
# coding: utf-8

# In[3]:

n=int(input('请输入所计算数字的总个数 '))
i=1
num=int(input('please enter an integer'))
max_num=num
min_num=num
sum=num

while i<n:
    i+=1
    if max_num<num :
        max_num=num
    if min_num>num :
        min_num=num 
    num=int(input('please enter an integer'))
    sum+=num

average=sum/n
print(average)
print(max_num)
print(min_num)
        
    


# - 练习 1：写程序，可由键盘读入用户姓名例如Mr. right，让用户输入出生的月份与日期，判断用户星座，假设用户是金牛座，则输出，Mr. right，你是非常有性格的金牛座！。

# In[5]:

print('What is you name ?')
name=input()
print('please enter your birthday ex:521 meas month: 5 day:21 ')
birthday=int(input())

if 421<=birthday<=521 :
    print('Mr.',name,'，你是非常有性格的金牛座！')


# - 练习 2：写程序，可由键盘读入两个整数m与n(n不等于0)，询问用户意图，如果要求和则计算从m到n的和输出，如果要乘积则计算从m到n的积并输出，如果要求余数则计算m除以n的余数的值并输出，否则则计算m整除n的值并输出。

# In[9]:

m=int(input('please enter an integer '))
n=int(input('please enter an integer '))
print('what can i do for you?(please choose from : 1.sum,2.product,3.mod,4.qita输入选择的数字 )')
test=int(input())

if test==1 :
    print(m+n)
elif test==2 :
    print(m*n)
elif test==3 :
    print(m%n)
else :
    print(n/m)
    



# - 练习 3：写程序，能够根据北京雾霾PM2.5数值给出对应的防护建议。如当PM2.5数值大于500，则应该打开空气净化器，戴防雾霾口罩等。

# In[11]:

n=int(input('please enter the PM2.5 point'))
if n>500 :
    print('建议打开空气净化器，戴防雾霾口罩等')
        

