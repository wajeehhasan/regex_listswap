import re


titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]


test_string=""
for x in titles:
	test_string+=x
	test_string+="#"



regex_exp=re.compile(r'(\b\d{4}\b)')
res=regex_exp.findall(test_string) # gives all the dates


final_string=test_string

remove_date=re.compile(r'(\(\d{4}\))')


new_str=remove_date.sub("",final_string) #movies without dates


final_list=new_str.split("#") #name of movies in list
temp_string=""
rtr_list=[]
ffinal_list=[]

for x in final_list:
	if x=="":
		continue
	else:
		ffinal_list.append(x)


for count,elem in enumerate(ffinal_list):
	temp_string=res[count]+" "+elem
	rtr_list.append(temp_string)

print(rtr_list)
