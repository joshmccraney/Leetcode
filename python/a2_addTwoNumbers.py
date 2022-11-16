import reverse

class Solution(object):
	def list2num(self, l):
		strings = [str(integer) for integer in l]
		a_string = "".join(strings)
		an_integer = int(a_string)
		return an_integer

if __name__ == "__main__":
	l1 = [2,4,3]
	l2 = [5,6,4]
	ob1 = Solution()
	intNum = reverse.rev(ob1.list2num(l1)) + reverse.rev(ob1.list2num(l2))
	res = [int(x) for x in str(intNum)]
	print(res)