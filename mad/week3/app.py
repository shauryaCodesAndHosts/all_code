import sys
import csv
from jinja2 import Template
from matplotlib import pyplot

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
        print(l)
        # print(std_id)
        total_marks = 0
        for row in range(1, len(l)):
            # print(l[row][1])
            if std_id == l[row][0]:
                std_list.append(l[row])
                total_marks = total_marks+int(l[row][2])
        # std_list.insert(0, l[0])
        print(std_list)

        template_file = open('template.html')
        TEMPLATE = template_file.read()
        template_file.close()

        template = Template(TEMPLATE)
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
                print(total_marks)
                sub_list.append(l[row])
                c = c+1
        # print(sub_list)
        marks_list = []
        for i in sub_list:
            marks_list.append(int(i[2]))
        # print(marks_list)
        pyplot.hist(marks_list)
        pyplot.xlabel("Marks")
        pyplot.ylabel("Frequency")
        # pyplot.show()
        pyplot.savefig('img.png')
        # print(total_marks/c, max_marks)

        template_file = open('template2.html')
        TEMPLATE = template_file.read()
        template_file.close()

        template = Template(TEMPLATE)
        htmlContent = template.render(avg=total_marks/c, max=max_marks)

        newHtmlDoc = open('output.html', 'w')
        newHtmlDoc.write(htmlContent)
        newHtmlDoc.close()

except:
    template_file = open('template3.html')
    TEMPLATE = template_file.read()
    template_file.close()

    template = Template(TEMPLATE)
    htmlContent = template.render()

    newHtmlDoc = open('output.html', 'w')
    newHtmlDoc.write(htmlContent)
    newHtmlDoc.close()
