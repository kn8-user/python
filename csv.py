rl = open("all_lines.txt", "r")
csv = open("op.csv", "a")

host = open("host.txt", "a")
status = open("status.txt", "a")
msg = open("msg.txt", "a")

for each in rl.readlines():
    each = each.strip("\n")
    sp = each.split()

    # print(sp)

    if "SUCCESS" in sp:
        csv.write(sp[0] + "," + sp[2] + "\n")
        host.write(sp[0] + "\n")
        status.write(sp[2] + "\n")

    elif 'FAILED!' in sp:
        csv.write(sp[0] + "," + sp[2] + "," + sp[5] + " " + sp[6].rstrip(",") + "\n")
        host.write(sp[0] + "\n")
        status.write(sp[2] + "\n")
        msg.write(sp[5] + " " + sp[6].rstrip(",") + "\n")

    elif 'UNREACHABLE!' in sp:
        csv.write(sp[0] + "," + sp[2] + "," + sp[7] + " " + sp[8].rstrip(",") + "\n")
        host.write(sp[0] + "\n")
        status.write(sp[2] + "\n")
        msg.write(sp[7] + " " + sp[8].rstrip(",") + "\n")

rl.close()
csv.close()
host.close()
status.close()
msg.close()
