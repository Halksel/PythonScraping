import pandas as pd
import sys
from pprint import pprint

args = sys.argv

df = pd.read_csv(
    "armData.csv",
    encoding="shift-jis",
    usecols=[
        '武器名', '属性', '武器種', '第一スキル', '第二スキル', '最大HP', '最大ATK', '凸上限',
        '100LvHP', '100LvATK', '150LvHP', '150LvATK'
    ])


def getArms(colname,target):
    ret = df[df[colname].str.contains(target)]
    return ret


pprint(getArms(args[1],args[2]))
