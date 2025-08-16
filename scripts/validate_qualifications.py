#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
資格マスターデータ検証スクリプト
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

def load_societies(filepath):
    """学会マスターを読み込む"""
    societies = {}
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            societies[row['学会ID']] = row['正式名称']
    return societies

def validate_qualifications(qualifications_file, societies_file):
    """資格マスターの検証"""
    print("=" * 60)
    print("資格マスターデータ検証レポート")
    print("=" * 60)
    
    # 学会マスターを読み込み
    societies = load_societies(societies_file)
    
    # 統計情報
    stats = {
        'total': 0,
        'by_type': defaultdict(int),
        'by_system': defaultdict(int),
        'by_domain': defaultdict(int),
        'missing_society': [],
        'duplicate_ids': [],
        'validation_errors': []
    }
    
    seen_ids = set()
    qualification_records = []
    
    # 資格マスターを読み込み
    with open(qualifications_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stats['total'] += 1
            qualification_records.append(row)
            
            # ID重複チェック
            if row['資格ID'] in seen_ids:
                stats['duplicate_ids'].append(row['資格ID'])
            seen_ids.add(row['資格ID'])
            
            # 学会ID存在チェック
            if row['学会ID'] and row['学会ID'] not in societies:
                stats['missing_society'].append(f"{row['資格ID']}: {row['学会ID']}")
            
            # 統計集計
            stats['by_type'][row['資格種別']] += 1
            stats['by_system'][row['制度区分']] += 1
            stats['by_domain'][row['基本領域']] += 1
            
            # フィールド検証
            if not row['資格名称']:
                stats['validation_errors'].append(f"{row['資格ID']}: 資格名称が空")
            if not row['更新周期'].isdigit() and row['更新周期']:
                stats['validation_errors'].append(f"{row['資格ID']}: 更新周期が数値でない")
    
    # レポート出力
    print(f"✅ 総資格数: {stats['total']}")
    print()
    
    print("【資格種別別内訳】")
    for qtype, count in sorted(stats['by_type'].items()):
        print(f"  {qtype}: {count}件")
    print()
    
    print("【制度区分別内訳】")
    for system, count in sorted(stats['by_system'].items()):
        print(f"  {system}: {count}件")
    print()
    
    print("【基本領域別内訳】")
    domain_counts = sorted(stats['by_domain'].items(), key=lambda x: x[1], reverse=True)
    for domain, count in domain_counts[:10]:  # 上位10件表示
        print(f"  {domain}: {count}件")
    if len(domain_counts) > 10:
        print(f"  ...他{len(domain_counts)-10}領域")
    print()
    
    # エラーチェック
    has_errors = False
    
    if stats['duplicate_ids']:
        print("❌ 重複ID:")
        for dup_id in stats['duplicate_ids']:
            print(f"  {dup_id}")
        has_errors = True
    
    if stats['missing_society']:
        print("⚠️ 存在しない学会ID参照:")
        for missing in stats['missing_society'][:5]:  # 最初の5件のみ表示
            print(f"  {missing}")
        if len(stats['missing_society']) > 5:
            print(f"  ...他{len(stats['missing_society'])-5}件")
        has_errors = True
    
    if stats['validation_errors']:
        print("⚠️ 検証エラー:")
        for error in stats['validation_errors'][:5]:  # 最初の5件のみ表示
            print(f"  {error}")
        if len(stats['validation_errors']) > 5:
            print(f"  ...他{len(stats['validation_errors'])-5}件")
        has_errors = True
    
    if not has_errors:
        print("✅ エラーなし")
    
    # 総合評価
    print()
    print("【総合評価】")
    if not has_errors and stats['total'] > 100:
        print("🎉 優秀 - データ品質が高く、十分な資格数が登録されています")
    elif not has_errors:
        print("✅ 良好 - エラーはありませんが、さらなるデータ拡充が望まれます")
    else:
        print("⚠️ 要改善 - 上記のエラーを修正してください")
    
    print("=" * 60)
    
    return 0 if not has_errors else 1

def main():
    # スクリプトのディレクトリを基準にパスを設定
    script_dir = Path(__file__).parent
    qualifications_file = script_dir.parent / 'data' / 'qualifications_master.csv'
    societies_file = script_dir.parent / 'data' / 'societies_master.csv'
    
    # 引数でファイルパスが指定された場合は上書き
    if len(sys.argv) > 1:
        qualifications_file = Path(sys.argv[1])
    if len(sys.argv) > 2:
        societies_file = Path(sys.argv[2])
    
    # ファイル存在チェック
    if not qualifications_file.exists():
        print(f"エラー: 資格マスターファイルが見つかりません: {qualifications_file}")
        return 1
    
    if not societies_file.exists():
        print(f"エラー: 学会マスターファイルが見つかりません: {societies_file}")
        return 1
    
    # 検証実行
    return validate_qualifications(qualifications_file, societies_file)

if __name__ == '__main__':
    sys.exit(main())