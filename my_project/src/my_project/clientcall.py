# mech_superforcaster_request.py

from mech_client.marketplace_interact import marketplace_interact

# === Configuration ===
PROMPT_TEXT = "Will the Federal Reserve lower interest rates before October 2025?"
CHAIN_CONFIG = "gnosis"
TOOL_NAME = "superforcaster"
PRIORITY_MECH_ADDRESS = "0x77af31de935740567cf4ff1986d04b2c964a786a" 
USE_OFFCHAIN = False 

# === Run Mech interaction ===
if __name__ == "__main__":
    print("Sending request to Mech Marketplace...")
    try:
        result = marketplace_interact(
            prompt=PROMPT_TEXT,
            priority_mech=PRIORITY_MECH_ADDRESS,
            use_offchain=USE_OFFCHAIN,
            tool=TOOL_NAME,
            chain_config=CHAIN_CONFIG
        )
        print("Mech response received:")
        print(result)
    except Exception as e:
        print(f"Error during Mech interaction: {e}")
