#!/usr/bin/env python3
"""
学会マスタデータ検証スクリプト
データの整合性と品質をチェックします
"""

import csv
import sys
import io
from collections import Counter, defaultdict
from datetime import datetime

# UTF-8出力設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_csv(filepath):
    """CSVファイルを読み込む"""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def check_duplicates(data):
    """重複チェック"""
    issues = []
    
    # 学会ID重複チェック
    ids = [row['学会ID'] for row in data]
    id_counts = Counter(ids)
    for id_val, count in id_counts.items():
        if count > 1:
            issues.append(f"❌ 学会ID重複: {id_val} ({count}件)")
    
    # 正式名称重複チェック
    names = [row['正式名称'] for row in data]
    name_counts = Counter(names)
    for name, count in name_counts.items():
        if count > 1:
            issues.append(f"⚠️  正式名称重複: {name} ({count}件)")
    
    return issues

def check_required_fields(data):
    """必須フィールドチェック"""
    issues = []
    required = ['学会ID', '正式名称', 'カテゴリ', 'ステータス']
    
    for i, row in enumerate(data, 2):  # 2行目から（ヘッダーを除く）
        for field in required:
            if not row.get(field):
                issues.append(f"❌ 行{i}: {field}が空です")
    
    return issues

def check_categories(data):
    """カテゴリ統計と検証"""
    stats = {}
    valid_categories = {'基本領域', 'サブスペ', 'その他'}
    issues = []
    
    categories = [row['カテゴリ'] for row in data]
    cat_counts = Counter(categories)
    
    for cat, count in cat_counts.items():
        if cat not in valid_categories:
            issues.append(f"⚠️  不明なカテゴリ: {cat}")
        stats[cat] = count
    
    return stats, issues

def check_parent_references(data):
    """親学会参照の整合性チェック"""
    issues = []
    id_set = {row['学会ID'] for row in data}
    
    for row in data:
        if row['親学会ID']:
            # 複数の親学会ID対応
            parent_ids = row['親学会ID'].split('/')
            for parent_id in parent_ids:
                if parent_id and parent_id not in id_set:
                    issues.append(f"⚠️  {row['学会ID']}: 存在しない親学会ID参照: {parent_id}")
    
    return issues

def check_data_quality(data):
    """データ品質スコア計算"""
    quality_scores = []
    
    for row in data:
        score = 100
        filled_fields = sum(1 for v in row.values() if v)
        total_fields = len(row)
        
        # フィールド充填率
        fill_rate = filled_fields / total_fields
        score = int(fill_rate * 100)
        
        # 重要フィールドの有無
        if row.get('専門医機構認定') == 'TRUE':
            score += 10
        if row.get('厚労省広告可能') == 'TRUE':
            score += 10
        if row.get('ウェブサイト'):
            score += 5
        if row.get('会員数（医師）'):
            score += 5
        
        quality_scores.append(min(score, 100))
    
    avg_score = sum(quality_scores) / len(quality_scores)
    high_quality = sum(1 for s in quality_scores if s >= 80)
    
    return {
        'average_score': avg_score,
        'high_quality_count': high_quality,
        'total_count': len(quality_scores)
    }

def generate_report(filepath):
    """検証レポート生成"""
    print("=" * 60)
    print("学会マスタデータ検証レポート")
    print("=" * 60)
    print(f"検証日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"ファイル: {filepath}")
    print()
    
    # データ読み込み
    data = load_csv(filepath)
    print(f"✅ 総レコード数: {len(data)}")
    print()
    
    # 重複チェック
    print("【重複チェック】")
    dup_issues = check_duplicates(data)
    if dup_issues:
        for issue in dup_issues:
            print(f"  {issue}")
    else:
        print("  ✅ 重複なし")
    print()
    
    # 必須フィールドチェック
    print("【必須フィールドチェック】")
    req_issues = check_required_fields(data)
    if req_issues:
        for issue in req_issues[:5]:  # 最初の5件のみ表示
            print(f"  {issue}")
        if len(req_issues) > 5:
            print(f"  ... 他{len(req_issues)-5}件")
    else:
        print("  ✅ すべて入力済み")
    print()
    
    # カテゴリ統計
    print("【カテゴリ分布】")
    cat_stats, cat_issues = check_categories(data)
    for cat, count in sorted(cat_stats.items()):
        print(f"  {cat}: {count}件")
    if cat_issues:
        for issue in cat_issues:
            print(f"  {issue}")
    print()
    
    # 親学会参照チェック
    print("【親学会参照チェック】")
    ref_issues = check_parent_references(data)
    if ref_issues:
        for issue in ref_issues[:5]:
            print(f"  {issue}")
        if len(ref_issues) > 5:
            print(f"  ... 他{len(ref_issues)-5}件")
    else:
        print("  ✅ すべて正常")
    print()
    
    # データ品質スコア
    print("【データ品質スコア】")
    quality = check_data_quality(data)
    print(f"  平均スコア: {quality['average_score']:.1f}/100")
    print(f"  高品質レコード: {quality['high_quality_count']}/{quality['total_count']}件")
    print()
    
    # 総合評価
    print("【総合評価】")
    critical_issues = len([i for i in dup_issues + req_issues if i.startswith('❌')])
    warnings = len([i for i in dup_issues + req_issues + cat_issues + ref_issues if i.startswith('⚠️')])
    
    if critical_issues == 0 and warnings == 0:
        print("  🎉 優秀: すべてのチェックをパス")
    elif critical_issues == 0:
        print(f"  ✅ 良好: 警告{warnings}件（致命的エラーなし）")
    else:
        print(f"  ⚠️  要改善: エラー{critical_issues}件、警告{warnings}件")
    
    print("=" * 60)
    
    return critical_issues == 0

if __name__ == "__main__":
    filepath = "../data/societies_master.csv"
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    
    success = generate_report(filepath)
    sys.exit(0 if success else 1)