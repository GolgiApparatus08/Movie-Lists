from Functions import assignRanks, inputFilm, orderList
import sys
import openpyxl

myRankingList = []
inputFilm(myRankingList)    #Gets new entry from user
orderList(myRankingList)    #Asks for comparisons and reorders list accordingly
assignRanks(myRankingList)  #Reranks all entries
