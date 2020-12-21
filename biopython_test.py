# parsingFasta1.pyで読み取り方書いてある

"""
コマンドライン

D:\python\biopython
python fastaMethods.py AAC53040.1.fasta
をうつ

C:\works\python\biopython
python fasta3.py AAC.fasta

勿論パスを通して

"""

import sys
from Bio import SeqIO
import winsound

fasta_in = sys.argv[1]  # コマンド実行時に与えられた引数の 1 番目を fasta_in という変数に渡しています。→今回はAAC53040.1.fastaを引数にしている


def choice_seq(fasta_in):
    for record in SeqIO.parse(fasta_in, 'fasta'):
        id_part = record.id  # id
        desc_part = record.description  # def line全体

        seq = record.seq  # 配列

        return seq


code = choice_seq(fasta_in)  # 配列の取り出し

print('code:', code)

c = code  # aminoの文字列
cKonma = ','.join(c)  # ->文字列'MEEPQ'

print(cKonma)  # ->文字列'M,E,E,P,Q'
c3 = cKonma.translate(str.maketrans(
    {'A': '261', 'R': '293', 'N': '329', 'D': '349', 'C': '391', 'Q': '440', 'E': '493', 'G': '523', 'H': '587',
     'I': '659', 'L': '698', 'K': '783', 'M': '880', 'F': '987', 'P': '1046', 'S': '1174', 'T': '1318', 'W': '1396',
     'Y': '1567', 'V': '1760'}))

print(c3)  # ->文字列'261,880,587,659,698,293'

c4 = c3.split(',')  # ->list型['261','880','587','659','698','293']要素内は文字列

c4_int = [int(n) for n in c4]  # ->list型[261,880,587,659,698,293]要素内は数値

for c in c4_int:  # 要素を一つずつ読み込み、要素はint型
    # print(len(code))
    print('周波数は：', c)
    winsound.Beep(c, 500)

"""
==============================================================
amino_0 = code[0] #アミノ酸の文字列を一つ読み取ってる
print('amino:' , amino_0)

moji = 'E'

if amino_0 == moji:#関数化した方がよいよね

    i=523
    winsound.Beep(i,500)
    print('played melody')

else:
    print(moji,'ではない')
==============================================================
"""
