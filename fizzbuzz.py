nums = range(1,101)

fizz = ["" for x in nums]

buzz = ["" for x in nums]

for i in range(1,len(nums)/3):
	fizz[i*3] = "fizz"
for j in range(0,len(nums)/3):
	buzz[j*3] = "buzz"

fizzbuzz=fizz+buzz