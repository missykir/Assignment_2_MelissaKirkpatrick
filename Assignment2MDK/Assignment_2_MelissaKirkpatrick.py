
#import statements
import random
from functools import reduce

#helper functions
def isSorted(list):
	#this is a helper function to determine if a list is sorted.
	for index in range(len(list)):
		if index >= 1:
			assert(list[index] >= list[index-1])
def genList(numElements):
	#this is a helper function to create a list of random numbers.
	x = random.Random()
	y = 0
	for i in range(numElements): 
		y = x.randint(1,100)
		yield y

#bubble sort - 50% #1
def bubbleSort(L):
	#this a function to bubble sort the list.
	for passnum in range(len(L)-1,0,-1):
		for index in range(passnum):
			if L[index] > L[index+1]:
				temp = L[index]
				L[index] = L[index+1]
				L[index+1] = temp
#bubble sort a predetermined list
alist = [3,1,8,23,51,2,8]
print("list to be bubble sorted: ", alist)
bubbleSort(alist)
isSorted(alist)
assert(alist == [1,2,3,8,8,23,51])
print("the bubble sorted list: ", alist)
print("")
#bubble sort  a random list
alist2 = list(genList(5))
print("the second list to be bubble sorted:  ", alist2)
bubbleSort(alist2)
print("the bubble sorted list: ",alist2)
isSorted(alist2)
print("")

#any,all,count 60% #1
def any(list, gauntlet):
	#this function sees if any of the items in the list match the condition.
	anyisTrue = False
	for item in list:
		if gauntlet(item):
			anyisTrue = True
	if anyisTrue:
		return True
	else:
		return False
def all(list,gauntlet):
	#this function checks if all of the items in the list satisfy the condition
	isTrue = False
	for item in list:
		if gauntlet(item):
			isTrue = True
		else:
			isTrue = False
	if isTrue:
		return True
	else:
		return False
def count(list, gauntlet):
	#this function counts all the items in the list that satisfy the condition
	count = 0
	for item in list:
		if gauntlet(item):
			count = count + 1
	return count

blist = [2,5,7,6]
assert(any(blist, lambda e: e > 3)==True)
assert(all(blist, lambda e: e < 2) == False)
assert(count(blist, lambda e: e > 0) == 4)	


#generating an ordered random list %60 #2 
def genOrderedList(numElements):
	#this creates a list of sorted random numbers
	x = random.Random()
	y = 0
	for index in range(numElements): 
		y = y + x.randint(1,9)
		yield y
		

genList1 = list(genOrderedList(7))
isSorted(genList1)
print("a randomly generated sorted list: ",genList1)
genList2 = list(genOrderedList(1))
print("a second randomly generated sorted list: ",genList2)
isSorted(genList2)
genList3 = list(genOrderedList(30))
print("a third randomly generated sorted list: ", genList3)
isSorted(genList3)
print("")


#binary search 80% #1
def binarySearch(List,x,y, searchTerm):
	#this does a binary search on the given list
	newList = List.copy()
	a = 0
	i = newList[int(len(newList)/2)]
	list1 = newList[0:x]
	list2 = newList[x:y]
	if searchTerm > i or searchTerm < i:
		if searchTerm < i:
			newList = list1			
		elif searchTerm > i:
			newList = list2

		x = int(len(newList)/2)
		y = len(newList)
		a +=1
		if a < len(List):
			return(binarySearch(newList, x,y, searchTerm))
		else:
			return None
	else:
		return i

#binary search predetermined list
testList1 = [1,2,3,4,5,6,7,8,9,10,11]
a = binarySearch(testList1,int(len(testList1)/2),len(testList1),8)
assert(a == 8)
assert(binarySearch(testList1,int(len(testList1)/2),len(testList1),4) == 4)
	#binary search randomized list
testList2 = list(genOrderedList(7))
b = binarySearch(testList2,int(len(testList2)/2),len(testList2), 4)
assert(b == 4 or b == None)
assert(binarySearch(testList2,int(len(testList2)/2), len(testList2), 17) == 17 or binarySearch(testList2,int(len(testList2)/2), len(testList2), 17) == None)


#where,select 80% #2

def where(list, predicate):
	#this function returns a new list containing the items from the original list that satisfied the condition 
	pointer = 0
	#this size was chosen because the new list size will always be the same size as the original or smaller.
	newList = [0]*(count(list, predicate))
	for item in list:
		if predicate(item):			
			newList[pointer] = item			
			pointer +=1
	return newList
def select(list,predicate):
	#this function changes each item in a list using the transformation given in the predicate
	pointer = 0
	newlist = list
	for item in list:	
		transform = predicate(item)
		newlist[pointer] = transform
		pointer+= 1
	return newlist

clist = [1,6,2,71,2]
assert(where(clist, lambda e: 2< e < 10)==[6])
assert(select(clist, lambda e: 2*e)==[2, 12, 4, 142, 4])


#linked list vs list 80% #3
print("Linked List: Inserting and deleting is really easy, just add and delete links")
print("rather than moving values over(iterating), hard to iterate. Not contiguous.")
print("")
print("List: Uses less RAM than a Linked List (unless you have a lot of empty space at the end), easier to iterate over(is faster to find things), and is contiguous.")
print("")


#merge sort 90% #1
def mergeSort(alist):
	#this function is a recursive algorithm to sort a list by splitting and merging.
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	return alist
testList3 = list(genList(7))
print("the list to be merge sorted: ", testList3)
mergedList = mergeSort(testList3)
isSorted(testList3)
print("the merged sorted list: ",mergedList)
print("")

#all asserts prior to this comment are for 100% #1

#map filter reduce 100% #2
maplist = [1,4,2,5,3,6]
assert(list(map(lambda e: e*2, maplist)) == [2,8,4,10,6,12])
print("map works like select. It effects a transformation on each element on the list")
print("")

filterlist = [3,1,6,2,7]
assert(list(filter(lambda e: e<6,filterlist)) == [3,1,2])
print("filter works like where. it returns a list containing only the elements of the")
print("original list that satisfy the condition.")
print("")

reducelist = [7,472,12,8, 105]
assert(reduce(lambda e,y: e+y,reducelist)==604)
print("reduce takes the first two items in a list and does what ever the function")
print("states. it takes that result and the next item in the list and repeats until")
print("the list is completed.")
print("")
