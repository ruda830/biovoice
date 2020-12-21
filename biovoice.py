"""
biopython	1.78
numpy	1.19.3

実行時にはパスを通す。あらかじめfastaファイルを同じディレクトリに入れる。
$ python biovoice.py (読みたいタンパク質).fasta
"""
import sys
from Bio import SeqIO
import winsound


#読み込みたいfastaファイルを指定して実行出来る様にする処理---------
fasta = sys.argv[1]

def read_seq(fasta):
    for record in SeqIO.parse(fasta, 'fasta'):
        
        seq = record.seq #配列だけ読む

        return seq

amino = read_seq(fasta)
print("このファイルのアミノ酸配列は：", amino)


#アミノ酸配列を周波数に変換--------------
##----maketransで一括変換するので、それまではfor分を使うべきでない？
##----↓リストだとstr.maketransが出来ない。そのため回りくどく変換させる


#後で周波数をstrからintに直した際隣のアミノ酸配列と区別できるように、先に,で区切っておく。
amino = ','.join(amino) 
print(amino)
#文字列'M','E','E','P','Q',...となる。リストにはしない。


#周波数（文字列）に変換
sound = amino.translate(str.maketrans(
    {'A':'261','R':'293','N':'329','D':'349','C':'391','Q':'440','E':'493','G':'523','H':'587','I':'659','L':'698','K':'783','M':'880','F':'987','P':'1046','S':'1174','T':'1318','W':'1396','Y':'1567','V':'1760'}
    ))
print(sound)
#文字列'880','493','493','1046','440',...となる。


#周波数を読み込んで音を出す-----------------
#リストにする
sound_list = sound.split(',')

for n in sound_list:
    beep = int(n)
    winsound.Beep(beep,500)
    print('周波数は：',beep)


