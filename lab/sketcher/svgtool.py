from svgpathtools import svg2paths, parse_path
paths, attributes = svg2paths('my.svg')


allPaths ="" 

for i in attributes:
    allPaths += i["d"]
    allPaths += " "

with open("test.txt", "w") as f:
    f.write(allPaths)

n = 5000
pp = parse_path(allPaths)
l = pp.length()

p = (10/5000)*l

for i in range(int(l)):
    print(i)
    if pp.point(int(i)) is not None:
        print(pp.point(int(i)))
        input()

# for k, v in enumerate(attributes):
#     print(v['d'])  # print d-string of k-th path in SVG