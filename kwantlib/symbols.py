### Refinitiv symbols for futures ###

#### Commodities ####

# Oil & Energy
oil = [
    'CL', # WTI Crude Oil (NYMEX - CME) 
    # 'QM', # E-Mini Crude Oil (NYMEX - CME)
    'HO', # Heating Oil (NYMEX - CME)
    'LGO', # Gasoil (NYMEX - CME)
    'LCO', # Brent Crude Oil (ICE)
    'RB', # Gasoline (NYMEX - CME)
    # 'JKE', # Kerosene (Tokyo Commodity Exchange) ###
]

# European gas 

european_gas = [
    "NGLNM", # NBP UK Natural Gas (ICE Eu - NBP UK)
    "TFMBM", # TTF Dutch Natural Gas (ICE Eu - ENDEX)
]

us_gas = [
    "NG", # Henry Hub US Natural Gas (NYMEX - CME)
]

coal = [
    "ATWM", # Rotterdam Coal Futures (ICE Eu - ENDEX) ###
]

carbon = [
    "CFI2", # Carbon Emission Futures (ICE Eu - ENDEX) ###
]

energy = oil + european_gas + us_gas + coal + carbon

# Softs Commodities
cocoa = [
    "CC", # Cocoa (ICE Us)
    "LCC", # London Cocoa (ICE Eu)
]

coffee = [
    "KC", # Arabica Coffee (ICE US)
    "LRC", # Robusta Coffee (ICE Eu)
]

cotton = [
    "CT", # Cotton n°2 (ICE US)
    "TTA", # Cotton n°2 (NYMEX - CME) ###
]

sugar = [
    "SB", # Sugar n°11 - Raw Sugar (ICE US)
    "LSU", # Sugar n°5 - White Sugar (ICE Eu)
    "SFS", # Sugar n°16 (ICE US) ###
]

ethanol = [
    "CUU", # Chicago Ethanol (NYMEX - CME) ###
    "AEZ", # Ethanol (CBOT - CME) ###
    # "ETH", # BMF Ethanol (BMF - Sao Paulo Exchange) ###
]

lumber = [
    "LXR", # Lumber (CME) ###
]

softs = cocoa + coffee + cotton + sugar + ethanol + lumber

# Agricultural Commodities

vegoil = [
    "FCPO", # Palm Oil Malaysia (Bursa Malaysia BMD) 
    "CPO", # Palm Oil US (CME)
    "BO", # Soybean Oil (CBOT - CME)
    "SM", # Soybean Meal (CBOT - CME)
    "RS", # Canola (ICE US) 

    # "NSO", # Refined Soybean Oil (Indian Exchange) ###
]

wheat = [
    "W", # Chicago Wheat (CBOT - CME)
    "KW", # Kansas Wheat (CBOT - CME)
    # "BL2", # Euronext Milling Wheat (Euronext)
    # "LWB", # Europe Wheat (ICE Eu) ###
]

soybeans = [
    "S", # Soybeans (CBOT - CME)
]

corn = [
    "C", # Corn (CBOT - CME)
    # "EMA", # Corn (MATIF - Euronext) ###
    # "MCR", # Corn (ROFEX - Rosario future Exchange) ###
]

rice = [
    "RR", # Rice (ICE US)
]

grains = wheat + soybeans + corn + rice

# Livestock & Dairy

livestock = [
    "LH", # Lean Hogs (CME) 
    "FC", # Feeder Cattle (CME)
    "LC", # Live Cattle (CME)
]

dairy = [
    "DCS", # Class III Milk (CME) ###
    "NF", # Nonfat Dry Milk (CME) ###
    "DK", # Class IV Milk (CME) ###
]

orange_juice = [
    "OJ", # Orange Juice (ICE) ###
]

# Metals

cme_metals = [    
    "HG", # Copper (COMEX - CME)
]

lme_metals = [
    # "AL", # Aluminium (LME)
    # "CO", # Copper (LME)
    # "ZN", # Zinc (LME)
    # "PB", # Lead (LME)
    # "NI", # Nickel (LME)
]

metals = cme_metals + lme_metals

commodities = energy + softs + vegoil + grains + livestock + dairy + metals 

#### Precious Metals ####

precious = [
    "GC", # Gold (COMEX - CME)
    "SI", # Silver (COMEX - CME)
    "PA", # Palladium (COMEX - CME)
    "PL", # Platinum (COMEX - CME)
]

#### Equity Futures ####

us_equity = [
    "ES", # E-mini S&P 500 (CME)
    "NQ", # E-mini Nasdaq-100 (CME)
    "YM", # E-mini Dow Jones (CBOE - CME)
    "RTY", # E-mini Russell 2000 (CME)
]

european_equity = [
    "STXE", # Euro Stoxx 50 (Eurex)
    # "FXXP", # Stoxx Europe 600 Banks (Eurex) 
    # "FDX", # DAX 40 (Eurex)
    # "FCE", # CAC 40 (Euronext)
    # "FFI", # FTSE 100 (ICE Eu)
]

asian_equity = [
    "NIY", # Nikkei 225 Japan (CME)
    "GIF", # Nifty 50 Index Futures (NSE India - National Stock Exchange)
    "KS", # KOSPI 200 Index Futures (KRX - Korea)
    # "TX", # TAIEX Index Futures (TAIFEX - Taiwan)
    # "YAF", # ASX 200 Index Futures (ASX - Sydney)
]

brazil_equity = [
    # "FMBZ", # MSCI Brazil Index Futures (Eurex)
    "IND", # BOVESPA Index Futures (BMF - Sao Paulo Exchange)
]

equity = (
    us_equity 
    + european_equity 
    + asian_equity 
    + brazil_equity 
)

# #### Bonds ####

us_bonds = [
    "TY", # 10-Year T-Note (CBOT - CME)
    "FV", # 5-Year T-Note (CBOT - CME)
    "TU", # 2-Year T-Note (CBOT - CME)
#     "ZB", # 30-Year T-Bond (CBOT - CME)
#     "UB", # Ultra T-Bond (CBOT - CME)
#     "GE", # Eurodollar Futures (CME)
#     "SR3", # SOFR Futures (CME)
]

european_bonds = [
    "FGBL", # Euro-Bund (10Y German) (Eurex)
#     "FGBM", # Euro-Bobl (5Y German) (Eurex)
#     "FGBS", # Euro-Schatz (2Y German) (Eurex)
#     "FBTP", # Euro-BTP (10Y Italian) (Eurex)
#     "OE1", # OAT 10Y French Government Bond (Eurex) ###
]

japan_bonds = [
#     "JB", # 10-Year Japanese Government Bond (JGB) Futures (JPX - Osaka Exchange)
#     "2JGB", # 2-Year JGB Futures (JPX - Osaka Exchange) ###
#     "5JGB", # 5-Year JGB Futures (JPX - Osaka Exchange) ###
#     "20JGB", # 20-Year JGB Futures (JPX - Osaka Exchange) ###
]

korea_bonds = [
#     "KTB3", # 3-Year Korea Treasury Bond Futures (KRX - Korea Exchange)
#     "KTB5", # 5-Year Korea Treasury Bond Futures (KRX - Korea Exchange)
#     "KTB10", # 10-Year Korea Treasury Bond Futures (KRX - Korea Exchange)
]

taiwan_bonds = [
#     "GBF", # 10-Year Government Bond Futures (TAIFEX - Taiwan Futures Exchange)
#     "GBF5", # 5-Year Government Bond Futures (TAIFEX - Taiwan Futures Exchange) ###
]

india_bonds = [
#     "IN10", # 10-Year Government Bond Futures (NSE India - National Stock Exchange)
#     "IN6", # 6-Year Government Bond Futures (NSE India) ###
]

australia_bonds = [
#     "YM", # 3-Year Australian Government Bond Futures (ASX - Sydney Futures Exchange)
#     "XM", # 10-Year Australian Government Bond Futures (ASX - Sydney Futures Exchange)
#     "XT", # 20-Year Treasury Bond Futures (ASX - Sydney Futures Exchange) ###
]

bonds = us_bonds + european_bonds + japan_bonds + korea_bonds + taiwan_bonds + india_bonds + australia_bonds


#### VIX ####

vix = [
    "VX", # Volatility Index Futures (CBOE - CME)
]

#### Crypto Futures ####

crypto = [
    "BTC", # Bitcoin Futures (CME)
    "FETE", # Ethereum Futures (CME)
]

#### Dollars Index Futures ####

dollars = [
    "DX", # US Dollar Index Futures (CME)
    # "ED", # Euro Dollar Futures (CME)
]

currencies = [
    # "JY", # Japanese Yen Futures (CME)
    # "BP", # British Pound Futures (CME)
    # "AD", # Australian Dollar Futures (CME)
    # "CD", # Canadian Dollar Futures (CME)
    # "SF", # Swiss Franc Futures (CME)
]

futures = (
    commodities + precious + equity + bonds + vix + crypto + dollars + currencies
)