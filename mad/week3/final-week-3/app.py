import sys
import csv
from jinja2 import Template
from matplotlib import pyplot

TEMPLATE1='''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Student Data</title>
        <meta name="description" content="This page lists Jnanpith Awardees"/>
        <link rel="stylesheet" href="./style.css">
    </head>
    <body>
        <div id="intro">
            <h1> Student Details</h1>
        </div>
        <div id="main">
            <table style="border: 1px solid black;">
                <thead >
                    <tr >
                      <th style="border: 1px solid black;text-align: center;">Student id</th>
                      <th style="border: 1px solid black;text-align: center;">Course id</th>
                      <th style="border: 1px solid black;text-align: center;">Marks</th>
                    </tr>
                </thead>
                <tbody >
                    {% for row in std_list %}
                    <tr>
                        <td style="border: 1px solid black;text-align: center;" >{{row[0]}}     </td>
                        <td style="border: 1px solid black;text-align: center;" >{{row[1]}}     </td>
                        <td style="border: 1px solid black;text-align: center;" >{{row[2]}}     </td>
                    </tr>
                    {% endfor %}
                    <tr>
                        <td colspan="2" style="border: 1px solid black;text-align: center;">Total Marks </td>
                        <td style="border: 1px solid black;text-align: center;">{{total}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>
</html>
'''

TEMPLATE2 = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Course Data</title>
        <meta name="description" content="This page lists Jnanpith Awardees"/>
        <link rel="stylesheet" href="./style.css">
    </head>
    <body>
        <div id="intro">
            <h1> Course Details</h1>
        </div>
        <div id="main">
            <table style="border: 1px solid black;">
                <thead >
                    <tr >
                      <th style="border: 1px solid black;text-align: center;">Average Marks</th>
                      <th style="border: 1px solid black;text-align: center;">Maximum Marks</th>
                    </tr>
                </thead>
                <tbody >
                    <tr>
                        <td style="border: 1px solid black;text-align: center;" >{{avg}}</td>
                        <td style="border: 1px solid black;text-align: center;" >{{max}}</td>
                    </tr>
                </tbody>
            </table>
            <img src="img.png" alt="Sorry for the error">
        </div>
    </body>
</html>

'''

TEMPLATE3='''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Something Went Wrong</title>
        <meta name="description" content="This page lists Jnanpith Awardees"/>
        <link rel="stylesheet" href="./style.css">
    </head>
    <body>
        <div id="intro">
            <h1> Wrong Inputs</h1>
        </div>
        <div id="main">
            <p>Something went wrong</p>
        </div>
    </body>
</html>
'''



try:
    arg = sys.argv
    l = []
    std_list = []
    if arg[1] == '-s':
        with open('./data.csv', 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                l.append(row)
        std_id = arg[2]
        #print(l)
        # print(std_id)
        total_marks = 0
        for row in range(1, len(l)):
            # print(l[row][1])
            if std_id == l[row][0]:
                std_list.append(l[row])
                total_marks = total_marks+int(l[row][2])
        # std_list.insert(0, l[0])
        #print(std_list)
        if(std_list==[]):
            raise Exception("Error")

        template = Template(TEMPLATE1)
        htmlContent = template.render(std_list=std_list, total=total_marks)

        newHtmlDoc = open('output.html', 'w')
        newHtmlDoc.write(htmlContent)
        newHtmlDoc.close()

    if arg[1] == '-c':
        with open('./data.csv', 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                l.append(row)
        sub_id = arg[2]
        max_marks = 0
        total_marks = 0
        c = 0
        sub_list = []
        # print(l)
        # print(sub_id)
        for row in range(1, len(l)):
            # print(int(l[row][1]))
            if int(sub_id) == int(l[row][1]):
                if max_marks < int(l[row][2]):
                    max_marks = int(l[row][2])
                total_marks = total_marks+int(l[row][2])
                #print(total_marks)
                sub_list.append(l[row])
                c = c+1
        # print(sub_list)
        marks_list = []
        for i in sub_list:
            marks_list.append(int(i[2]))
        # print(marks_list)
        if(marks_list==[]):
            raise Exception("Error")

        pyplot.hist(marks_list)
        pyplot.xlabel("Marks")
        pyplot.ylabel("Frequency")
        # pyplot.show()
        pyplot.savefig('img.png')
        # print(total_marks/c, max_marks)


        template = Template(TEMPLATE2)
        htmlContent = template.render(avg=total_marks/c, max=max_marks)

        newHtmlDoc = open('output.html', 'w')
        newHtmlDoc.write(htmlContent)
        newHtmlDoc.close()

except:

    template = Template(TEMPLATE3)
    htmlContent = template.render()

    newHtmlDoc = open('output.html', 'w')
    newHtmlDoc.write(htmlContent)
    newHtmlDoc.close()
