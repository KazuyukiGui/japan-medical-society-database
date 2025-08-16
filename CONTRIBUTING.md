# 貢献ガイドライン / Contributing Guidelines

## Japan Medical Society Databaseへの貢献

このプロジェクトへの貢献を歓迎します！データの正確性向上にご協力ください。

## 貢献方法

### 1. データの誤りを報告

**Issueを作成する場合：**
- [Issues](https://github.com/KazuyukiGui/japan-medical-society-database/issues)ページへアクセス
- 「New issue」をクリック
- 以下の情報を記載：
  ```
  学会名: （例：日本内科学会）
  学会ID: （例：SOC_00001）
  誤っている内容: （具体的に記載）
  正しい内容: （修正案を記載）
  情報源: （公式サイトURL等）
  ```

### 2. データの追加・修正

**Pull Requestを作成する場合：**

1. **リポジトリをFork**
   - 右上の「Fork」ボタンをクリック

2. **ローカルにクローン**
   ```bash
   git clone https://github.com/YOUR_USERNAME/japan-medical-society-database.git
   cd japan-medical-society-database
   ```

3. **ブランチを作成**
   ```bash
   git checkout -b update/society-name
   ```

4. **データを修正**
   - `data/societies_master.csv`を編集
   - 検証スクリプトを実行：
     ```bash
     python scripts/validate_data.py data/societies_master.csv
     ```

5. **コミット**
   ```bash
   git add data/societies_master.csv
   git commit -m "Update: 学会名の情報を更新"
   ```

6. **プッシュ**
   ```bash
   git push origin update/society-name
   ```

7. **Pull Request作成**
   - GitHubで「Compare & pull request」をクリック
   - 変更内容を説明

## データ形式

### 必須フィールド
- `学会ID`: SOC_XXXXX形式の一意識別子
- `正式名称`: 法人格を含む正式名称
- `カテゴリ`: 基本領域/サブスペ/その他
- `ステータス`: 活動中/休止/解散等

### 新規学会追加時のID採番
- 最後の番号の次を使用（例：SOC_00198の次はSOC_00199）
- 必ず5桁でゼロパディング

### カテゴリ分類基準
- **基本領域**: 日本専門医機構が定める19基本領域
- **サブスペ**: 機構認定サブスペシャルティ領域
- **その他**: 上記以外の専門学会

## コーディング規約

### CSVファイル
- エンコーディング: UTF-8 with BOM
- 区切り文字: カンマ（,）
- 引用符: ダブルクォート（"）
- 日付形式: YYYY-MM-DD

### コミットメッセージ
```
種別: 簡潔な説明

- 詳細な変更内容1
- 詳細な変更内容2
```

種別：
- `Add`: 新規学会追加
- `Update`: 既存データ更新
- `Fix`: 誤りの修正
- `Remove`: 学会削除
- `Docs`: ドキュメント更新

## データ検証

変更前に必ず検証スクリプトを実行してください：

```bash
python scripts/validate_data.py data/societies_master.csv
```

以下の項目がチェックされます：
- 学会IDの重複
- 必須フィールドの入力
- 親学会IDの参照整合性
- カテゴリの妥当性

## 情報源について

信頼できる情報源を使用してください：
- 各学会の公式ウェブサイト
- 日本専門医機構の公開資料
- 厚生労働省の公式文書
- 日本医学会の会員学会リスト

## 行動規範

- 正確な情報提供を心がける
- 建設的なフィードバックを行う
- 他の貢献者を尊重する
- 個人情報や機密情報を含めない

## 質問・サポート

質問がある場合は[Issues](https://github.com/KazuyukiGui/japan-medical-society-database/issues)でお気軽にお問い合わせください。

## ライセンス

貢献いただいた内容は[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)ライセンスで公開されます。

---

ご協力ありがとうございます！