# import json
# with open ("students.json", "w") as fdes:
#     Ist = ["Iman","Ali",6436]
#     di={"Name": "Inam","Class": "Ai","Ist":Ist}
#     # json.dump(Ist,fdes)
#     json.dump(di,fdes)
with open("student.json","r") as fdes:
    data=json.load(fdes)
    print(data)
