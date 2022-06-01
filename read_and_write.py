import os

# ディレクトリ下のファイルを読み込んだり、ファイルを保存したりする

READ_DIRECTORY = "input"
SAVE_DIRECTORY = "output"
tmp = [1, 2, 3, 4]

for root, dirs, files in os.walk(READ_DIRECTORY, topdown=False):
    for name in files:
        # name はファイルの名前

        ### 何かしらの処理 ###

        save_file_path = os.path.join(SAVE_DIRECTORY, name)

        with open(save_file_path, mode='w') as f:

            ### 何かしらの処理 ###

            for t in tmp:
                f.write(str(t))

