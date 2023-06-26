import numpy as np
import pandas as pd 
import lib.const as const
map_col = dict(zip(["o","h","c"],["本卦","互卦","变卦"]))
map_index = dict(zip(["s","x","by","sk","sg5","xg5","sg","xg","g"],
        ["上卦","下卦","变爻","五行生克","上卦（五行）","下卦（五行）","上卦*","下卦*","卦"]))
map_yao = ["初爻", "二爻" , "三爻" , "四爻" , "五爻" , "上爻"]
def qg():
    raw_number = np.random.random_integers(low = 1, high = 96, size = 3)
    return raw_number



def pan(raw_number):
    raw_number = dict(zip( ["_s","_x","_b"] , raw_number))
    bg = get_bg_8(raw_number)
    cg = get_cg_8(bg)
    hg = get_hg_8(bg)
    mhp = pd.DataFrame({"o": bg ,"h":hg, "c":cg,})
    # mhp.loc["raw"] = pd.Series(raw_number)
    mhp = mhp.loc[["s","x","by","sk","sg5","xg5","sg","xg","g"]].fillna("")
    mhp["raw"] = ""
    mhp.loc[["s","x","by"],"raw"] = list(raw_number.values())
    return mhp

#####################
def _get_tysk(by , _sg5 , _xg5):

    if by >= 4:
        yo = _sg5
        ti = _xg5 
    else:
        yo = _xg5 
        ti = _sg5
    
    rs = const.map5_rs_inv[yo][ti]
    if rs == "=":
        res = "({}) yo <h> ti ({})".format(yo , ti) 
    elif rs == "->":
        res = "({}) yo <s> ti ({})".format(yo , ti) 
    elif rs == "<-":
        res = "({}) ti <s> yo ({})".format(ti , yo) 
    elif rs == "-x":
        res = "({}) yo <k> ti ({})".format(yo , ti) 
    elif rs == "x-":
        res = "({}) ti <k> yo ({})".format(ti , yo) 
    else:
        assert False
    return res

def get_bg_8(raw_number):
    res_sign = dict()
    res_sign["s"] = raw_number["_s"] %8
    
    res_sign["x"] = raw_number["_x"] %8
    res_sign["b"] = raw_number["_b"] %6
    res_sign["s"] = 8 if res_sign["s"] == 0 else res_sign["s"] 
    res_sign["x"] = 8 if res_sign["x"] == 0 else res_sign["x"] 
    res_sign["by"] = 6 if res_sign["b"] == 0 else res_sign["b"] 
    sg5 =  const.map8_5[res_sign["s"]]
    xg5 =  const.map8_5[res_sign["x"]]

    res = _get_tysk(res_sign["b"] , sg5 , xg5)
    res_sign["sk"] = res
    res_sign["sg5"] = sg5
    res_sign["xg5"] = xg5
    res_sign["sg"]= const.map8_sign[res_sign["s"]]
    res_sign["xg"]= const.map8_sign[res_sign["x"]]
    res_sign["g"] = res_sign["sg"] + res_sign["xg"]
    return res_sign

def get_cg_8(bg):
    by = bg["b"] - 1
    cg = list(bg["g"])[::-1]
    cg[by] = (cg[by]  + 1 ) % 2
    cg = tuple(cg[::-1])
    cg_dict = g_breakdown(cg)
   
    res = _get_tysk(by , cg_dict["sg5"] , cg_dict["xg5"])
    cg_dict["sk"] = res
    cg_dict["g"] = cg
    return cg_dict

def get_hg_8(bg):
    hg =  list(bg["g"])[::-1]
    hg =  tuple(hg[2:5].copy()[::-1] +  hg[1:4].copy()[::-1])
    hg_dict = g_breakdown(hg)
    hg_dict["g"] = hg
    return hg_dict

def g_breakdown(g):
    sg = g[:3]
    xg = g[3:]
    s = const.map8_sign_inv[sg]
    x = const.map8_sign_inv[xg]
    g_dict = {
        "s":s, 
        "x":x,
        "sg5": const.map8_5[s],
        "xg5": const.map8_5[x],
        "sg":sg,
        "xg": xg,
    }
    return g_dict

#####################
def show_sign(mhp_):
    sign_df = pd.DataFrame()
    for col in mhp_[["o","h","c"]].columns:
        _series = mhp_.loc["g",col]
        sign_df[col] = [ const.map2[x]  for x in _series]
    sign_df.columns = [map_col[x] for x in sign_df.columns]
    sign_df.index = map_yao[::-1]
    return sign_df

def convert_to_chinese(mhp_):
    mhp = mhp_[["o","h","c"]].copy()
    mhp.loc["s"] = mhp.loc["s"].apply(lambda x: str(x) + " "  + const.map8_word[x] + " "
                                            "({})".format( const.map8_simplied[x]))
    mhp.loc["x"] = mhp.loc["x"].apply(lambda x: str(x) + " "  + const.map8_word[x]+ " "
                                            "({})".format( const.map8_simplied[x]))

    mhp.loc["sg5"] = mhp.loc["sg5"].apply(lambda x: const.map5_word[x])
    mhp.loc["xg5"] = mhp.loc["xg5"].apply(lambda x: const.map5_word[x])

    for col in mhp.columns:

        x = mhp.loc["sk" , col] 
        if x == "":
            continue
        x = x.replace("yo","用")
        x = x.replace("ti","体")
        x = x.replace(" <k> ","克")
        x = x.replace(" <s> ","生")
        x = x.replace( "<h> ","合")
        # print(x,x[-2])
        # print(const.map5_word[x[-2]])
        right_  = const.map5_word[x[1]]
        left_ = const.map5_word[x[-2]]
        x = x.replace(x[1],right_)
        x = x.replace(x[-2],left_)
        mhp.loc["sk" , col]  = x

    if mhp.loc["by","o"] >= 4:
        mhp.loc["sg5"] +=  " (用)"
        mhp.loc["xg5"] +=  " (体)"
    else:
        mhp.loc["sg5"] +=  " (体)"
        mhp.loc["xg5"] +=  " (用)"

    mhp.columns = [map_col[x] for x in mhp.columns]
    mhp.index = [map_index[x] for x in mhp.index]
    mhp["数字起卦"] = mhp_["raw"].values
    return mhp
