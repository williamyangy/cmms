import unittest
import pandas as pd
import os.path


class MyTestCase(unittest.TestCase):

    '''def test_something(self):
        df = pd.read_excel("combined_2021_JAN.xlsx",
                           usecols=[24],
                           names=None)  # 读取项目名称列,不要列名
        #print(df)
        df_li = df.values.tolist()
        result = []

        for s_li in df_li:
            result.append(s_li[0])
        cleanedList = [x for x in result if str(x) != 'nan']
        #print(cleanedList)

        lack_list = []
        #print(os.path.exists("./covers/ACC201.jpg"))
        #print(os.path.isfile("./covers/ACC201.jpg"))
        for item in cleanedList:
             #print("./covers/" + item)
             if os.path.isfile("./covers/" + item):
                 pass
             else:
                 lack_list.append(item)

        #print(lack_list)

        mylist = list(dict.fromkeys(lack_list))
        print(mylist)'''

    def test_something(self):
       print(int('20221', 12))







if __name__ == '__main__':
    unittest.main()
