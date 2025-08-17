# 推奨コマンド一覧

## データ検証コマンド
```bash
# 学会マスターの検証
python scripts/validate_data.py data/societies_master.csv

# 資格マスターの検証
python scripts/validate_qualifications.py
```

## データ整形コマンド
```bash
# CSV形式の修正
python scripts/fix_csv_format.py

# マスターデータの再編成
python scripts/reorganize_masters.py
```

## Git操作
```bash
# ステータス確認
git status

# 変更の確認
git diff

# コミット
git add .
git commit -m "種別: 変更内容"

# プッシュ
git push origin main
```

## データダウンロード
```bash
# 学会マスターをダウンロード
curl -O https://raw.githubusercontent.com/KazuyukiGui/japan-medical-society-database/main/data/societies_master.csv

# 資格マスターをダウンロード
curl -O https://raw.githubusercontent.com/KazuyukiGui/japan-medical-society-database/main/data/qualifications_master.csv
```

## ファイル操作（macOS）
```bash
# ディレクトリ内容確認
ls -la

# ファイル内容確認
cat ファイル名
head -n 20 ファイル名

# 検索
grep "検索文字列" ファイル名

# ファイル検索
find . -name "*.csv"
```