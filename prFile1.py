import requests

# getreq = requests.get("https://api.github.com/events")
# print(getreq)

# putreq = requests.put("https://httpbin.org/put")
# print(putreq)

# headreq = requests.head("https://httpbin.org/get")
# print(headreq)

# optionreq = requests.options("https://httpbin.org/get")
# print(optionreq)

# payload = {"Key1":"Bashira","Key2":"Bahira"}
# payloadreq = requests.get("https://httpbin.org/get", params=payload)
# print(payloadreq.url)

# payloadTuple ={"Key1": "Name", "Babies": ["Bashira","Bahira"]} 
# payloadTuplereq = requests.get("https://httpbin.org/get", params=payloadTuple)
# print(payloadTuplereq.url)


#From the Video of Corey Schafer from : https://www.youtube.com/watch?v=tb8gHvYlCFs&t=997s
#r = requests.get("https://xkcd.com/353/")
payloadr2 = {"Name":"Sunvy","Pass":"12345"}
r2 = requests.post("https://httpbin.org/post",data = payloadr2)
#print(r2.text)
r2_dict = r2.json()
print(r2_dict["form"])

#print(r)
#print(dir(r)) #objects that can be accessed with the response object can be shown with dir
#print(help(r))
#print(r.text)
#print(r.status_code)
#print(r.ok)
#print(r.headers)

#imagereq = requests.get("https://imgs.xkcd.com/comics/python.png")
#print(imagereq.content)#Shows the byte information of the picture
# with open("comic.png","wb") as f: 
#     f.write(imagereq.content)

