
import json

js = open("/home/prashant/Downloads/json.json","r")
temp = open("/home/prashant/Desktop/python_codes/bill_generator/template.html","r")


t1 = temp.read()
jsr = js.read()

json1_data = json.loads(jsr)


o = open("/home/prashant/Desktop/python_codes/bill_generator/bill/bill1.html","w")
t1 = t1.replace("cname",json1_data['name'],1)
s=""
c=1
a=0
for i in json1_data:
	if c!=1:
		na = json1_data['data'+str(c-1)][0]
		q = json1_data['data'+str(c-1)][1]
		p = json1_data['data'+str(c-1)][2]
		s = s+"\n<tr>\n<td>"+str(c-1)+"</td>\n<td>"+na+"</td>\n<td>"+str(q)+"</td>\n<td>"+str(p)+"</td>\n<td>"+str(p*q) +"</td>\n</tr>\n"
		a=a+p*q
	c+=1

t1 = t1.replace("xxx",s)
t1 = t1.replace("xyz","<td>"+str(a)+"</td>")
print(s)
o.write(t1)

js.close()
temp.close()
o.close()



