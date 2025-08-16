# 本プロジェクトへの協力について (CONTRIBUTING.md)

## Japan Medical Society Databaseへのご協力について

このプロジェクトにご関心をお持ちいただき、ありがとうございます。皆さまからの情報提供を歓迎します。ぜひ、データの品質向上のためにお力添えください。

## 協力の方法

### 1. データの間違いを報告する

**Issue（課題）を登録する場合：**
- [Issuesページ](https://github.com/KazuyukiGui/japan-medical-society-database/issues)にアクセスします。
- 「New issue」をクリックします。
- 以下の情報を参考に、内容を記載してください。
  ```
  学会名: (例：日本内科学会)
  学会ID: (例：SOC_00001)
  誤っている箇所: (具体的に記載してください)
  正しい内容: (修正案を記載してください)
  情報源: (公式サイトのURLなど)
  ```

### 2. データの追加・修正を提案する

**Pull Request機能を利用する場合：**

1. **このリポジトリをフォーク（複製）する**
   - 画面右上の「Fork」ボタンをクリックします。

2. **ローカル環境にクローン（複製）する**
   ```bash
   git clone https://github.com/YOUR_USERNAME/japan-medical-society-database.git
   cd japan-medical-society-database
   ```

3. **作業用のブランチを作成する**
   ```bash
   git checkout -b update/society-name
   ```

4. **データを修正する**
   - `data/societies_master.csv` を編集します。
   - 編集後、検証スクリプトを実行してください。
     ```bash
     python scripts/validate_data.py data/societies_master.csv
     ```

5. **変更内容をコミット（保存）する**
   ```bash
   git add data/societies_master.csv
   git commit -m "Update: 学会名の情報を更新"
   ```

6. **変更内容をプッシュ（送信）する**
   ```bash
   git push origin update/society-name
   ```

7. **Pull Requestを作成する**
   - GitHub上で「Compare & pull request」ボタンをクリックし、変更内容を説明してください。

## データ形式について

### 必須項目
- `学会ID`: `SOC_XXXXX`形式の一意なID
- `正式名称`: 法人格を含む正式名称
- `カテゴリ`: 「基本領域」「サブスペ」「その他」のいずれか
- `ステータス`: 「活動中」「休止」「解散」など

### 新しい学会を追加する場合のID採番ルール
- 既存のIDの最後の番号に続く数字を使用してください (例：`SOC_00198` の次は `SOC_00199`)。
- IDは必ず5桁とし、ゼロ埋めしてください。

### カテゴリの分類基準
- **基本領域**: 日本専門医機構が定める19の基本領域
- **サブスペ**: 機構が認定するサブスペシャルティ領域
- **その他**: 上記以外の学会

## コーディング規約

### CSVファイル
- 文字コード: UTF-8 with BOM
- 区切り文字: カンマ (`,`)
- 引用符: ダブルクォート (`"`)
- 日付形式: `YYYY-MM-DD`

### コミットメッセージ
```
種別: 変更内容の要約

- 変更点の詳細1
- 変更点の詳細2
```

**種別の例：**
- `Add`: 新しい学会の追加
- `Update`: 既存データの更新
- `Fix`: 誤りの修正
- `Remove`: 学会の削除
- `Docs`: ドキュメントの更新

## データ検証について

データを変更した際は、必ず検証スクリプトを実行してください。

```bash
python scripts/validate_data.py data/societies_master.csv
```

このスクリプトは以下の項目をチェックします：
- 学会IDの重複
- 必須項目の入力漏れ
- 親学会IDの整合性
- カテゴリ分類の妥当性

## 情報源について

情報の追加・修正を行う際は、信頼性の高い情報源をご利用ください。
- 各学会の公式サイト
- 日本専門医機構の公開資料
- 厚生労働省の公式文書
- 日本医学会の会員学会リスト

## 行動規範
- 正確な情報の提供を心がけてください。
- 建設的な意見交換を行いましょう。
- 他の協力者に敬意を払いましょう。
- 個人情報や機密情報は含めないでください。

## ご質問・サポート
ご不明な点があれば、[Issues](https://github.com/KazuyukiGui/japan-medical-society-database/issues)でお気軽にお尋ねください。

## ライセンス
ご協力いただいた内容（データやコード）は、[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)ライセンスで公開されます。

---

ご協力に心より感謝いたします。