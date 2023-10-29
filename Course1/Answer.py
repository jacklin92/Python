x,y=4,2#動物腿數
count=35
leg=94
for i in range(0,count):
    if (i*x+(count-i)*y)==94:
        print("兔子有%d隻,雞有%d隻" %(i,count-i))
#i+(count-i)=35，i*x+(count-i)*y=94，i*4+(count-i)*2=94

