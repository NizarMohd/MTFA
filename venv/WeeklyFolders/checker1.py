import week1
import solution
# change based on input
file = open("scratch.txt", "r")
lines = file.readlines()
i = 0
marks = 0
for line in lines:
    x, y = line.strip().split(" ")
    Sum = week1.Questions()
    Sum2 = solution.Solution()
    sum1 = Sum.sum(x=int(x),y=int(y))
    sum2 = Sum2.sum(int(x),int(y))
    if sum1 == sum2:
        print("Test" + str(i) + ": " + "passed!")
        marks = marks + 1
    else:
        print("Test" + str(i) + ": " + "failed :(")
    i = i + 1
print("Score: " + str(marks*100/i) + "%")