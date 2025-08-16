#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

def reorganize_societies_master():
    """学会マスターのカテゴリ更新と並び順整理"""
    
    input_file = '../data/societies_master_fixed.csv'
    output_file = '../data/societies_master_reorganized.csv'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # カテゴリの詳細化
    for row in rows:
        soc_id = row['学会ID']
        current_cat = row['カテゴリ']
        
        # 基本領域はそのまま
        if current_cat == '基本領域':
            continue
            
        # サブスペは領域別に分類
        elif current_cat == 'サブスペ':
            # 内科系サブスペ（SOC_00020-00034）
            if soc_id >= 'SOC_00020' and soc_id <= 'SOC_00034':
                row['カテゴリ'] = 'サブスペ（内科系）'
            # 外科系サブスペ（SOC_00035-00040）
            elif soc_id >= 'SOC_00035' and soc_id <= 'SOC_00040':
                row['カテゴリ'] = 'サブスペ（外科系）'
            # その他サブスペ
            else:
                row['カテゴリ'] = 'サブスペ（その他）'
                
        # その他を詳細化
        elif current_cat == 'その他':
            # 認定団体
            if soc_id in ['SOC_00201', 'SOC_00202']:
                row['カテゴリ'] = '認定団体'
            # 専門医機構認定がTRUEなら関連学会（サブスペ候補）
            elif row['専門医機構認定'] == 'TRUE':
                row['カテゴリ'] = '関連学会（機構認定）'
            # それ以外は関連学会
            else:
                row['カテゴリ'] = '関連学会'
    
    # 並び順のための優先度設定
    def get_sort_key(row):
        soc_id = row['学会ID']
        category = row['カテゴリ']
        
        # カテゴリ別の優先度
        cat_priority = {
            '基本領域': '1',
            'サブスペ（内科系）': '2', 
            'サブスペ（外科系）': '3',
            'サブスペ（その他）': '4',
            '関連学会（機構認定）': '5',
            '関連学会': '6',
            '認定団体': '7'
        }
        
        priority = cat_priority.get(category, '9')
        return f"{priority}_{soc_id}"
    
    # ソート実行
    rows.sort(key=get_sort_key)
    
    # 書き出し
    fieldnames = reader.fieldnames
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"学会マスター再編成完了: {output_file}")
    
    # カテゴリ別統計表示
    categories = {}
    for row in rows:
        cat = row['カテゴリ']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n【カテゴリ別統計】")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}件")
    
    return output_file

if __name__ == "__main__":
    reorganize_societies_master()