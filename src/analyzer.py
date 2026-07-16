import pandas as pd
import numpy as np

def analyze_lottery(hist_df, lottery):
    numbers = []
    for n in hist_df['numbers']:
        numbers.extend(eval(n) if isinstance(n, str) else n)
    freq = pd.Series(numbers).value_counts()
    
    max_n = 31 if 'mini' in lottery['id'] else 28 if 'chispazo' in lottery['id'] else 69
    gs = max_n // 3
    groups = {}
    for i in range(3):
        groups[f"G{i+1} ({i*gs+1}-{(i+1)*gs})"] = freq[(freq.index >= i*gs+1) & (freq.index <= (i+1)*gs)].sum()
    return {"groups": groups, "freq": freq.to_dict()}

def predict_numbers(hist, lot, method='statistical'):
    if hist.empty: return {"main": [1,2,3,4,5]}
    analysis = analyze_lottery(hist, lot)
    hot = sorted(pd.Series(analysis['freq']).nlargest(5).index.tolist())
    if method == 'statistical':
        return {"main": hot, "bonus": [np.random.randint(1,20)]}
    return {"main": hot[:3] + [np.random.randint(1,30) for _ in range(2)], "bonus": [np.random.randint(1,20)], "note": "60% hot + 40% random"}
