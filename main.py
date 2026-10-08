import requests

url = "https://api.hyperliquid.info/info"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
payload = {"type": "metaAndAssetCtxs"}

try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        universe = data[0]["universe"]
        asset_contexts = data[1]
        
        for name, ctx in zip([u["name"] for u in universe][:10], asset_contexts[:10]):
            oi = float(ctx.get('openInterest', 0))
            funding = float(ctx.get('funding', 0))
            print(f"Coin: {name} | OI: {oi:.2f} | Funding: {funding:.6f}")
    else:
        print(f"Hata Kodu: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Hata oluştu: {e}")
