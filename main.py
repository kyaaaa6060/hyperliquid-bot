import requests

def get_hyperliquid_signals():
    url = "https://api.hyperliquid.info/info"
    headers = {"Content-Type": "application/json"}
    data = {"type": "metaAndAssetCtxs"}

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            print(f"API Hatası: {response.status_code}")
            return

        result = response.json()
        universe = result[0]["universe"]
        asset_contexts = result[1]

        print("=== HYPERLIQUID AÇIK POZİSYON VE PİYASA ANALİZİ ===")
        print(f"Toplam İncelenen Varlık Sayısı: {len(universe)}\n")

        # İlk 10 coini örnek olarak analize alalım
        for i in range(min(10, len(universe))):
            coin_name = universe[i]["name"]
            ctx = asset_contexts[i]
            
            # Verileri çekelim (gelmeyen veriler için varsayılan 0)
            open_interest = float(ctx.get("openInterest", 0))
            funding_rate = float(ctx.get("funding", 0))
            
            # Basit bir sinyal/tavsiye mantığı üretelim
            # Fonlama oranı yıllık veya anlık bazda pozitifse longlar baskın demektir
            signal = "Nötr / Dengeli"
            if funding_rate > 0.0005:
                signal = "Aşırı Long Baskısı (Düzeltme/Long Squeeze Riski Var)"
            elif funding_rate < -0.0002:
                signal = "Aşırı Short Baskısı (Short Squeeze Riski Var)"

            print(f"Coin: {coin_name}")
            print(f"  -> Açık Pozisyon (OI): {open_interest:.2f}")
            print(f"  -> Fonlama Oranı (Funding): {funding_rate:.6f}")
            print(f"  -> Piyasa Durumu / Tavsiye Sinyali: {signal}")
            print("-" * 50)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    get_hyperliquid_signals()
