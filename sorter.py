"""
Program to sort contestents according to score 
Input : Provide receipt number , Name , Score 

"""

import heapq

def accept():
	reciept = input("\nReciept no: ")
	name = input("\nName: ")
	score = input("\nScore: ")
	return reciept , name , score
	
	
def sort_list(data_list):
	sorted_list = heapq.nlargest(len(data_list) , data_list , key = lambda s : s['score']) 
	rank = 0
	print("Rank \t\t Team description \n")
	for i in sorted_list :
		rank += 1
		print(rank,"\t\t",i,"\n")
		

def main():
	portfolio = []
	
	total = int(input("\nTotal number of entries : "))
	for i in range(0,total):
		data_dict = {}
		#portfolio.append(accept())
		return_tuple = accept()
		data_dict['reciept'] = return_tuple[0]
		data_dict['name'] = return_tuple[1]
		data_dict['score'] = return_tuple[2]
		portfolio.append(data_dict)

	#print("Final Data",portfolio)
	sort_list(portfolio)
	

if __name__ == '__main__':
	main()

