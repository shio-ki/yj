##############
##############
# map2 = {1: "_____",0:"__ __"}
map2 = {1: "_______",0:"___ ___"}
map8_sign = {1:(1,1,1),
            2:(0,1,1),
            3:(1,0,1),
            4:(0,0,1),
            5:(1,1,0),
            6:(0,1,0),
            7:(1,0,0),
            8:(0,0,0),
        }
map8_sign_inv = {v:k for k , v in map8_sign.items()}
map8_name = {1:"q",2:"d",3:"l",4:"z",5:"x",6:"ka",7:"g",8:"ku",}
map8_word = {1:"乾",
           2:"兑",
          3:"离",
          4:"震",
          5:"巽",
          6:"坎",
          7:"艮",
          8:"坤",
        }


map8_simplied = {1:"天",
          2:"泽",
          3:"火",
          4:"雷",
          5:"风",
          6:"水",
          7:"山",
          8:"地",
        }


##############
map5_word = {"j":"金","m":"木","s":"水","h":"火","t":"土",}

map8_5 = {1:"j",2:"j",3:"h",4:"m",5:"m",6:"s",7:"t",8:"t",}

map5_rs = {
            "m":{"=":"m","->":"h","<-":"s","x-":"j","-x":"t"},
            "h":{"=":"h","->":"t","<-":"m","x-":"s","-x":"j"},
            "t":{"=":"t","->":"j","<-":"h","x-":"m","-x":"s"},
            "j":{"=":"j","->":"s","<-":"t","x-":"h","-x":"m"},
            "s":{"=":"s","->":"m","<-":"j","x-":"t","-x":"h"},
            
        }
map5_rs_inv = { k: {v2:k2 for k2 , v2 in v.items() }for k , v in map5_rs.items()}

rs_symbol = {"bh":"=", "ts":"->", "st":"<-" , "tk":"-x" , "kt":"x-"} 

##############
map_dz = {1:"m",2:"m",3:"t",4:"h",5:"h",6:"t",7:"j",8:"j",9:"t",10:"s",11:"s",12:"t"}



