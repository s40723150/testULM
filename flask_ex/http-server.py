from flask import Flask, render_template, send_from_directory

# for randomgrouping
import random
import requests

app = Flask(__name__)

@app.route('/') 
def hello_world():
    return 'Hello, From Flask!'
    
@app.route('/drawROC')
def drawROC():
    return render_template("drawROC.html")
    
# setup static directory
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
    
@app.route("/randomgrouping")
def randomGrouping():
    # url to get the student number data
    target_url = "http://mde.tw/cd2020/downloads/2020spring_cd_2a_list.txt"
    # use requests to retrieve data from url
    f = requests.get(target_url)
    # get student list from target_url
    # use splitlines() to put student number into studList
    studList = f.text.splitlines()
    # minimum number for each group
    num_in_one_group = 10
    # temp list to save the student number for each group
    gpList = []
    # whole class list
    group = []
    # number of member list for each group
    numList = []
    # get numList
    numList = getNumList(len(studList), num_in_one_group)
    # check numList
    # list numList
    #print("Expected number of member list:" + str(numList))
    
    output = ""
    gth = 1
    inc = 0
    
    # use shuffle method of random module to shuffle studList
    random.shuffle(studList)
    output += "Before sort: <br />"
    for i in numList:
        # print 20 * sign
        output += '=' * 20 + "<br />";
        output += "group " + str(gth) + " has " + str(i) + " members:<br />"
        # reset group list
        gpList = []
        for j in range(i):
            output += studList[j+inc] + "<br />"
            # append student number into grpList
            gpList.append(studList[j+inc])

        gth = gth + 1
        inc = inc + j
        # sort gpList
        gpList.sort()
        group.append(gpList)

    # print output which is the result before sorting
    print(output)
    # print group whis is the sorted result
    print("Sorted result:" + str(group))

    output = ""
    # output sorted result
    output += '=' * 20 + "<br />"
    output += 'Sorted result:<br />'
    gth = 1

    # list sorted data seperated by \n
    for i in range(len(group)):
        # print seperated mark
        output += '=' * 20 + "<br />"
        output += "group" + str(gth) + "<br />"
        gpList = []

        for j in range(len(group[i])):
            output += str(group[i][j]) + "<br />"

        gth = gth + 1

    return output

# get the distributed list among each group
def getNumList(total, eachGrp=10):
    # total is the number of students
    # each group at least 10 students
    #eachGrp = 10;
    # may divide into "grpNum" number of group
    grpNum = total // eachGrp;
    # check grpNum
    #print(grpNum)
    # vacan list
    splits = []
    # find remainder when total number divid into "grpNum" number of group
    remainder = total % grpNum
    # number of people in one group by calculation
    calGrp = total // grpNum

    for i in range(grpNum):
        splits.append(calGrp)

    # check first splits
    #print(splits)

    for i in range(remainder):
        splits[i] += 1

    # check final splits
    #print(splits);
    return splits;

    
if __name__== '__main__': 
	app.run()