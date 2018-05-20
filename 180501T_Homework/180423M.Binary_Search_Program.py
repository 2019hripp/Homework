#Name- 180423M.Binary_Search_Program.py

def bSearch(arr, find):

	#if the length of array is 0 or length is 1 and number is not our number,
	if (len(arr) == 0 or (len(arr) == 1 and len[0] != find)):
		return False #return false

	mid = arr[len(arr)//2] #the middle index is defined as "mid"

	if (mid == find): #if the number we want is equal to mid
		return True #return true

	if (mid > find): #if mid is greater than our number
		return (bSearch(arr[len(arr)//2:]), find) #begin method over but look at the first half of array

	if (mid < find): #if mid is less than our number
		return (bSearch(arr[len(arr)//2]), find) #begin method over but look at the second half of array





arr = [1,2,3,4,5,6,7,8,9] #stating numbers in array
print(bSearch(arr, 5)) #calling array and stating our number is 5
