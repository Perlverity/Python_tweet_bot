import os
import datetime
import shutil

def make_move():
    """
    docstring
    """

    # 昨日のランキング
    date_today = datetime.date.today()
    date_yesterday = date_today - datetime.timedelta(days=1)
    str_date = date_yesterday.strftime('%Y-%m-%d')

    path = '/Users/administrator/Google ドライブ/16 Python/01 WordPress/03 pixiv保管庫/'
    new_dir_path = path + str_date

    # print(new_dir_path)

    os.makedirs(new_dir_path, exist_ok=True)


    path_dir = "/Users/administrator/Google ドライブ/16 Python/01 WordPress/01Twitter_bot/illusts"
    move_dir = new_dir_path

    list_file_name =  os.listdir(path_dir)

    for i_file_name in list_file_name:
        join_path = os.path.join(path_dir,i_file_name)
        move_path = os.path.join(move_dir,i_file_name)

        if os.path.isfile(join_path):
            shutil.move(join_path,move_path)

if __name__ == '__main__':
    make_move()