def get_stock_data(ticker, start_date, end_date):
    """
    Retrieve historical stock data for a specific ticker.
    
    Parameters:
    - ticker (str): Stock ticker symbol
    - start_date (str): Start date in YYYY-MM-DD format
    - end_date (str): End date in YYYY-MM-DD format
    
    Returns:
    - dict: Dictionary containing stock data
    """
    # Simulated stock data
    import random
    from datetime import datetime, timedelta
    
    stock_info = {
        "AAPL": {
            "company_name": "Apple Inc.",
            "sector": "Technology",
            "industry": "Consumer Electronics"
        },
        "MSFT": {
            "company_name": "Microsoft Corporation",
            "sector": "Technology",
            "industry": "Software"
        },
        "GOOGL": {
            "company_name": "Alphabet Inc.",
            "sector": "Technology",
            "industry": "Internet Content & Information"
        },
        "AMZN": {
            "company_name": "Amazon.com, Inc.",
            "sector": "Consumer Cyclical",
            "industry": "Internet Retail"
        },
        "TSLA": {
            "company_name": "Tesla, Inc.",
            "sector": "Consumer Cyclical",
            "industry": "Auto Manufacturers"
        }
    }
    
    if ticker not in stock_info:
        return {
            "error": f"Ticker {ticker} not found",
            "ticker": ticker,
            "company_name": "",
            "data": [],
            "summary": {}
        }
    
    # Generate simulated data
    data = []
    base_prices = {
        "AAPL": 180.0,
        "MSFT": 360.0,
        "GOOGL": 140.0,
        "AMZN": 170.0,
        "TSLA": 240.0
    }
    
    current_price = base_prices.get(ticker, 100.0)
    volatility = {
        "AAPL": 0.015,
        "MSFT": 0.018,
        "GOOGL": 0.022,
        "AMZN": 0.025,
        "TSLA": 0.035
    }
    
    current_volatility = volatility.get(ticker, 0.02)
    
    # Parse dates
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        current_date = start
        
        while current_date <= end:
            # Skip weekends
            if current_date.weekday() < 5:  # 0-4 are Monday to Friday
                # Daily random variation
                daily_change = random.normalvariate(0, current_volatility)
                price_change = current_price * daily_change
                
                # Generate day's prices
                open_price = current_price
                close_price = current_price + price_change
                high_price = max(open_price, close_price) * (1 + random.uniform(0, 0.01))
                low_price = min(open_price, close_price) * (1 - random.uniform(0, 0.01))
                
                # Generate volume
                base_volume = {
                    "AAPL": 80000000,
                    "MSFT": 25000000,
                    "GOOGL": 15000000,
                    "AMZN": 35000000,
                    "TSLA": 100000000
                }
                volume = int(base_volume.get(ticker, 20000000) * (1 + random.uniform(-0.3, 0.5)))
                
                data.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "open": round(open_price, 2),
                    "high": round(high_price, 2),
                    "low": round(low_price, 2),
                    "close": round(close_price, 2),
                    "volume": volume
                })
                
                current_price = close_price
            
            current_date += timedelta(days=1)
    except ValueError:
        return {
            "error": "Invalid date format. Use YYYY-MM-DD.",
            "ticker": ticker,
            "company_name": "",
            "data": [],
            "summary": {}
        }
    
    # Calculate summary statistics
    if data:
        closes = [day["close"] for day in data]
        highs = [day["high"] for day in data]
        lows = [day["low"] for day in data]
        volumes = [day["volume"] for day in data]
        
        summary = {
            "start_price": data[0]["open"],
            "end_price": data[-1]["close"],
            "period_change": round((data[-1]["close"] - data[0]["open"]) / data[0]["open"] * 100, 2),
            "average_price": round(sum(closes) / len(closes), 2),
            "highest_price": round(max(highs), 2),
            "lowest_price": round(min(lows), 2),
            "average_volume": int(sum(volumes) / len(volumes))
        }
    else:
        summary = {}
    
    return {
        "ticker": ticker,
        "company_name": stock_info[ticker]["company_name"],
        "sector": stock_info[ticker]["sector"],
        "industry": stock_info[ticker]["industry"],
        "data": data,
        "summary": summary
    }

def get_market_indicators(date):
    """
    Get market indicators for a specific date.
    
    Parameters:
    - date (str): Date in YYYY-MM-DD format
    
    Returns:
    - dict: Dictionary containing market indicators
    """
    # Simulated market data
    import random
    from datetime import datetime
    
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return {
            "error": "Invalid date format. Use YYYY-MM-DD.",
            "date": date,
            "indices": {},
            "metrics": {},
            "sectors": {}
        }
    
    # Generate simulated data based on market sentiment
    market_sentiment = random.normalvariate(0, 1)  # Normal distribution around 0
    
    indices = {
        "S&P 500": round(4700 * (1 + market_sentiment * 0.01), 2),
        "Dow Jones": round(36500 * (1 + market_sentiment * 0.008), 2),
        "NASDAQ": round(16200 * (1 + market_sentiment * 0.012), 2),
        "Russell 2000": round(2100 * (1 + market_sentiment * 0.015), 2),
        "VIX": round(max(10, 18 - market_sentiment * 3), 2)
    }
    
    metrics = {
        "market_breadth": round(0.5 + market_sentiment * 0.1, 2),
        "put_call_ratio": round(max(0.7, 1.0 - market_sentiment * 0.1), 2),
        "10y_treasury": round(max(1.5, 3.5 - market_sentiment * 0.2), 2),
        "average_volume": int(8500000000 * (1 + abs(market_sentiment) * 0.2))
    }
    
    # Sector performance varies based on market sentiment
    sectors = {
        "Technology": round(market_sentiment * 1.2, 2),
        "Healthcare": round(market_sentiment * 0.8, 2),
        "Financials": round(market_sentiment * 1.0, 2),
        "Consumer Discretionary": round(market_sentiment * 1.1, 2),
        "Consumer Staples": round(market_sentiment * 0.5, 2),
        "Energy": round(market_sentiment * 1.3, 2),
        "Utilities": round(market_sentiment * 0.4, 2),
        "Materials": round(market_sentiment * 0.9, 2),
        "Industrials": round(market_sentiment * 1.0, 2),
        "Real Estate": round(market_sentiment * 0.7, 2)
    }
    
    # Add some random variation to sectors
    for sector in sectors:
        sectors[sector] = round(sectors[sector] + random.normalvariate(0, 0.5), 2)
    
    return {
        "date": date,
        "indices": indices,
        "metrics": metrics,
        "sectors": sectors
    }

def calculate_portfolio_metrics(holdings):
    """
    Calculate metrics for a given portfolio.
    
    Parameters:
    - holdings (list): List of dictionaries with ticker, shares, and purchase_price
    
    Returns:
    - dict: Dictionary containing portfolio metrics
    """
    # Simulated current prices
    current_prices = {
        "AAPL": 182.63,
        "MSFT": 374.51,
        "GOOGL": 143.96,
        "AMZN": 185.07,
        "TSLA": 237.49,
        "JPM": 195.83,
        "JNJ": 147.58,
        "PG": 165.74,
        "V": 275.54,
        "XOM": 116.85
    }
    
    # Simulated sector information
    sector_info = {
        "AAPL": "Technology",
        "MSFT": "Technology",
        "GOOGL": "Technology",
        "AMZN": "Consumer Cyclical",
        "TSLA": "Consumer Cyclical",
        "JPM": "Financial Services",
        "JNJ": "Healthcare",
        "PG": "Consumer Defensive",
        "V": "Financial Services",
        "XOM": "Energy"
    }
    
    # Risk metrics per ticker (beta, volatility)
    risk_info = {
        "AAPL": {"beta": 1.2, "volatility": 0.22},
        "MSFT": {"beta": 1.1, "volatility": 0.20},
        "GOOGL": {"beta": 1.3, "volatility": 0.25},
        "AMZN": {"beta": 1.4, "volatility": 0.28},
        "TSLA": {"beta": 2.1, "volatility": 0.45},
        "JPM": {"beta": 1.1, "volatility": 0.18},
        "JNJ": {"beta": 0.7, "volatility": 0.15},
        "PG": {"beta": 0.6, "volatility": 0.12},
        "V": {"beta": 1.0, "volatility": 0.17},
        "XOM": {"beta": 0.9, "volatility": 0.19}
    }
    
    # Process holdings
    total_value = 0
    total_cost = 0
    sector_values = {}
    portfolio_risk = {"beta": 0, "volatility": 0}
    holdings_performance = []
    
    for holding in holdings:
        ticker = holding.get("ticker", "")
        shares = holding.get("shares", 0)
        purchase_price = holding.get("purchase_price", 0)
        
        if ticker not in current_prices:
            continue
        
        # Calculate values
        current_price = current_prices[ticker]
        current_value = shares * current_price
        cost_basis = shares * purchase_price
        gain_loss = current_value - cost_basis
        
        total_value += current_value
        total_cost += cost_basis
        
        # Add to holdings performance
        holdings_performance.append({
            "ticker": ticker,
            "shares": shares,
            "purchase_price": purchase_price,
            "current_price": current_price,
            "current_value": current_value,
            "gain_loss": gain_loss,
            "percent_gain_loss": round((current_price - purchase_price) / purchase_price * 100, 2)
        })
        
        # Calculate sector allocation
        if ticker in sector_info:
            sector = sector_info[ticker]
            if sector not in sector_values:
                sector_values[sector] = 0
            sector_values[sector] += current_value
        
        # Calculate risk contribution
        if ticker in risk_info:
            weight = current_value / (total_value or 1)  # Avoid division by zero
            portfolio_risk["beta"] += weight * risk_info[ticker]["beta"]
            portfolio_risk["volatility"] += weight * risk_info[ticker]["volatility"]
    
    # Calculate gain/loss
    total_gain_loss = total_value - total_cost
    percent_gain_loss = (total_gain_loss / total_cost * 100) if total_cost > 0 else 0
    
    # Calculate sector allocation percentages
    sector_allocation = {}
    for sector, value in sector_values.items():
        sector_allocation[sector] = round(value / total_value * 100, 2)
    
    # Additional risk metrics
    risk_metrics = {
        "beta": round(portfolio_risk["beta"], 2),
        "volatility": round(portfolio_risk["volatility"], 2),
        "sharpe_ratio": round((percent_gain_loss / 100) / (portfolio_risk["volatility"] or 1), 2),
        "diversification_score": round(min(100, len(holdings) / 20 * 100), 2)
    }
    
    return {
        "total_value": round(total_value, 2),
        "total_cost": round(total_cost, 2),
        "total_gain_loss": round(total_gain_loss, 2),
        "percent_gain_loss": round(percent_gain_loss, 2),
        "sector_allocation": sector_allocation,
        "risk_metrics": risk_metrics,
        "holdings_performance": holdings_performance
    }