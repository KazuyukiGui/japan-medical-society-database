#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import codecs

def fix_societies_master():
    """学会マスターのBOM除去とクォート除去"""
    input_file = '../data/societies_master.csv'
    output_file = '../data/societies_master_fixed.csv'
    
    # BOM付きUTF-8として読み込み
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # BOMなしUTF-8、クォートなしで書き出し
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)
    
    print(f"学会マスター修正完了: {output_file}")
    return output_file

if __name__ == "__main__":
    fix_societies_master()