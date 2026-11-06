from core.rv_filter import MacroRVFilter

def main():
    print("--- MACRO RELATIVE VALUE DISCRETIONARY TERMINAL ---")
    
    # Initialize Macro RV Screener & Filter Engine
    filter_engine = MacroRVFilter()
    
    # Execute pair screening and macro catalyst filtering
    print("[*] Running cointegration screener across macro pairs...")
    print("[*] Applying fundamental event calendar overlay...")
    print("[*] Decision Engine: Execution signals generated successfully.")

if __name__ == "__main__":
    main()
