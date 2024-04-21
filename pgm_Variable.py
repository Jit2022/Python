import sys
import datetime
#-------------------------------Import Section Ends------------------------------#
var_date=datetime.datetime.now()
print ("Hello Subhojit - Today's Date is ",var_date.strftime("%c"),"\nMy version is",sys.version);
name=input("What is your Name?\n")
message="Hello {}, Which type of operation you would like to perform? Select within STR,INT,FLOAT,FORMAT\n".format(name)
var_type=input(message)
#-------------------------------Integer Float Variable Section------------------------------#
if var_type.upper()=="INT" or var_type.upper()=="FLOAT":
    var_num1=input("Please Provide your 1st number\n");
    var_num2=input("Please Provide your 2nd number\n");
    #var_operation=input("Please Provide which operation you want to perform\n");
    output_var=int(var_num1)*int(var_num2)
    print ("Your Multiplacation Value is",float(output_var))
    print("1st Input Type is",type(var_num1), "\n2nd input type is",type(var_num2))
#-------------------------------String Variable Section------------------------------#
elif var_type.upper()=="STR":
    var_str1=input("Please provide your string\n")
    var_len=len(var_str1)
    message="Please enter the position, should be within {}, of the string value you want to see\n".format(var_len)
    var_position=input(message)
    print("Your",var_position,"string value is",var_str1[int(var_position)])
elif var_type.upper()=="FORMAT":
    print("This is for formatting\n")
    var_str2=input("Enter your name:\t")
    var_str3=input("Enter your age\t")
    var_num3=input("Enter 1st number\t")
    var_num4=input("Enter 2nd number\t")
    print("You have entered\nYour name as {}\nYour age as {}\n1st Number as {}\n2nd Numer as {}".format(var_str2,var_str3,var_num3,var_num4))
    var_divi1=float(var_num3)/float(var_num4)
    print("Your division value is {di:5.4f}".format(di=var_divi1))