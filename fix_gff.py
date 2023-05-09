
import re
rows = []
with open("err.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        row_re = re.search("gff3:(\d*):", line)
        if row_re:
            rows.append(int(row_re.group(1)))

print(rows)
print(len(rows))


'''
make a file with the error lines to test the script ahed
'''
a = 1
with open("ae.longissima.pgsb.Feb2020.LC.gff3", 'r') as gff_in, open("error_lines.txt", 'w') as err_out:
    l = gff_in.readline()
    while l:
        if a in rows:
            print(l, file=err_out)
        a+=1
        l = gff_in.readline()


# with open("ae.longissima.pgsb.Feb2020.LC.gff3", 'r') as gff_in, open("longissima_new_gff.gff3", 'w') as gff_out:

with open("error_lines.txt", 'r') as gff_in, open("test1.txt", 'w') as gff_out:
    line = gff_in.readline()
    while line:
        # print(line)
        # old_comp = re.compile(r";description=(.*);(.*);")

        old_comp = re.compile(r"chr(.*)")
        print(re.search(old_comp, line).group(1))
        # fun = lambda x: 'description={};name={}'.format(x.group(1), x.group(2))
        # new_line = re.sub(old_comp, fun, line)
        # print(new_line)
        # print(line)
        # print(new_line, file=gff_out)
        line = gff_in.readline()

    # a =1  # the firat row is header so start with 1
    # line = gff_in.readline()
    # while line:
    #     #go over each line and see if it is in the list, if not write it to the new file
    #     if a in rows:
    #         print(line)
    #     # line=gff_in.readline()
    #     # a += 1
    #         print(line, file="longissima_new_gff.gff3")
    #
    #     # if the row is in the list correct it
    #     else:
    #         old = re.search(r"descriptoin=(.*);(.*);")
    #         fun = lambda old : 'descriptoin={};name={}'.format(old.group(1), old.group(2))
    #         new_line = re.sub(r"descriptoin=(.*);(.*);", fun, line)
    #         print(new_line)
    #         print(line)
    #     line = f.readline()
    #     a += 1
    #     if a > max(rows):
    #         break
    #

