import os
import re
import argparse
import time

def write_err(GFF_file):
    '''save the error output of the gff3ToGenePred command to a file'''

    os.system("gff3ToGenePred {} stdout  &>  err.txt".format(GFF_file))


def take_rows(err_file):
    '''Take the rows number from the err file'''
    rows = []
    with open(err_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            row_re = re.search("gff3:(\d*):", line)
            if row_re:
                rows.append(int(row_re.group(1)))
    return rows

# print(rows)
# print(len(rows))


'''
loop over the ines in the gff file and write them to a new file unless they are in the error list than fix them
byt adding 'name='
'''

def fix_gff(GFF_file, rows):
    with open(GFF_file, 'r') as gff_in, open("new_gff2.gff3", 'w') as gff_out:

        a = 1

        line = gff_in.readline()

        while line:
            #go over each line and see if it is in the list, if not write it to the new file
            if a not in rows:
                gff_out.write(line)

            # if the row is in the list correct it
            else:
                # old = re.search(r"descriptoin=(.*);(.*);")
                fun = lambda x : 'description={};name={}'.format(x.group(1), x.group(2))
                new_line = re.sub(r"description=(.*?);(.*?);", fun, line)  # The '?' makes it not greedy so it will refer to the first match (i.e. stop after the first ';')
                print(new_line)
                print(line)
                gff_out.write(new_line)
            line = gff_in.readline()
            a += 1
            # if a > max(rows):
            #     break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_gff', '-gff', type=str)
    parser.add_argument('--err_file', '-err', type=str)
    args = parser.parse_args()

    # write_err(args.in_gff)
    # time.sleep(15)
    rows = take_rows(args.err_file)
    fix_gff(args.in_gff, rows)


