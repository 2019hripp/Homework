#Name- 180424T.Queue_Class_Program.py

#First in First out
class Queue():
	#init
	def __init__(self): #begin initialization method
		self.items = [] #create array for items

	#enqueue
	def enqueue(self, item): #begin enqueue method
		self.items.append(0,item) #define enqueue

	#dequeue
	def dequeue(self): #begin dequeue method
		self.items.pop(0) #define dequeue

	#show all
	def list(self): #begin list method
		for x in self.items: #initialize for loop
			print(x) #print x


q = Queue() #q is an instance of class q
q.enqueue ('aaahhahhhah') #q is of type queue
q.enqueue ('internal screaming')
print (q.items_list()) #print items
print (q.dequeue()) #print dequeue
