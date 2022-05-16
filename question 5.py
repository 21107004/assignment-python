Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#question 5 Assignment 3

h= int(input("Enter no. of hydrogen atoms: "))
c = int(input("Enter the no. of carbon atoms: "))
o= int(input("Enter the no. of oxygen atoms: "))

wt_h = h*1.00794
wt_c = c*12.0107
wt_o = o*15.9994

print(wt_h + wt_c + wt_o)