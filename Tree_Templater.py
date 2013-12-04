#!/usr/lib/python3.2
import re
import os
import fileinput
from collections import defaultdict
'''Templates code within <> will always be replaced at various functions,
	therefore can use grouping find line numbers and do it'''
attribute_list = defaultdict(list)

def template_copy():
		input_Node = open("Node_template.java","r")
		input_Node_write = input_Node.read()
		g = open("Node.java","w")
		print(input_Node_write,file = g)
		g.close()
		input_Node.close()
		k = open("Tree_template.java","r")
		k_write = k.read()
		m = open("Tree.java","w")
		print(k_write,file = m)
		k.close()
		m.close()
		
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
		m = open("Node.java","r")
		input_Node_stream = m.read()
		inh = input_Node_stream
		matchObj = re.search(pattern,input_Node_stream)
		#print("matchObj.group() : ", matchObj.group(1))
		replacement = attr_delimitter(";\n\t")
		#print(replacement)
		to_be_replaced = str(matchObj.group(1))		
		input_Node_stream = input_Node_stream.replace(to_be_replaced,replacement)
		n = open("Node.java","w")
		print(input_Node_stream,file = n)
		n.close()
		#replace using re.sub the tuple in attribute list location
def attr_constructor():
		pattern = r'\((.*)\)'
		#code to populate constructor header
		m = open("Node.java","r")
		input_Node_stream = m.read()
		matchObj = re.search(pattern,input_Node_stream)
		#print("matchObj.group() : ", matchObj.group(1))
		replacement = attr_delimitter(",")
		replacement = replacement[:-1]
		input_Node_stream = input_Node_stream.replace(matchObj.group(1),replacement)
		n = open("Node.java","w")
		print(input_Node_stream,file = n)
		m.close()
		n.close()
		constr_curly()
		
		#find pos of last line then add the intialization attrs there
def constr_curly():
		 pattern =  r'(<set>)'
		 m = open("Node.java","r")
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
		 n = open("Node.java","w")
		 print(input_Node_stream,file = n)
		 n.close()

def tree_accept():
		 pattern =  r'(<.*>)'
		 m = open("Tree.java","r")
		 input_Node_stream = m.read()
		 matchObj = re.search(pattern,input_Node_stream)
		 #print("matchObj.group() : ", matchObj.group())
		 m.close()
		 replacement = ""
		 for l in attribute_list:
			  if len(attribute_list.get(l)) >= 1:
				     for i in range(len(attribute_list.get(l))):
                                            replacement += "System.out.println(\"Enter the "+attribute_list.get(l)[i]+":\");\n\t"
                                            replacement += l+" "
                                            replacement += attribute_list.get(l)[i]
                                            if(l != "String"):
                                                replacement += " = in."
                                            else:
                                                replacement += " = in1."
                                            if(l == "int"):
                                                replacement += "nextInt()"
                                            elif(l == "double"):
                                                replacement += "nextDouble()"
                                            elif(l == "float"):
                                                replacement += "nextFloat()"
                                            elif(l == "String"): 
                                                replacement += "nextLine()"
                                            elif(l == "char"):
                                                replacement += "next()"
                                            replacement += ";\n\t"
			  else:
				    replacement += "System.out.println(\"Enter the "+attribute_list.get(l)+":\");\n\t"
				    replacement += l+" "
				    replacement += attribute_list.get(l)
				    if(l != "String"):	
				    	replacement += " = in."
				    else:
                                        replacement += " = in1."
				    if(l == "int"):
                                        replacement += "nextInt()"
				    elif(l == "double"):
                                        replacement += "nextDouble()"
				    elif(l == "float"):
                                        replacement += "nextFloat()"
				    elif(l == "String"):
                                        replacement += "nextLine()"
				    elif(l == "char"):
                                        replacement += "next()"
				    replacement += ";\n\t"

		 input_Node_stream = input_Node_stream.replace(matchObj.group(1),replacement)
		 n = open("Tree.java","w")
		 print(input_Node_stream,file = n)
		 n.close()
		 tree_attr_add()
def tree_attr_add():
		#code to populate constructor header in Node add
		pattern = r'\((<attribute list>)\)'
		m = open("Tree.java","r")
		inp= m.read()
		matchObj = re.search(pattern,inp)
		#print(matchObj.group(1))
		replacement = ""
		m.close()
		for l in attribute_list:
		    if len(attribute_list.get(l)) >= 1:
                        for i in range(len(attribute_list.get(l))):
                            replacement += attribute_list.get(l)[i]+","
		    else:
                        replacement += attribute_list.get(l)+","
		replacement = replacement[:-1]
		#print(replacement)
		inp = inp.replace(matchObj.group(1),replacement)
		n = open("Tree.java","w")
		print(inp,file = n)
		n.close()
def tree_insert():
		pattern = r'(<comparism>)'
		m = open("Tree.java","r")
		inp = m.read()
		matchObj = re.search(pattern,inp)
		#print(matchObj.group(1))
		m.close()
		replacement = ""
		for l in attribute_list:
			if(l != "String"):
				replacement += "add."
				replacement += attribute_list.get(l)[0]
				replacement += " <= temp."
				replacement += attribute_list.get(l)[0]
			else:
				replacement += "add."+attribute_list.get(l)[0]
				replacement += ".compareTo(temp."
				replacement += attribute_list.get(l)[0]+")"
				replacement += " <= 0"
			break
		#print(replacement)
		inp = inp.replace(matchObj.group(1),replacement)
		n = open("Tree.java","w")
		print(inp,file =  n)
		n.close()
def print_Statements():
		"""Code to print data at each node"""
		f=open("Tree.java","r")
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
					replacement += "root."+attribute_list.get(l)[i]+");"
					replacement += "\n\t"
			else:
					replacement += "System.out.println(\""+attribute_list.get(l)[i]+": \"+"  
					replacement += "root."+attribute_list.get(l)[i]+");"
					replacement += "\n\t"
		list_input = list_input.replace(matchObj.group(1),replacement)
		n = open("Tree.java","w")
		print(list_input,file = n)
		n.close()
def attr_printer():
         print("The attribute set you provided is:")
         rep = attr_delimitter("\n")
         print(rep)
			
def call():
	#attr values accepted
	#all functions called
	#java exec on main Tree Builder class
	attr_count()
	template_copy()
	attr_printer()
	attribute_builder()
	attr_constructor()
	tree_accept()
	tree_insert()
	print_Statements()
	os.system("javac Node.java")
	os.system("javac Tree.java")
	os.system("javac TreeMain.java")
	os.system("java TreeMain")
'''attr_count()
template_copy()
attribute_builder()
attr_constructor()
tree_accept()
tree_insert()
print_Statements()
os.system("javac Tree.java")
os.system("java TreeMain")'''
