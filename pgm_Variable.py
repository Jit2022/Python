import sys
import datetime
#-------------------------------Integer Float Variable Section------------------------------#
print ("Hello Subhojit - Today's Date is ",datetime.datetime.now());
var_num1=input("Please Provide your 1st number\n");
var_num2=input("Please Provide your 2nd number\n");
#var_operation=input("Please Provide which operation you want to perform\n");
output_var=int(var_num1)*int(var_num2)
print (float(output_var))
print("1st Input Type is",type(var_num1), "\n2nd input type is",type(var_num2))
#-------------------------------String Variable Section------------------------------#
var_str1=input("Please provide your string\n")
var_position=input("Please enter the position of the string value you want to see\n")
print("Your",var_position,"string value is",var_str1[int(var_position)])