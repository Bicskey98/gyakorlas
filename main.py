szam = 8
print(szam,end="")
print(szam)

if szam == 8:
  print('A változó értéke 8')
else:
  print('A változó értéke nem nyolc!')

osztas1 = 10 % 2
osztas2 = 10 / 2

osztas3 = 10 // 2

print(type(osztas1))
print(type(osztas2))
print(type(osztas3))



if szam % 2 == 0:
  print('A változó értéke osztható 2-vel')
else:
  print('A változó értéke nem osztható kettővelwh')

szam=0
while szam <=10:
  print(szam)
  szam = szam + 1

print("__")
szam=-1
while szam <10:
  szam = szam + 1
  print(szam)
print("__sima ifes__")

szam=0
while szam <=10:
  szam = szam + 1     #szam += 2 ugyanezt csinálja
  if szam %2 ==0:
    print('A szám kettővel osztható: ',szam)
  if szam % 3==0:
    print('A szám hárommal osztható: ',szam)
  else:
    print(szam)
print("__elifes __")

szam=0
while szam <=10:
  szam = szam + 1     #szam += 2 ugyanezt csinálja
  if szam %2 ==0:
    print('A szám kettővel osztható: ',szam)
  elif szam % 3==0:
    print('A szám hárommal osztható: ',szam)
  else:
    print(szam) 






alma = "alma"
x = 6
print("a változok értéke: ",alma , x)
print(f"a változok értéke: {alma} {x+8/12}")


print("__valtozos for__")

szavak = "alma répa  dinnye körte"
for i in szavak:
  print(i , end='\n')
print("__lista for__")

taska=["füzet","könyv","tolltartó","körző"]
for kez in taska:
  if kez == "füzet":
    print("Ez egy füzet")
  elif kez != "füzet":
    print(f"Ez nem egy füzet:{kez} ")

for szam in range(0,104,4):
  print(szam)


