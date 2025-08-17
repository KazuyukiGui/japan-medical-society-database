#!/usr/bin/env python3
"""
学会IDの形式を変換するスクリプト
SOC_00001 -> SOC001 形式に変換
"""

import csv
import os
import sys

def convert_id(old_id):
    """SOC_00001形式をSOC001形式に変換"""
    if not old_id or not old_id.startswith('SOC_'):
        return old_id
    
    # SOC_00001 -> SOC001
    number_part = old_id.split('_')[1] if '_' in old_id else old_id[3:]
    number = int(number_part)
    return f'SOC{number:03d}'


def convert_societies_master(filepath):
    """学会マスターのID変換"""
    temp_file = filepath + '.tmp'
    
    with open(filepath, 'r', encoding='utf-8-sig') as infile:
        with open(temp_file, 'w', encoding='utf-8-sig', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                # 学会IDを変換
                row['学会ID'] = convert_id(row['学会ID'])
                
                # 親学会IDを変換（複数の場合は/で区切られている）
                if row.get('親学会ID'):
                    parent_ids = row['親学会ID'].split('/')
                    converted_parents = [convert_id(pid) for pid in parent_ids]
                    row['親学会ID'] = '/'.join(converted_parents)
                
                writer.writerow(row)
    
    # 元のファイルを置き換え
    os.replace(temp_file, filepath)
    print(f"✓ {filepath} のID変換完了")


def convert_qualifications_master(filepath):
    """資格マスターの学会ID参照を変換"""
    temp_file = filepath + '.tmp'
    
    with open(filepath, 'r', encoding='utf-8-sig') as infile:
        with open(temp_file, 'w', encoding='utf-8-sig', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                # 学会IDを変換
                row['学会ID'] = convert_id(row['学会ID'])
                writer.writerow(row)
    
    # 元のファイルを置き換え
    os.replace(temp_file, filepath)
    print(f"✓ {filepath} のID変換完了")


def main():
    """メイン処理"""
    # プロジェクトルートに移動
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    os.chdir(project_root)
    
    # ファイルパス
    societies_file = 'data/societies_master.csv'
    qualifications_file = 'data/qualifications_master.csv'
    
    # 変換実行
    print("学会ID形式の変換を開始します...")
    print("変換形式: SOC_00001 → SOC001")
    print("-" * 40)
    
    convert_societies_master(societies_file)
    convert_qualifications_master(qualifications_file)
    
    print("-" * 40)
    print("変換が完了しました！")
    print("\n注意: データ検証スクリプトの実行をお勧めします:")
    print("  python scripts/validate_data.py data/societies_master.csv")


if __name__ == '__main__':
    main()