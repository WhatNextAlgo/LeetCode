import collections


def kthDistinct(arr, k):
    lst= []
    checked = []
    for x in arr:
        if x not in checked:
            checked.append(x)
            if arr.count(x) == 1:
                lst.append(x)
        
    if k > len(lst):
        return ""
    else:
        return lst[k-1]


# def kthDistinct(arr, k):
#     distinct = []
#     checked = []
#     for char in arr:
#         if(char not in checked):
#             checked.append(char)
#             if(arr.count(char) == 1):
#                 distinct.append(char)
#     if(len(distinct) < k-1 or len(distinct) == 0):
#         return ""
#     return distinct[k-1]
print(kthDistinct(arr = ["a","b","a"], k = 3))
print(kthDistinct(arr = ["meio","l","xhb","p","psuzr","hrp","bhqxm","ccqrl","d","nix","ce","bkm","jvqh","c","mpah","uh","z","hin","ekaxo","cpcy","cmvj","glnrk","uqem","vq","tw","p","tqlrv","uxf","kzxf","tjd","arm","iqfc","fmze","txq","ij","rlqv","j","up","om","hdvku","tkp","hm","vdbdd","lbmc","bpx","mqy","ddecp","zmdg","ik","msy","pzohq","fuj","s","bbb","qhy","nbz","xbhvi","dh","w","nznd","lvl","nru","y","q","jciw","lmnmm","e","lvnrk","eoi","fp","neq","wuw","qsjga","fy","qvg","dqjd","rb","ck","uhall","qcly","q","igv","uq","ijjqt","er","yxx","wyx","jlasw","aln","ohy","vf","gpzy","mywlj","xf","cgwl","wyjli","pyow","i","upic","mpze","ol","z","mxwb","iouzk","zfx","f","y","gsvv","hi","x","qgj","zvnz","vb","yyl","m","uwyhh","qgd","qcbky","h","wqiyo","ey","uqjn","ma","h","phnc","ozptm","rwk","w","yfw","lkfbb","hvaq","hh","arhm","rz","gtvi","tgpyt","np","e","z","cmodm","jhhga","yal","unhsp","acg","yn","d","vndjs","ntrj","rmixt","fh","xjs","oib","mk","p","rrhep","zdk","dyy","eox","hrtr","n","ty","nj","o","s","ewt","dyvn","hrejt","vkzj","y","swzzb","dnelj","ow","pv","c","muc","unvy","vnbk","nkwte","ef","bminn","zjgcy","u","g","fwks","cjtv","ximu","oiwp","h","h","zpbm","w","h","h","vqbq","mg","xopv","m","zceki","rn","abiwc","bid","gjvsu","pv","i","cemf","x","jrxa","ye","vovg","uhlp","enpj","oyr","mgrvo","jk","kuqe","q","k","v","gzo","zcx","ylj","kmt","x","byudz","eh","lonmh","iqnx","apzod","vif","f","bq","ik","utjnj","bx","c","oyf","kqp","zc","oxpi","t","pagk","yrup","xly","o","ipndf","qy","rqfnp","c","abnh","gm","yvzh","jro","gjxq","ir","oicxq","yplnw","rxji","cdwr","nmnv","qeiht","bu","gg","jlg","ajvqg","bumzg","lpuf","lzypp","fpxj","uwyqf","c","e","flubx","cb","se","mfw","wmerw","xun","xq","hkuiw","z","ffop","qvc","xl","yp","v","lv","ij","au","m","yjlxq","oqfne","ave","oqc","qlly","zf","pa","h","pfr","vhee","gh","lswh","si","p","nwzeb","cy","fbddc","xkvqd","smhl","t","gdlvc","umj","xujwi","sqjvz","m","bkvv","tdkg","nbk","m","wvvc","d","mlpn","zi","wemrh","qv","xww","gzq","qa","nqcp","hat","jqdg","bjz","pozj","ehv","bqct","pihs","yodi","yaxhs","if","xlw","ums","v","pa","accg","wcfdf","t","j","tlijm","twibw","q","gq","w","cyrop","von","crdtn","tjt","sldvo","ykyg","wi","uej","zmqda","b","rbim","r","r","cknvt","drmac","mnxm","bsgw","c","vwyil","hblbj","ddzr","ixe","s","yd","dx","bj","fxtmw","mbxvz","kwut","cpnt","ctr","r","a","bmxg","ecr","guofg","c","eczhh","sunz","ic","d","nu","xtle","w","ckb","fnelp","z","kpdw","pe","lz","me","vbc","sk","n","gp","fud","qphr","bbius","jyqa","anhge","tuqse","d","fi","wmrn","heds","djyrj","vv","e","cf","gylm","mdswr","jxyc","stn","uo","hyjt","nl","wcay","oee","ng","dwaii","d","kkxpi","jxir","wsv","lkz","tyf","fenfb","xfzi","o","yf","xq","etvcv","c","ajv","qm","hbfy","krzac","nd","oymuu","fsok","sblyv","fgubg","bxy","clex","cbny","y","kfgi","e","lpjd","wuq","um","trv","mkgb","dtdcj","xuetk","cj","hhzl","jcni","wk","jtrcp","jbkju","hwrr","tlbw","xypv","qmsbe","gkzm","lmwz","gwyw","yuq","uz","cq","jatsr","jpd","xw","ebfoa","kbr","zvtl","bhqhj","en","jvj","ua","pth","joral","pw","wlw","vvddv","pnx","v","u","fy","drdf","m","xepi","e","rtk","byqvc","ewu","k","d","nef","lihc","puvu","hdi","ymcnd","vwo","dripr","jloqq","jyy","b","fbzn","fth","ptzw","u","rcjjy","udm","rb","nky","txz","w","wkx","kp","ay","ots","adkr","u","tmh","ayqc","cs","ulzbt","tnz","rha","he","ly","fhanm","julf","vwpap","m","fzlx","tc","sohc","x","u","hwdgu","tdlcd","dhlq","tvs","ftam","fyjg","kq","qlww","gbn","bw","tqx","kcfmg","lahfo","ipst","pyddr","ua","ilhj","fdor","ch","lp","gcduz","trjo","kuz","rizf","xmzg","pyykm","idr","adog","i","lrot","vu","r","phbq","sbvpo","x","tb","hh","xzco","xbx","z","ccgr","xdo","qb","mf","lcib","rsir","zgyxt","zpvai","yi","clyuu","nix","h","lndqw","odz","rkjnh","bl","hhuwe","eqnmj","yt","zb","dhm","mdxow","sdhd","ugybz","caf","jfjxw","ztuoz","mxoz","e","tdo","zp","yc","tg","rtki","z","icppp","ficph","oq","jmxj","nor","dlhp","iaca","qin","qghtw","n","mrjtx","bx","fmyfr","pp"], k = 374))