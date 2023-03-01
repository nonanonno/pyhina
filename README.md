# pyhina

Python でのパッケージ作成のテンプレート。ビルドシステムとして `setuptools` を使用する。

## 前提環境

- python (>= 3.8)
- pyenv (テストで使用)

## インストール

## 開発者向け

### セットアップ

以下のコマンドでeditorモードでインストールする。

```shell
pip install -e .[develop,test]
```

### テスト

```shell
tox
```