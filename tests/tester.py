import numpy as np, pandas as pd, sympy as sy
import scipy.integrate as si
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def test_numpy():
    a=np.arange(100)
    assert np.sum(a)==sum(a)

def test_scipy():
    val,_=si.quad(lambda x:x*x,0,6)
    assert abs(val-72.0)<1e-6

def test_pandas():
    s=pd.Series(range(10))
    assert s.size==10

def test_sympy():
    x=sy.Symbol('x')
    assert sy.diff(x**2,x)==2*x

def test_matplotlib(tmp_path):
    p=tmp_path/"fig.png"
    plt.plot([0,1],[0,1]); plt.savefig(p)
    assert p.exists()
