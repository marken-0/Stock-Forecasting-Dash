import yfinance as yf
import pandas as pd

def update_header(n_clicks, stock_name):
    if n_clicks > 0:
        stock = yf.Ticker(stock_name)
        info = stock.info
        # print(info)
        # print(info['logo_url'])
        df = pd.DataFrame().from_dict(info, orient="index").T
        domain = df['website'].values[0]
        print(domain)
        logo_url = f"https://logo.clearbit.com/{domain}"
        print(logo_url)
        # return [
        #     print(src=info['logo_url'], className="logo"),
        #     print(info['shortName'])
        # ]
    
update_header(1, 'AAPL')