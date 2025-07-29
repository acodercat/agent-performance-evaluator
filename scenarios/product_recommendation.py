def get_products():
    """
    Get product list
    
    Returns:
    - list: List of products
    """
    # Simulated product data
    products = [
        {"id": "P001", "name": "Laptop Model A", "category": "Electronics", "price": 899, "stock": 10, "rating": 4.5},
        {"id": "P002", "name": "Smartphone Model B", "category": "Electronics", "price": 599, "stock": 25, "rating": 4.7},
        {"id": "P003", "name": "Wireless Headphones C", "category": "Electronics", "price": 129, "stock": 50, "rating": 4.3},
        {"id": "P004", "name": "Tablet Model D", "category": "Electronics", "price": 399, "stock": 15, "rating": 4.6},
        {"id": "P005", "name": "Coffee Maker E", "category": "Appliances", "price": 179, "stock": 8, "rating": 4.2},
        {"id": "P006", "name": "Vacuum Cleaner F", "category": "Appliances", "price": 249, "stock": 12, "rating": 4.4},
        {"id": "P007", "name": "Bluetooth Speaker G", "category": "Electronics", "price": 79, "stock": 30, "rating": 4.1},
        {"id": "P008", "name": "Rice Cooker H", "category": "Appliances", "price": 89, "stock": 20, "rating": 4.0},
        {"id": "P009", "name": "Smart Watch I", "category": "Electronics", "price": 199, "stock": 18, "rating": 4.2},
        {"id": "P010", "name": "Blender J", "category": "Appliances", "price": 69, "stock": 0, "rating": 3.9}
    ]
    
    return products

def filter_products(category=None, max_price=None, in_stock=None, min_rating=None):
    """
    Filter products based on criteria
    
    Parameters:
    - category (str): Product category filter
    - max_price (int): Maximum price filter
    - in_stock (bool): Filter for in-stock items only
    - min_rating (float): Minimum rating filter
    
    Returns:
    - list: Filtered products
    """
    products = get_products()
    filtered = products.copy()
    
    # Apply filters
    if category:
        filtered = [p for p in filtered if p["category"] == category]
    
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    
    if in_stock:
        filtered = [p for p in filtered if p["stock"] > 0]
    
    if min_rating is not None:
        filtered = [p for p in filtered if p["rating"] >= min_rating]
    
    return filtered

def get_product_recommendations(budget, preferences):
    """
    Get personalized product recommendations based on budget and preferences
    
    Parameters:
    - budget (int): Customer's budget
    - preferences (dict): Customer preferences including preferred categories and features
    
    Returns:
    - dict: Personalized recommendations
    """
    all_products = get_products()
    
    # Extract preferences
    preferred_categories = preferences.get("categories", [])
    min_rating = preferences.get("min_rating", 4.0)
    
    # Filter products within budget and in stock
    affordable_products = [p for p in all_products if p["price"] <= budget and p["stock"] > 0]
    
    # Filter by preferred categories if specified
    if preferred_categories:
        category_matches = [p for p in affordable_products if p["category"] in preferred_categories]
        # If no matches in preferred categories, fall back to all affordable products
        recommendations = category_matches if category_matches else affordable_products
    else:
        recommendations = affordable_products
    
    # Sort by rating
    recommendations.sort(key=lambda p: p["rating"], reverse=True)
    
    # Get top recommendations
    top_picks = recommendations[:3] if len(recommendations) >= 3 else recommendations
    
    # Get budget-friendly options
    budget_options = sorted([p for p in affordable_products if p["rating"] >= min_rating], 
                           key=lambda p: p["price"])[:3]
    
    return {
        "top_recommendations": top_picks,
        "budget_friendly_options": budget_options,
        "total_matches": len(recommendations)
    }