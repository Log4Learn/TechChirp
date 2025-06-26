# 🐦 TechChirp

**TechChirp** は、技術者向けの小ネタ・Tipsを Excel から自動で読み取り、Twitter に定期投稿するための Python 製 Bot です。
「技術情報を小鳥のようにさえずる」をコンセプトに、軽やかで確実な運用を目指しています。

---

## 特徴

* `tips.xlsx` に蓄積した技術Tipsをもとに、投稿内容を自動生成
* Twitter API（v1.1 権限）を使ったツイート投稿
* 投稿履歴を記録し、重複投稿を防止
* `.env` による安全なトークン管理
* Docker 実行対応 & GitHub Actions 自動実行対応

---

## ディレクトリ構成

```
TechChirp/
├── config/             # APIキーなどを含む .env ファイル配置
├── data/               # tips.xlsx 配置ディレクトリ
├── logs/               # 実行ログ保存先
├── templates/          # tweet_template.txt を格納
├── utils/              # データ処理・履歴管理モジュール
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── main.py             # エントリーポイント
├── requirements.txt
└── README.md
```

---

## セットアップ手順

### 1. Twitter APIの準備

※ 投稿には Twitter API v1.1 の write 権限が必要です。
[Twitter Developer Portal](https://developer.x.com/en/portal/products/elevated) にて申請し、必要なトークンを取得してください。

---

### 2. `.env` の作成

`config/.env` を作成し、以下の内容を記述します：

```
TWITTER_API_KEY=xxxxxxxxxxxxxxxxxxxx
TWITTER_API_SECRET=xxxxxxxxxxxxxxxxxxxx
TWITTER_ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxx
TWITTER_ACCESS_SECRET=xxxxxxxxxxxxxxxxxxxx
```

---

### 3. `tips.xlsx` の準備

`data/tips.xlsx` に以下の形式でTipsを記載してください：

| テーマ    | 内容                                   |
| ------ | ------------------------------------ |
| Git    | git stash で作業中の変更を一時保存できます。          |
| Python | f"Hello, {name}" のようにf文字列で変数を埋め込めます。 |

---

## 実行方法

### Dockerでの実行

```bash
docker-compose run --rm app
```

※ `.env` と `tips.xlsx` が正しく配置されていることを確認してください。

---

### GitHub Actions による定期実行（任意）

`.github/workflows/post.yml` にて `cron` 設定を追加することで、自動投稿が可能です。

---

## セキュリティ上の注意

* `.env` や `tips.xlsx` は `.gitignore` によってバージョン管理から除外されています。
* **公開リポジトリに APIキーを絶対に含めないようご注意ください。**

---

## ライセンス

MIT License

---

## 🚧 補足：自動投稿機能について（2025年6月時点）

Twitter API（X API）では、**無料プラン（Essential）では write 権限が制限されており、自動投稿（`POST /statuses/update`）は利用できません**。
そのため、現在は自動投稿Botの本番運用は**保留中**です。

**今後の対応予定**：

* 有料プラン（Elevated Accessなど）での検証
* ActivityPub／Mastodon等の代替API対応も検討中

自動化をご希望の場合は、[X Developer Portal](https://developer.x.com/en/portal/products) より有料プランの申請をご検討ください。

---

## クレジット

* 開発者: Log4Learn
* コンセプト: 「技術を小鳥のように、気軽に、正しく伝える。」

