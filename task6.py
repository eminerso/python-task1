
# import shutil

# #src =r"C:\Users\Raul\Desktop\python\example\next\1.jpg"
# src =r"C:\Users\Raul\Desktop\python\example\next\text.jpg"


# direct=r"C:\Users\Raul\Desktop\python\example"
 
# try:
#     shutil.move(src,direct)
# except:
    print("error")

xallar=[5,44,3,2,1]

for x in range(1,6):
   print(f"{max(xallar)} xalla tutdugu yer {x}-ci yer")
   xallar.remove(max(xallar))

