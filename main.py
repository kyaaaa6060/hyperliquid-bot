import requests

url = "https://api.hyperliquid.info/info"
headers = {"Content-Type": "application/json"}
data = {"type": "metaAndAssetCtxs"}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    
    universe = result[0]["universe"] 
    asset_contexts = result[1]      
    
    for i in range(min(5, len(universe))):
        coin_name = universe[i]["name"]
        ctx = asset_contexts[i]
        
        open_interest = ctx.get("openInterest", "Bilinmiyor")
        funding_rate = ctx.get("funding", "Bilinmiyor")
        
        print(f"Coin: {coin_name}")
        print(f"-> Açık Toplam Pozisyon (OI): {open_interest}")
        print(f"-> Fonlama Oranı (Funding): {funding_rate}")
        print("-" * 30)
else:
    print(f"Hata: {response.status_code}")
