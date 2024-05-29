#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# usage：python formal-F.py input.fa P/N/none output.vec
# P:AMP
# N:Non_AMP
# none:Predictive_sequence

aacode = {
    'A': "1", 'C': "2", 'D': "3", 'E': "4",
    'F': "5", 'G': "6", 'H': "7", 'I': "8",
    'K': "9", 'L': "10", 'M': "11", 'N': "12",
    'P': "13", 'Q': "14", 'R': "15", 'S': "16",
    'T': "17", 'V': "18", 'W': "19", 'Y': "20",
}

def convert_sequence(sequence):
    converted_seq = []
    for aa in sequence:
        if aa in aacode:
            converted_seq.append(aacode[aa])
        else:
            converted_seq.append("format error")
            
    while len(converted_seq) < 40:
        converted_seq.append("0")
        
    return ",".join(converted_seq)

def main():
    input_file = sys.argv[1]
    mode = sys.argv[2]
    output_file = sys.argv[3]
    output = []    
    
    with open(input_file, 'r') as f:
        sequences = f.readlines()
        for line in sequences:
            line = line.strip()
            if line.startswith(">"):
                continue
            else:
                seq = line.upper()
                converted_seq = convert_sequence(seq)
                
                if mode == "P":
                    converted_seq += ",1"
                elif mode == "N":
                    converted_seq += ",0"
                elif mode == "none":
                    converted_seq = converted_seq
                output.append(converted_seq)

    with open(output_file, 'w') as i:
        i.write('\n'.join(output))
        i.write("\n")
        
if __name__ == "__main__":
    main()
