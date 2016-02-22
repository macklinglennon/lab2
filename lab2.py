#lab2 by Mac Glennon

#ask the user for an algebraic expression

s = str(input("Input an algebraic expression: "))

#find the operator

sgn = s.find('+')
if(sgn == -1):
    sgn = s.find('-')
if(sgn == -1):
    sgn = s.find('*')
if(sgn == -1):
    sgn = s.find('/')

#get numeric values of integers entered

firstInt = int(s[:sgn])
operator = str(s[sgn])
secondInt = int(s[sgn+1:])

#designate operation for each possible operator

theSum = firstInt + secondInt
theQuo = firstInt / secondInt
theProd = firstInt * secondInt
theDif = firstInt - secondInt

#calculate

if operator == "+":
    print(str(firstInt) + " + " +  str(secondInt) + " = " +
      str(theSum))
if operator == "-":
    print(str(firstInt) + " - " + str(secondInt) + "=" + str(theDif))
if operator == "*":
    print(str(firstInt) + " * " + str(secondInt) + "=" + str(theProd))
if operator == "/":
    print(str(firstInt) + " / " + str(secondInt) + "=" + str(theProd))


##num1=int(input("enter your first number:"))
##func=input("function- *,/,+,- :")
##num2=int(input("enter your second number:"))
##
##if func=="+":
##    ans=num1+num2
##    print(ans)
##else:
##    pass
##
##if func=="-":
##    ans=num1-num2
##    print(ans)
##else:
##    pass
##
##if func=="*":
##    ans=num1*num2
##    print(ans)
##else:
##    pass
##
##if func=="/":
##    ans=num1/num2
    #print(ans)
