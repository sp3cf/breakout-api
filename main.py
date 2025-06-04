from fastapi import FastAPI
from breakout_scanner import find_breakout_candidates

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Breakout API is running"}

@app.get("/scan")
def scan():
    tickers = ['AAPL', 'MSFT', 'TSLA', 'AMZN', 'NVDA', 'META']
    result = find_breakout_candidates(tickers)
    return {"breakouts": result}
