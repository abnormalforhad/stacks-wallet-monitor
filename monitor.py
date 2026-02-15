import requests
import time
from datetime import datetime

# The Stacks Blockchain API endpoint
BASE_URL = "https://api.mainnet.hiro.so"

# A target Stacks address to monitor (You can swap this for your own later)
# This is a known Stacks foundation address for demo purposes
TARGET_WALLET = "SP1P72Z37Z4326CE978X6DRKJ04D747558ZQVFDBA"

def get_stx_balance(address):
    """Fetches the STX balance for a given address."""
    url = f"{BASE_URL}/extended/v1/address/{address}/balances"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        stx_balance = int(data['stx']['balance']) / 1_000_000  # Convert micro-STX to STX
        return stx_balance
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

def main():
    print(f"--- Starting Stacks Wallet Monitor ---")
    print(f"Tracking Address: {TARGET_WALLET}")
    
    current_balance = get_stx_balance(TARGET_WALLET)
    
    if current_balance is not None:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Current Balance: {current_balance:,.2f} STX")
        
        # In a real bot, you would loop this to check for changes
        # while True:
        #    check_for_updates()
        #    time.sleep(60)
    else:
        print("Could not retrieve data. Check your API connection.")

if __name__ == "__main__":
    main()