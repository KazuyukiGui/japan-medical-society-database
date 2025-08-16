# Japan Medical Society Database (日本医学系学会データベース)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## 🎯 概要 / Overview

日本の医学系学会200団体の包括的なマスタデータベースです。医療機関の資格管理、医師の専門性管理などにご利用いただけます。

Comprehensive master database of 200 Japanese medical societies for healthcare institutions and medical professionals.

## ✨ 特徴 / Features

- 📊 **200学会を網羅** - 基本領域19学会、サブスペシャルティ26学会、その他155学会
- 🔄 **定期更新** - コミュニティによる継続的な更新
- 📖 **オープンデータ** - CC BY 4.0ライセンスで自由に利用可能
- 🤝 **コミュニティ駆動** - 誰でも貢献可能

## 📥 利用方法 / Usage

### CSVファイルの直接利用
```bash
# 最新版のダウンロード
curl -O https://raw.githubusercontent.com/[YOUR_USERNAME]/japan-medical-society-database/main/data/societies_master.csv
```

### Pythonでの利用例
```python
import pandas as pd

# GitHubから直接読み込み
url = "https://raw.githubusercontent.com/[YOUR_USERNAME]/japan-medical-society-database/main/data/societies_master.csv"
df = pd.read_csv(url)

# 基本領域の学会のみ抽出
basic_societies = df[df['カテゴリ'] == '基本領域']
print(basic_societies[['学会ID', '正式名称', '略称']])
```

## 📊 データ構造 / Data Structure

| フィールド名 | 型 | 説明 | 例 |
|------------|---|------|-----|
| 学会ID | String | 一意識別子 | SOC_00001 |
| 正式名称 | String | 法人格を含む正式名称 | 一般社団法人日本内科学会 |
| 略称 | String | 一般的な略称 | 内科学会 |
| カテゴリ | String | 分類 | 基本領域/サブスペ/その他 |
| 最終確認日 | Date | データ確認日 | 2024-08-01 |
| データソース | String | 情報の出典 | 専門医機構概報2024 |

詳細は[data/societies_master.csv](data/societies_master.csv)をご確認ください。

## 🤝 貢献方法 / Contributing

このプロジェクトへの貢献を歓迎します！

### データの誤りを報告
1. [Issues](https://github.com/[YOUR_USERNAME]/japan-medical-society-database/issues)で報告
2. 学会名、誤っている内容、正しい内容を記載

### データの追加・修正を提案
1. このリポジトリをFork
2. 修正を行い、Pull Requestを作成
3. レビュー後、マージされます

## 📈 プロジェクト統計 / Statistics

- 収録学会数: 200
- 基本領域: 19学会
- サブスペシャルティ: 26学会
- 最終更新: 2024年1月

## 📜 ライセンス / License

このデータベースは [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) の下で公開されています。

利用時は以下のクレジット表記をお願いします：
```
Japan Medical Society Database is licensed under CC BY 4.0
```

## 🙏 謝辞 / Acknowledgments

- 日本専門医機構
- 貢献者の皆様
- 医療情報の標準化に取り組むすべての方々

## 📞 連絡先 / Contact

- Issues: [GitHub Issues](https://github.com/[YOUR_USERNAME]/japan-medical-society-database/issues)
- Discussions: [GitHub Discussions](https://github.com/[YOUR_USERNAME]/japan-medical-society-database/discussions)

---

**みんなで作る、みんなのための医学会データベース**
*Together, we build the future of medical information in Japan*