import re
import argparse


def fix_name(in_fasta_path, out_fasta_path):
    '''
    This function take a genome file and write a new one with different fasta headers such that only what before the white space in the original file is written
    :param in_fasta_path: the path to the fasta file we want to change
    :param out_fasta_path: the path to the new fasta path
    :return: a new genome file with different headers
    '''

    with open(in_fasta_path, "r") as fasta_in, open(out_fasta_path, "w") as fasta_out:
        # read the file
        old = fasta_in.read()

        # make a list of each fasta header and sequence
        lst = re.split('\n', old)

        # go over the headers and take only the name up to the whitespace
        for i in range(len(lst)):
            if lst[i].startswith(">"):
                new_header = re.search("(>.*?)\s", lst[i])
                lst[i] = re.sub(">.*", new_header.group(1), lst[i])

        # print("\n".join(lst))
        fasta_out.write("\n".join(lst))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_fasta_path', '-in')
    parser.add_argument('--out_fasta_path', '-out')
    args = parser.parse_args()

    in_fasta_path = args.in_fasta_path
    out_fasta_path = args.out_fasta_path

    fix_name(in_fasta_path, out_fasta_path)