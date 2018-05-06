# python のコマンドラインパーサーの比較

python のコマンドラインインターフェイス比較用リポジトリ

下記のブログエントリで使用したコードになります。
http://replicity.hateblo.jp/entry/2018/05/07/015029

## 比較対象
- optparse
- argparse
- docopt
- click

## simple interface

`ls` のような `command [option]` のインターフェイスの実装。

## subcommand interface 

`git` の `git subcommand [option]`のようなサブコマンドのインタフェースの実装。
`hg`の `add`,`branch`のインターフェイスを一部実装してあります。

