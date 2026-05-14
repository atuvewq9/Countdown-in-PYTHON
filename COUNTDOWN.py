import time
t=int(input("enter time:"))
for i in range(t,0,-1):
    seconds=i%60
    min=int(i/60)%60
    hours=int(i/3600)
    print(f"{hours:02}:{min:02}:{seconds:02}")
    time.sleep(1)
print("time up!")