lt=['welcome','to','the','world','of','python']
length=len(lt)
count=0
for i in lt:
    lt[count]=(i[::-1])
    count+=1
print(lt)