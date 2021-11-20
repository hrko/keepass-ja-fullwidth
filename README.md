# keepass-ja-fullwidth
KeePass 2.x の日本語化ファイルの半角カナを全角カナに置換するPythonスクリプト

# ダウンロード
[Releases](https://github.com/hrko/keepass-ja-fullwidth/releases) から変換済みの .lngx ファイルをダウンロードできます。

# 使い方
自分で変換したいときは次のように実行します。

```
$ python convert.py VERSION
```

例: バージョン 2.49 の日本語翻訳ファイルを全角化する場合

```
$ python convert.py 2.49
converted file has been saved to Japanese-2.49-FullWidth.lngx
$ ls
convert.ipynb  convert.py  Japanese-2.49-FullWidth.lngx  LICENSE  README.md
```


