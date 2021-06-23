## Conda install

1. Terminal を開きます。

2. conda 仮想環境 (lgbenv) を構築します。

```shell
cd day2
conda env create -f lgbenv.yml
```

3. 環境変数をロードします。

```shell
source ~/.bashrc
```
or
新しいターミナルを開いて、新しい環境変数をロードします。

4. lgbenv を有効化します。

```shell
conda activate lgbenv
```

### 注意事項

- 新しくインストールした conda 仮想環境を VScode の Python Script や Notebook で利用する前に一度 VSCode を Reload してください。

- 既存の lgbenv を更新する場合のコマンドは下記になります。

```shell
conda env update -f lgbenv.yml
```