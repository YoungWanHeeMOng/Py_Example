
import re
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러\s\d+")
#mo = regex.search(text)
#if mo != None:
#    print(mo.group()) 
mc = regex.findall(text)
print(mc)


#text = "문의사항이 있으면 010-9094-7082 으로 연락주시기 바랍니다."
 
#regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
#matchobj = regex.search(text)
#phonenumber = matchobj.group()
#print(phonenumber)  