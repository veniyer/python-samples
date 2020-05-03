import json

#print "reading input1*****"




dict_id_name = {}
with open('input1.json') as json_file:
    data1 = json.load(json_file)
    for item in data1:
        #print "Processing item " + str(item["id"]) + "," + item["name"];
        dict_id_name[item["id"]] = item["name"]

#print  dict_id_name

#print "reading input2*****"
with open('input2.json') as json_file:
    data2 = json.load(json_file)
    for item in data2:
        itsnameinfile2 = item["name"]
        itsnameinfile1 = dict_id_name[item["service_action_id"]]
        if itsnameinfile1 == item["service_action_name"]:
        	samename = '0'
        else:
        	samename = '1'
        print itsnameinfile2 + "," + itsnameinfile1 + "," + item["service_action_name"] + "," + samename
