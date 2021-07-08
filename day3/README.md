# Day3 : 自然言語処理 BERT 

- [BERT の基本的な動作確認](Tutorial/BERT_NSP_MLM.ipynb)
- [BERT ファインチューニング](Tutorial/BERT_Fine_Tune.ipynb)

# Preparation
## conda 環境

install_conda.sh を実行して conda の仮想環境の作成と Jupyter Kernel への登録を実施

```bash
cd setup
./install_conda.sh # conda 名称と yml ファイル名を入力するプロンプトが現れる
# bert_env の場合
# conda 名称 : bert_env
# yml ファイル名 : bert_env.yml
```

conda の切り替えと有効化

```bash
conda init bash
source ~/.bashrc
conda env list
conda activate bert_env
```

## Data
### Livedoor
Livedoor ニュースのデータをダウンロード & 前処理
※ 時間がかかるので要注意

```bash
conda activate bert_env
cd setup
python livedoor-dataprep.py # data フォルダに整形済みの TSV をダウンロード
```
