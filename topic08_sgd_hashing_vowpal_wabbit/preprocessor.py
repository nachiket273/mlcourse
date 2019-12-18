import argparse
import os
from tqdm import tqdm

def preprocess(in_file, out_file):
    f = open(in_file, "r")
    tags = ['javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift']
    tag_dict = dict()
    for i, tag in enumerate(tags):
        tag_dict[tag] = i+1

    fw = open(out_file, 'a')
    num_line = 0
    for line in tqdm(f):
        if num_line > 0:
            fw.write(os.linesep)
        num_line = 0
        num_tabs = line.count('\t')
        if num_tabs == 1:
            text, labels = line.split('\t')
            arr = [label.lower() for label in labels.split(' ')]
            cnt = 0
            match = ''
            for tag in tags:
                if tag in arr:
                    cnt += 1
                    match = tag
            if cnt == 1:
                for char in ['|', ':']:
                    text = text.replace(char, '')
                str1 =  str(tag_dict[match])+ ' | ' + text
                fw.write(str1)
                if num_line == 0:
                    num_line += 1

    f.close()
    fw.close()

def main():
    parser = argparse.ArgumentParser(description="Interface to preprocess text")
    parser.add_argument('-ip_fp', required=True, type=str, \
                        help='Input file path that contains text to be processed')
    parser.add_argument('-op_fp', required=True, type=str, \
                        help='Output file path where preprocessed text will be stored ')
    args = parser.parse_args()
    in_file = args.ip_fp
    out_file = args.op_fp

    if not os.path.exists(in_file):
        raise Exception(f"Input File {in_file} doesn't exist.")
    
    preprocess(in_file, out_file)


if __name__ == "__main__":
    main()