from typing import Union,Optional
from numpy  import log,exp,sign,float64

def alpha(e:float) -> float:
    """Compute voting weight of h(x)."""
    assert e!=0, "<e> must not be 0"
    return float(0.5*log((1-e)/e))

def weight(_w:list,_alpha:Optional[float]=None,avg:Optional[float]=None,count:Optional[int]=None) -> list:
    """Recompute weights (Weighting update)."""
    if len(_w)==0:
        assert count!=None, "To initialize the weight array, you need to add the <count> parameter.\nEx => W:list[list] = weight([],count=len(X))"
        _w = [1/count for _ in range(count)]
    else:
        _temp:list = []
        for n in range(len(_w)):
            # print(f"{sign(X,avg)[n]}, {Y[n]}")
            _exp:float64 = exp(-_alpha*Y[n]*I(X,avg[1],avg[0])[n])
            _temp.append(_w[n]*_exp)
        zt:int = sum(_temp)
        _w = [_/zt for _ in _temp]
    return _w

def I(_value:list,threshold:float,symbol:str='<'):
    _result:list = []
    for value in _value:
        _ = 1 if value < threshold else -1
        _result.append(_)
    if symbol == '<':return _result
    elif symbol == '>':return [-_ for _ in _result]
    else: raise ValueError()

def error(x:list,y:list,p:list) -> tuple[list[Union[str,int]],float]:
    """Train a weak classifier h(x) weighted training data minimizing the error."""
    value:list = []
    ave:list[float] = []   # average
    x_len:int = len(x)
    for i in range(1,x_len):
        ave.append(['<',(x[i]+x[i-1])/2])  
        ave.append(['>',(x[i]+x[i-1])/2])  
        _error:int = 0
        for j in range(x_len):
            if (lambda a : -1 if a == 0 else 1)(x[j] < ave[-1][1]) != y[j]:_error+=p[j]
        _error_scale = _error
        value.append(_error_scale)
        value.append(1-_error_scale)
    index = value.index(min(value))
    # print(value)
    # print(ave)

    return ave[index], min(value)

def sign_of_h(x:list,alpha_avg_lists:list[list]):
    _result:list = []
    for n in range(len(x)):
        _total = 0
        for alpha_avg in alpha_avg_lists:
            a=I(x,alpha_avg[1][1],alpha_avg[1][0])
            _total += alpha_avg[0]*a[n]
        _result.append(sign(_total))
    return _result

def verify(x:list,y:list,alpha_avg_lists:list[list]) -> bool:
    """Verify the answer is correct."""
    for n,value in enumerate(sign_of_h(x,alpha_avg_lists)):
        if float(value) != y[n]:return False
    return True

### Define x value and y value.  ###
# X:list = [0,1,2,3,4,5,6,7,8,9]  #[1, 3, 9,11]
# Y:list = [1,1,1,-1,-1,-1,1,1,1,-1]  #[1,-1, 1,-1]
X:list = [1, 3, 9,11]
Y:list = [1,-1, 1,-1]

### Parameter default value. ###
W:list = weight([],count=len(X))
E:int = 1
COUNT:int = 1
alpha_avg_lists:list = []
_verify = False

### Start iterating. ###
while _verify == False:
    print(f"Iterate {COUNT}")
    AVG,E = error(X,Y,W)
    if E == 0 or COUNT>5:break
    A = alpha(E)
    W = weight(W,A,AVG)
    alpha_avg_lists.append([A,AVG])
    _verify = verify(X,Y,alpha_avg_lists)
    print(f"AVG={AVG}, E={E},  A={A}, verify={_verify}\nW={W}\n")
    COUNT+=1
