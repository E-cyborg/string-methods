#python provides a set of built in methods that we can use to alter and modify the strings
#string are immutable
#these method will not change the data in the variable 


#upper method
name="kinshuk"
print(name.upper())

#lower method
string="KINSHUK"
print(string.lower())

#rstrip method
#this method remove any trailing character.
#this will not strip the starting characters
string1="1111kinshuk11111"
print(string1.rstrip("1"))


#replace method
#replace all occurences of a string with the given character string.
sr="hello my name is kinshuk learning python"
print(sr.replace("n","ia"))


#split method
strin="hello world"
print(strin.split(" "))

#capitalize method
#turn only the first character into upper case and the rest into lower case
st="itro i am kinshuk Learning python"
print(st.capitalize())


#center method
#aligns the string to the center as per the parameter given by the user.
# print(len(ste1))
ste1="hello kinshuk"
print(ste1.center(200))

#count method
#returns a number of times given value occurred in string
sy="ababababababbcbcbschaakvddvsc"
print(sy.count("ab"))


#endswith method
#check if the string ends with a given value.returns TRUE and FALSE
#can also check for a value in-b/w the strings by providing strating and ending index position
str1="welcome to my console !!"
print(str1.endswith("!"))
print(str1.endswith("come",3,7))


#find method
#searches for the first occurence of the given vale and return index number.
#find and index are same method but if the vale is not in the string index raises a ValueError for lists.
srt1="hello i am kinshuk in diploma ftd ce student"
print(srt1.find("i am "))
print(srt1.index("i"))


#isalnum method 
#returns true only if the entire string only consists of A-Z,a-z,0-9. 
str2="helloworld123"
print(str2.isalnum())

#isalpha method
#returns true if only the entire string only consists of A-Z,a-z.
str2="helloworld"
print(str2.isalpha())


#islower method
#check if the entire string is in lower case
# same with the is upper 
#return TRUE and false
print(str2.islower())
print(str2.isupper())

#isprintable
#returns true if all the values within the given string is printable 
#non printable values are {\n,\t}
st1="wrhaha ahad ssjdsjf ajwsey "
print(st1.isprintable())

#isspace
#return true only and only if the string contains white spaces.
sw="    "
print(sw.isspace()) 


#istitle method
#RETURNS TRUE ONLY IF THE FIRST LETTER OF THE STRING IS CAPITALIZED ,else return false.
dj="Ejsbf Uhhfb Jehhfb"
print(dj.istitle())


#islower method
#RETURNS TRUE ONLY IF THE ALL THE  LETTER OF THE STRING IS UPPER CASE ,else return false.
#
iw=" R R E W W R T RERG"
print(iw.isupper())


#startswith method
#this same as endswith but it checks the starting point of theb string 
op="whefrff fjjhberj fkhhrg "
print(op.startswith("whefrff"))


#swapcase method
#changes the character casing of the string .upper to lower and lower to upper
str1="hvf wsejfvwf af errgthy ikky rfqw "
print(str1.swapcase())


#title methode
#capitalizes each letter of the word within the string
str1="evf erg grgf bb betb b"
print(str1.title())


print()
