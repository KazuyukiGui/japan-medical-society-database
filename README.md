# Japan Medical Society Database (日本医学系学会データベース)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## 検索サイト

**[日本の医学会・専門医資格 検索データベース](https://sites.google.com/view/med-db-jp/)**  
このデータベースを簡単に検索・閲覧できるWebサイトを公開しています。

## 概要 (Overview)

日本の医学系学会199団体と医師資格137種類の情報を網羅したマスターデータベースです。医療機関における所属医師の資格管理や、医師の専門性情報の管理など、幅広い用途にご利用いただけます。

This is a comprehensive master database of 199 Japanese medical societies and 137 medical qualifications, designed for healthcare institutions and medical professionals.

## なぜこのプロジェクトを作ったか

病院で医師の資格管理をするたびに、どこにも正確なマスターデータがなくて本当に苦労していました。「誰か作って公開してくれないかな…」とずっと思っていたのですが、もう待てないので自分で作ることにしました。

特に、日々の資格管理に追われる事務の方の苦労を、少しでも楽にできれば。それが、このマスタの一番の目的です。

この活動を一時的なものではなく、情報を持ち寄り、**日本の医療界の「当たり前のインフラ」に育てていきたい**と本気で思っています。

## 主な特徴 (Features)

- **199学会・137資格の情報を収録**: 基本領域19学会、サブスペシャルティ26学会、関連学会152学会、認定団体2団体を網羅しています。
- **体系的な資格マスター**: 専門医73種、指導医39種、認定医22種など、医師資格を体系的に整理しています。
- **継続的な更新**: コミュニティからの情報提供により、データを定期的に更新しています。
- **オープンデータ**: [CC BY 4.0ライセンス](https://creativecommons.org/licenses/by/4.0/)に基づき、どなたでも自由に利用できます。
- **コミュニティ主体**: 皆さまからの情報提供によって成り立つプロジェクトです。

## 活用事例

### 病院での資格管理
- 医師の専門医資格の有効期限管理
- 標榜科目と専門医資格の整合性確認
- 新規採用医師の資格確認

### データ分析
- 診療科別の専門医分布の分析
- 医師の専門性の可視化
- 地域医療計画の基礎データとして

### その他の活用
- ヘルスケア企業での医師データベース構築
- 医療系スタートアップでの医師マッチング
- 研究機関での医療人材分析

## 利用方法 (Usage)

### Webサイトで検索する
[検索サイト](https://sites.google.com/view/med-db-jp/)で学会名や資格名から簡単に検索できます。

### CSVファイルを直接ダウンロードする
```bash
# 学会マスターをダウンロード
curl -O https://raw.githubusercontent.com/KazuyukiGui/japan-medical-society-database/main/data/societies_master.csv

# 資格マスターをダウンロード
curl -O https://raw.githubusercontent.com/KazuyukiGui/japan-medical-society-database/main/data/qualifications_master.csv
```

### Excel/Googleスプレッドシートでの利用例

1. CSVファイルをダウンロード
2. Excel/スプレッドシートで開く
3. VLOOKUPやフィルタ機能で必要な情報を抽出

**例：内科系の学会を抽出する**
- フィルタ機能で「領域詳細」列を「内科系」でフィルタリング

**例：特定の学会の資格を調べる**
- 資格マスターで「学会ID」を使ってVLOOKUP

### Pythonでの利用例
```python
import pandas as pd

# 学会マスターを読み込む
societies_url = "https://raw.githubusercontent.com/KazuyukiGui/japan-medical-society-database/main/data/societies_master.csv"
societies_df = pd.read_csv(societies_url)

# 資格マスターを読み込む
qualifications_url = "https://raw.githubusercontent.com/KazuyukiGui/japan-medical-society-database/main/data/qualifications_master.csv"
qualifications_df = pd.read_csv(qualifications_url)

# 「基本領域」に分類される学会を抽出
basic_societies = societies_df[societies_df['カテゴリ'] == '基本領域']
print(basic_societies[['学会ID', '正式名称', '略称']])

# 内科系の専門医資格を抽出
internal_medicine_specialists = qualifications_df[
    (qualifications_df['基本領域'] == '内科') & 
    (qualifications_df['資格種別'] == '専門医')
]
print(internal_medicine_specialists[['資格ID', '資格名称']])
```

## データ構造 (Data Structure)

### 学会マスター (societies_master.csv)
| フィールド名 | 型 | 説明 | 例 |
|:---|:---|:---|:---|
| 学会ID | String | 各学会に割り当てられた一意なID | `SOC_00001` |
| 正式名称 | String | 法人格を含む正式名称 | 一般社団法人日本内科学会 |
| 略称 | String | 一般的に使われる略称 | 内科学会 |
| カテゴリ | String | 学会の分類 | 基本領域/サブスペ（内科系）/関連学会 |
| 最終確認日 | Date | データの最終確認日 | `2024-08-01` |
| データソース | String | 情報の出典元 | 専門医機構概報2024 |

### 資格マスター (qualifications_master.csv)
| フィールド名 | 型 | 説明 | 例 |
|:---|:---|:---|:---|
| 資格ID | String | 各資格に割り当てられた一意なID | `Q001` |
| 学会ID | String | 管理学会のID | `SOC_00001` |
| 資格名称 | String | 資格の正式名称 | 内科専門医 |
| 資格種別 | String | 資格の種類 | 専門医/指導医/認定医 |
| 制度区分 | String | 制度の区分 | 新専門医制度/共通/旧制度 |
| 基本領域 | String | 基本となる診療領域 | 内科 |

詳細は[data/societies_master.csv](data/societies_master.csv)および[data/qualifications_master.csv](data/qualifications_master.csv)をご覧ください。

## 本プロジェクトへのご協力について

### フィードバックをお待ちしています

#### 簡単な報告方法
- 間違いを見つけた
- こんな情報も追加してほしい  
- 使い方がわからない

→ [Issues](https://github.com/KazuyukiGui/japan-medical-society-database/issues) で「New issue」をクリックして、自由に書き込んでください。技術的な知識は不要です。

#### データの間違いを報告する場合
学会名、誤っている箇所、正しい内容を記載してください。

### データの追加・修正を提案する
1. このリポジトリをフォーク（複製）してください。
2. データを修正し、Pull Requestを作成してください。
3. 内容を確認後、データベースに反映します。

より詳しい手順は、[協力ガイドライン](CONTRIBUTING.md)をご覧ください。

## プロジェクトの状況 (Statistics)

- **収録学会数**: 199
  - **基本領域**: 19学会
  - **サブスペシャルティ**: 26学会（内科系15、外科系6、その他5）
  - **関連学会**: 152学会
  - **認定団体**: 2団体
- **収録資格数**: 137
  - **専門医**: 73種
  - **指導医**: 39種
  - **認定医**: 22種
  - **その他**: 3種
- **最終更新**: 2024年8月

## ライセンス (License)

このデータベースは、[クリエイティブ・コモンズ 表示 4.0 国際 ライセンス](https://creativecommons.org/licenses/by/4.0/)の下で公開されています。

ご利用の際は、以下のクレジット表記をお願いします。
```
Japan Medical Society Database is licensed under CC BY 4.0
```

## 謝辞 (Acknowledgments)

本データベースの作成にあたり、以下の方々に心より感謝申し上げます。
- 日本専門医機構
- ご協力いただいた全ての皆様
- 医療情報の標準化に取り組むすべての方々

## 連絡先 (Contact)

ご意見やご質問は、[GitHub Issues](https://github.com/KazuyukiGui/japan-medical-society-database/issues)までお寄せください。

---

**みんなで育てる、みんなのための医学会データベース**  
*Together, we build the future of medical information in Japan*