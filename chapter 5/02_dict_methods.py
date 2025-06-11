marks={
   "moni":60,
   "piya":80,
   "santo":60
   
   
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"moni":100})
print(marks)

print(marks.get("moni")) #prints none
print(marks.get["moni"]) #returns erroe