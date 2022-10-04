append_list = []
flag = 0
full_line = ""


def full_line_reset():
    global full_line, flag
    full_line = ""
    flag = 0


full_line_reset()

f = open("/Users/lchalla/PycharmProjects/pythonProject/raw.txt", "r")

for each in f.readlines():
    each = each.strip("\n")
    if each != "}":
        full_line += each
        # print("IF CON")
        # print("Each Item, ", each)
        # print("Line Item, ", full_line)

    elif each == "}":
        full_line += " }"
        append_list.append(full_line)
        flag = 1
        # print("EIF CON")
        # print("Each Item, ", each)
        # print("Line Item, ", full_line)

    if flag == 1:
        # print("Flag is 1, Please reset full_line")
        full_line_reset()
        # print("RESET FULL LINE, ", full_line)

f.close()

nf = open("all_lines.txt", "a")
for each in append_list:
    nf.write(each+"\n")

nf.close()
