import pandas as pd
import json
import os
from datetime import datetime

DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

def load_lotteries():
    return [
        {"id": "powerball", "name": "US Powerball", "format": "5/69 + 1/26", "odds": "1 in 292M", "provider": "Lottoland"},
        {"id": "euromillions", "name": "EuroMillions", "format": "5/50 + 2/12", "odds": "1 in 139M", "provider": "Lottoland"},
        {"id": "megamillions", "name": "US Mega Millions", "format": "5/70 + 1/25", "odds": "1 in 302M", "provider": "Lottoland"},
        {"id": "chispazo", "name": "Chispazo Mexico", "format": "5/28", "odds": "1 in 98,280", "provider": "Pronosticos"},
        {"id": "mini_lotto", "name": "Japan Mini Lotto", "format": "5/31 + Bonus", "odds": "1 in 169,911", "provider": "Takarakuji"},
    ]

def get_draw_history(lot_id):
    path = f'{DATA_DIR}/{lot_id}_history.csv'
    if os.path.exists(path):
        df = pd.read_csv(path)
        df['date'] = pd.to_datetime(df['date'])
        return df.sort_values('date', ascending=False)
    # Demo fallback
    demos = {
        'chispazo': pd.DataFrame([{'date':'2026-07-15','numbers':'[3,7,14,22,28]','bonus':None}]),
        'mini_lotto': pd.DataFrame([{'date':'2026-07-14','numbers':'[4,11,19,25,30]','bonus':15}]),
    }
    return demos.get(lot_id, pd.DataFrame(columns=['date','numbers','bonus']))

def save_prediction(lot_id, pred, method):
    log_path = f'{DATA_DIR}/predictions.json'
    logs = json.load(open(log_path)) if os.path.exists(log_path) else []
    logs.append({"lot_id": lot_id, "pred": pred, "method": method, "ts": datetime.now().isoformat()})
    with open(log_path, 'w') as f:
        json.dump(logs, f, indent=2)
