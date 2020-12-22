# biovoice【タンパク質の音を聞いてみよう】
タンパク質のアミノ酸配列を読み取りそれに合わせた音を出します

実行環境  
biopython	1.78  
numpy	1.19.3

実行時にはパスを通す。  
あらかじめfastaファイルをbiovoice.pyと同じディレクトリに入れる。

$ python biovoice.py (読みたいタンパク質).fasta  
で実行できます

今回サンプルとして読み取るのは p53(チャイニーズハムスター由来）というタンパク質です。  
p53はがん抑制遺伝子として良く知られ、  
DNAの修復、細胞周期の調節、アポトーシスの促進に大きく関与するといわれています。

![AAC.fasta](C:\Users\white\PycharmProjects\pythonProject\biovoice_AAC.png "sample")
NCBIのここのサイトからダウンロード出来ます。
https://www.ncbi.nlm.nih.gov/protein/AAC53040.1


実行すると次の感じになります。
![jikkou](C:\Users\white\PycharmProjects\pythonProject\biovoice_jikkou.png "sample")

実行した際の音も聞ききたいときは、movieを見てください。

----------------------------------------------------------------------------------------------------------------------------
ここから、メモ↓

(2020/12/20）pycharmを導入した。「venv」（仮想環境を作成するためのモジュール）や「pip」（パッケージ管理ツール）、インタプリタの管理がめっちゃ楽。使い勝手よさそう。インタプリタとは、Pythonのコードを解釈して実行してくれるソフトウェアのことです。 biopythonを入れて本格的にfastaが読めるような実装を目指す。

→pip install biopythonでbiopython入れた。なぜか上手くいかない。 →numpyの最新版バージョンのせいだったらしい。ダウングレードしたら治った。(参考：https://qiita.com/bear_montblanc/items/b4b75dfd77da98076da5)

pycharmとgithubをアクセストークン使って連携。 biopytonの使い方(https://biomedicalhacks.com/2020-05-12/biopython-basic-1/) Genbank(.gb)のファイルは読めるようになった。

(2020/12/22)
※↑もともとHeroku_deployリポジトリで管理してましたが、煩雑になりそうなのでこちらに分けました。なので、以前の書き込みなどをこちらに移しています。
