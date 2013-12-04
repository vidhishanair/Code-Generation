import re
import os
import fileinput
from collections import defaultdict
'''Templates code within <> will always be replaced at various functions,
therefore can use grouping find line numbers and do it'''
attribute_list = defaultdict(list)

def template_copy():
	input_Node = open("QNode_template.java","r")
	input_Node_write = input_Node.read()
	g = open("QNode.java","w")
	print(input_Node_write,file = g)
	g.close()
	input_Node.close()
def attr_delimitter(delimit):
	replacement = ""
	global attribute_list
	for l in attribute_list:
                 if len(attribute_list.get(l)) >= 1:
                          for i in range(len(attribute_list.get(l))):
                                 replacement += l
                                 replacement += " "
                                 replacement += attribute_list.get(l)[i]
                                 replacement += delimit
                 else:
                          replacement += l
                          replacement += " "
                          replacement += attribute_list.get(l)
                          replacement += delimit

	return replacement	
def attr_count():
	f = open("attributes.txt")
	l = f.readline()
	num = 0
	while l :
		l = l.strip()		
		val = l.split(" ")
		if (val[0] != "" and len(val)>1):		
			global attribute_list
			attribute_list[val[0]].append(val[1])
			#print(val)
			num += 1
		l = f.readline()
	f.close()
	

def attribute_builder():
	#insert tuple key as type, name of attribute as value		
	pattern = r'(<.*>)'
	m = open("QNode.java","r")
	input_Node_stream = m.read()
	inh = input_Node_stream
	matchObj = re.search(pattern,input_Node_stream)
	#print("matchObj.group() : ", matchObj.group(1))
	replacement = attr_delimitter(";\n\t")
	#print(replacement)
	to_be_replaced = str(matchObj.group(1))		
	input_Node_stream = input_Node_stream.replace(to_be_replaced,replacement)
	n = open("QNode.java","w")
	print(input_Node_stream,file = n)
	n.close()
	#replace using re.sub the tuple in attribute list location
def attr_constructor():
	pattern = r'\((.*)\)'
	#code to populate constructor header
	m = open("QNode.java","r")
	input_Node_stream = m.read()
	matchObj = re.search(pattern,input_Node_stream)
	#print("matchObj.group() : ", matchObj.group(1))
	replacement = attr_delimitter(",")
	replacement = replacement[:-1]
	input_Node_stream = input_Node_stream.replace(matchObj.group(1),replacement)
	n = open("QNode.java","w")
	print(input_Node_stream,file = n)
	m.close()
	n.close()
	constr_curly()
	
	#find pos of last line then add the intialization attrs there
def constr_curly():
	 pattern =  r'(<set>)'
	 m = open("QNode.java","r")
	 input_Node_stream = m.read()
	 matchObj = re.search(pattern,input_Node_stream)
	 #print("matchObj.group() : ", matchObj.group())
	 m.close()
	 replacement = ""
	 for l in attribute_list:
                  if len(attribute_list.get(l)) >= 1:
                             for i in range(len(attribute_list.get(l))):
                                    replacement += "this."
                                    replacement += attribute_list.get(l)[i]
                                    replacement += " = "
                                    replacement += attribute_list.get(l)[i]
                                    replacement += ";\n\t"
                  else:
                            replacement += "this."
                            replacement += attribute_list.get(l)
                            replacement += " = "
                            replacement += attribute_list.get(l)
                            replacement += ";\n\t"

	 input_Node_stream = input_Node_stream.replace(matchObj.group(1),replacement)
	 n = open("QNode.java","w")
	 print(input_Node_stream,file = n)
	 n.close()

def accept():
	"""Code to instantiate data at each node"""
	f=open("Queue_template.java","r")
	list_input=f.read();
	pattern=r'(<attributes accept>)'
	matchObj = re.search(pattern,list_input)
	#print("matchObj.group() : ", matchObj.group())
	f.close()
	replacement = ""
	for l in attribute_list:
		if len(attribute_list.get(l)) >= 1:
			for i in range(len(attribute_list.get(l))):
				replacement += "System.out.println(\"Enter the "+attribute_list.get(l)[i]+":\");\n\t"
				replacement += l+" "
				replacement += attribute_list.get(l)[i]
				if(l == "String"):
					replacement += " = in1."
				else:
					replacement += " = in."
				if(l=="int"):
					replacement+="nextInt();"
				elif(l=="String"):
					replacement+="nextLine();"
				elif(l == "double"):
					replacement += "nextDouble();"
				elif(l == "float"):
					replacement  += "nextFloat();"
				elif(l == "char"):
					replacement += "next();"

				replacement += "\n\t"
		else:
			replacement += "System.out.println(\"Enter the "+attribute_list.get(l)[i]+":\");\n\t"
			replacement += l+" "
			replacement += attribute_list.get(l)[i]
			if(l == "String"):
				replacement += " = in1."
			else:
				replacement += " = in."
			if(l=="int"):
				replacement+="nextInt();"
			elif(l=="String"):
				replacement+="nextLine();"
			elif(l == "double"):
				replacement+="nextDouble();"
			elif(l == "float"):
				replacement+="nextFloat();"
			elif(l == "char"):
				replacement += "next();"
			replacement += "\n\t"
	list_input = list_input.replace(matchObj.group(1),replacement)
	n = open("Queue.java","w")
	print(list_input,file = n)
	n.close()

def attr_create():
	pattern = r'(<attribute list>)'
	#code to populate node instantiation header
	m = open("Queue.java","r")
	input_Node_stream = m.read()
	m.close();
	matchObj = re.search(pattern,input_Node_stream)
	#print("matchObj.group() : ", matchObj.group(1))
	replacement=""
	global attribute_list
	for l in attribute_list:
                 if len(attribute_list.get(l)) >= 1:
                          for i in range(len(attribute_list.get(l))):
                                 replacement += attribute_list.get(l)[i]
                                 replacement += ","
                 else:
                          replacement += attribute_list.get(l)
                          replacement += ","
	replacement=replacement[:-1]
	input_Node_stream = input_Node_stream.replace(matchObj.group(1),replacement)
	n = open("Queue.java","w")
	print(input_Node_stream,file = n)
	n.close()
def print_Statements():
        """Code to print data at each node"""
        f=open("Queue.java","r")
        list_input=f.read();
        pattern=r'(<print statements>)'
        matchObj = re.search(pattern,list_input)
        #print("matchObj.group() : ", matchObj.group())
        f.close()
        replacement = ""
        for l in attribute_list:
                if len(attribute_list.get(l)) >= 1:
                        for i in range(len(attribute_list.get(l))):
                                replacement += "System.out.println(\""+attribute_list.get(l)[i]+": \"+"  
                                replacement += "temp."+attribute_list.get(l)[i]+");"
                                replacement += "\n\t"
                else:
                                replacement += "System.out.println(\""+attribute_list.get(l)[i]+": \"+"  
                                replacement += attribute_list.get(l)[i]+");"
                                replacement += "\n\t"
        list_input = list_input.replace(matchObj.group(1),replacement)
        n = open("Queue.java","w")
        print(list_input,file = n)
        n.close()
def attr_printer():
         print("The attribute set you provided is:")
         rep = attr_delimitter("\n")
         print(rep)

def __main__():
	#attr values accepted
	#all functions called
	#java exec on main Tree Builder class
	attr_count()
	template_copy()
	attr_printer()
	attribute_builder()
	attr_constructor()
	accept()
	attr_create()
	print_Statements()
	os.system("javac QNode.java")
	os.system("javac Queue.java")
	os.system("javac QueueMain.java")
	os.system("java QueueMain")
