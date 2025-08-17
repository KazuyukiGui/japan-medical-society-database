# Japan Medical Society Database プロジェクト概要

## プロジェクトの目的
日本の医学系学会199団体と医師資格137種類の情報を網羅したマスターデータベースの管理。医療機関における所属医師の資格管理や、医師の専門性情報の管理などに利用されている。

## 主な特徴
- **199学会・137資格の情報を収録**
  - 基本領域19学会
  - サブスペシャルティ26学会
  - 関連学会152学会
  - 認定団体2団体
- **体系的な資格マスター**
  - 専門医73種
  - 指導医39種
  - 認定医22種
  - その他3種
- **オープンデータ（CC BY 4.0ライセンス）**
- **コミュニティ主体での継続的更新**

## データファイル
- `data/societies_master.csv`: 学会マスターデータ
- `data/qualifications_master.csv`: 資格マスターデータ

## リポジトリ構造
```
├── README.md             # プロジェクト概要
├── DATA_QUALITY.md       # データ品質に関する詳細
├── CONTRIBUTING.md       # 協力ガイドライン
├── data/                 # データファイル
│   ├── societies_master.csv
│   └── qualifications_master.csv
├── scripts/              # 検証・管理スクリプト
│   ├── validate_data.py
│   ├── validate_qualifications.py
│   ├── fix_csv_format.py
│   └── reorganize_masters.py
└── docs/                 # ドキュメント類
```

## 最終更新
2024年8月