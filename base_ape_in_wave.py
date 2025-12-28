import requests, time
from collections import defaultdict

def ape_wave():
    print("Base — Ape In Wave (50+ small buys <$5k in <30 sec)")
    waves = defaultdict(int)

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/transactions/base?limit=500")
            now = time.time()

            for tx in r.json().get("transactions", []):
                if tx.get("side") != "buy" or tx.get("valueUSD", 0) > 5000:
                    continue

                pair = tx["pairAddress"]
                age = now - tx.get("timestamp", 0)
                if age > 30: continue

                waves[pair] += 1

                if waves[pair] >= 50:
                    token = tx["token0"]["symbol"] if "WETH" in tx["token1"]["symbol"] else tx["token1"]["symbol"]
                    print(f"APE WAVE INCOMING\n"
                          f"{token} — {waves[pair]} small buys in seconds\n"
                          f"https://dexscreener.com/base/{pair}\n"
                          f"→ Retail FOMO starting — volume about to explode\n"
                          f"{'APE'*30}")
                    del waves[pair]

        except:
            pass
        time.sleep(1.4)

if __name__ == "__main__":
    ape_wave()
