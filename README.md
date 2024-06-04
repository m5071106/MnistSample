## Number recoginition sample program with m3, macOS 14.5, Python 3.10.14

### 簡易版 (number_recog.py をターミナルで実行する)

1. number_recog_train.py 冒頭のコメントをもとに必要なモジュールを準備し、実行してください。
2. models/配下にモデルが作成できていれば、3以降で数値認識ができるようになります。
3. sourceフォルダに画像ファイルを格納してください。対象拡張子はextensions.txtで制御します。
4. python3 number_recog.py
   で変換を開始します。
5. resultフォルダに音声ファイル名+年月日時分秒のテキストが格納されます。

### Web版 (front_web.py をターミナルで実行後、Web Browser で http://[hostname]:5001/でアクセス)

1. number_recog_train.py 冒頭のコメントをもとに必要なモジュールを準備し、実行してください。
2. models/配下にモデルが作成できていれば、3以降で数値認識ができるようになります。
3. python3 front_web.py でwebを起動します。
4. http://[hostname]:5001/ でアクセスします。
5. ファイルをアップロードし、変換ボタン選択で処理が始まります。
6. 結果がWeb上に表記されます。./result/フォルダを別の静的webでディレクトリが見られるよう設定することで変換結果をダウンロードします。
