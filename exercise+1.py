
# coding: utf-8

# In[4]:

m=int(input('please enter an integer'))
n=int(input('please enter an integer'))
if m>n :
    print(m,'>',n)
elif m<n:
    print(m,'<',n)
else : 
    print(m,'=',n)


# In[6]:

max_num=int(input('please enter a number'))
i=1

while i<=10 :
    i+=1
    num=int(input('please enter a number'))
    if num>max_num :
        max_num=num

print(max_num)


# In[8]:

print('多个参数',5,56987%15,450.32,63//32)
print('多个参数',5,56987%15,450.32,63//32,sep='  ')
print('多个参数',5,56987%15,450.32,63//32,sep=' ,')
print('多个参数',5,56987%15,450.32,63//32,sep=',')


# In[9]:

print(45>78)
print(78>int(input('please enter a num')))


# In[10]:

x=407.8 
y=4078 
if 0<x<1000: 
    print('here 1.') 
if -5<0<x<y<x*y: 
    print('here 2.') 
print(x==407.8<y==40*78<=10000)


# In[ ]:



