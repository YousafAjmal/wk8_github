#!/usr/bin/env python
# coding: utf-8

# ## Challenge: Voucher Problem

# In[ ]:





# A local shop is having a promotion! If you spend over £10 you will get a £1 voucher to spend next time you come in the store. If you spend over £20 you get a £3 voucher.
# 
# Write a programme to tell the sales assistant which voucher to give the customer.
# 
# This challenge includes:
# User input
# Output
# IF statements

# In[8]:


# Code for the voucher task
spend = float(input('Enter amount customer has spent: '))
if spend > 20:
    print('Customer gets a £3 voucher')
elif spend > 10:
    print('Customer gets a £1 voucher')
elif spend >= 0:
    print('Customer gets no voucher')
else:
    print('Invalid number entered')


# ## Challenge: Rock, Paper, Scissors 

# Develop and write the "Rock, "Paper","Scissors" game.
# Get the computer to ask for the player’s name.
# The game rules are simple: rock beats scissors, scissors beat paper, paper beats rock. Two of the same gives a draw.  
# An idea to get you started
# 
# import random
# selection=random.choice(["Rock","Paper","Scissors"])
# print(selection) - try this first to help.
# 
# Use comments in the code so it is clear about what is going on.
# 
# This challenge includes:
# 
# Use of random library
# Input/Output
# IF statement
# 
# Extension: 
# Use a loop to play 3 rounds.

# In[21]:


#code for the game
import random 
selection=random.choice(["Rock","Paper","Scissors"]).lower()
print(selection)

name = input('Enter your name: ')
choice = input('Enter rock, paper or scissors: ').lower()

if choice == selection:
    print('Game is a draw')

elif choice == 'rock' and selection == 'scissors':
    print(f'{name} wins')

elif choice == 'scissors' and selection == 'paper':
    print(f'{name} wins')

elif choice == 'paper' and selection == 'rock':
    print(f'{name} wins')

elif selection == 'rock' and choice == 'scissors':
    print('computer wins')

elif choice == 'scissors' and selection == 'paper':
    print('computer wins')

elif choice == 'paper' and selection == 'rock':
    print('computer wins')

else:
    print('invalid input')


# ## Challenge: Displaying the lowest number using a function

# Write a function that asks the user to enter two numbers and then outputs which number is the smallest of the two with a suitable message.
# To achieve this you will need to use a function which will compare the two numbers.
# Outside the function will be the two inputs which will allow the user to enter the numbers.
# 
# This will start you off.
# 
# def lowest_number(num1, num2):
#     insert code her to compare numbers
#     insert print statement to output the smaller number.
#     
# number1 = Write a suitable input statement here
# number2  = Write a suitable input statement here
# 
# 
# lowest_number(number1, number2)
# 
# 
# 

# In[17]:


#code for the function problem
def lowest_number(num1, num2): 
    if num1 > num2:
        print('Second number is smaller')
    if num1 < num2:
        print('First number is smaller')
    if num1 == num2:
        print('Both numbers same')

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

lowest_number(number1, number2)


# ## Challenge: Counting using Subprograms

# Write a function that asks the user to enter a number between 1 - 100 and saves the number as the variable, num1.
# Write a second function which counts up to that number ( whatever it may be.)
# To help, here is the structure of the program.
# 
# def usernum():
#   num = enter a suitable input statement here
#   return num
# 
# def count(num)
# 
# 
# def main():
#   usernum()
#   count(num)
#   
# main()
# 
# This is the way you can structure this program, the main function is called at the end of the program and will go the usernum function first before moving to the count function.
# 
# 
# 

# #### Challenge: Find the word using a linear search

# In[25]:


#Code for the counting program
def usernum(): 
    num = int(input('Enter a number between 1 and 100: '))
    return(num)

def count(num):
    tot=0
    for i in range(num+1):
        tot+=i
    return(tot)
def main(): 
    n=usernum() 
    m=count(n)
    return(m)

main()


#def usernum(): 
#    global num
#    num = input('Enter a number between 1 and 100: ')
#usernum()
#print(num)
#
#def count():
#    for i in range(1,int(num)+1,1):
#        print(i)
#def main(): 
#    usernum() 
#    count()
#
#main()


# #### A linear eearch is a search algorithm that goes through a list and checks to see if the item in the list is equal to the target, i.e the thing that you are looking for.
# e.g. Beatles = ["John","Paul","George","Ringo"]
# 
# searching for "George"
# Is John == George:
#  no, move on
# Is Paul == George:
#  no, move on 
# Is George == George:
#  yes, target found.
#  
# Write a program that asks a user for a name, then iterates through a list to find the item and states what position in the list that the word could be found.
# 
# wordList = ["Giraffe","Lion","Elephant","Zebra","Hyena","Crocodile","Rhinoceros","Hippopotamus","Flamingo","Chimpanzee"]
# 
# 
#  Use the internet to help if needed before asking your PDE.
#  

# In[ ]:


#code for the search


# In[29]:


wordList = ["Giraffe","Lion","Elephant","Zebra","Hyena","Crocodile","Rhinoceros","Hippopotamus","Flamingo","Chimpanzee"]
name = input('Search for animal: ')
def linearsearch(name):
    if name in wordList:
        return wordList.index(name)
    else:
        print('Animal not found in list')

print(f'{linearsearch(name)} is the index number')


# In[17]:





# In[ ]:




