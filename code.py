append_list = []
flag = 0
full_line = ""


def full_line_reset():
    global full_line, flag
    full_line = ""
    flag = 0


full_line_reset()

f = open("raw.txt", "r")

for each in f.readlines():
    each = each.strip("\n")
    if each != "}":
        full_line += each
 

    elif each == "}":
        full_line += " }"
        append_list.append(full_line)
        flag = 1


    if flag == 1:
        full_line_reset()


f.close()

nf = open("all_lines.txt", "a")
for each in append_list:
    nf.write(each+"\n")

nf.close()
