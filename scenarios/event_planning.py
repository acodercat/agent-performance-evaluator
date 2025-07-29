def get_weather_forecast(location, date):
    """
    Get weather forecast for a specific location and date.
    
    Parameters:
    - location (str): City name or coordinates
    - date (str): Date in YYYY-MM-DD format
    
    Returns:
    - dict: Dictionary containing weather forecast information
    """
    # Simulated weather data
    import random
    from datetime import datetime
    
    weather_patterns = {
        "New York": {"baseline_temp": 15, "precipitation_chance": 0.3, "humidity": 65},
        "Los Angeles": {"baseline_temp": 24, "precipitation_chance": 0.1, "humidity": 50},
        "Chicago": {"baseline_temp": 12, "precipitation_chance": 0.35, "humidity": 70},
        "Miami": {"baseline_temp": 28, "precipitation_chance": 0.4, "humidity": 75},
        "Seattle": {"baseline_temp": 14, "precipitation_chance": 0.6, "humidity": 80},
        "Austin": {"baseline_temp": 26, "precipitation_chance": 0.25, "humidity": 55},
        "Denver": {"baseline_temp": 16, "precipitation_chance": 0.3, "humidity": 45},
        "Boston": {"baseline_temp": 13, "precipitation_chance": 0.35, "humidity": 65},
        "San Francisco": {"baseline_temp": 17, "precipitation_chance": 0.2, "humidity": 75},
        "Washington DC": {"baseline_temp": 16, "precipitation_chance": 0.3, "humidity": 60},
    }
    
    # Default values for unknown locations
    default_weather = {"baseline_temp": 20, "precipitation_chance": 0.3, "humidity": 60}
    
    # Parse the date
    try:
        forecast_date = datetime.strptime(date, "%Y-%m-%d")
        days_ahead = (forecast_date - datetime.now()).days
        
        # Limit forecast to 10 days ahead
        if days_ahead < 0 or days_ahead > 10:
            return {
                "error": "Forecast only available for the next 10 days",
                "location": location,
                "date": date,
                "forecast": {}
            }
    except ValueError:
        return {
            "error": "Invalid date format. Use YYYY-MM-DD.",
            "location": location,
            "date": date,
            "forecast": {}
        }
    
    # Get baseline data for location
    weather_base = weather_patterns.get(location, default_weather)
    
    # Adjust forecast based on days ahead (more random variation the further out)
    forecast_certainty = max(0.4, 1 - (days_ahead * 0.06))
    temp_variance = 5 + (days_ahead * 0.5)
    precip_variance = 0.1 + (days_ahead * 0.02)
    
    # Generate daily forecast with seasonal adjustments
    month = forecast_date.month
    # Simple seasonal adjustment in Northern Hemisphere
    seasonal_temp_adj = -5 if 11 <= month <= 12 or 1 <= month <= 3 else 5 if 5 <= month <= 9 else 0
    
    # Apply randomization while respecting climate patterns
    temp = weather_base["baseline_temp"] + seasonal_temp_adj + random.uniform(-temp_variance, temp_variance)
    
    # Precipitation more likely with higher humidity
    precipitation_chance = min(0.95, max(0.05, 
        weather_base["precipitation_chance"] + random.uniform(-precip_variance, precip_variance)))
    
    # Determine weather condition based on precipitation chance
    if precipitation_chance > 0.7:
        conditions = random.choice(["Heavy Rain", "Thunderstorms", "Showers"])
    elif precipitation_chance > 0.4:
        conditions = random.choice(["Light Rain", "Scattered Showers", "Overcast"])
    elif precipitation_chance > 0.2:
        conditions = random.choice(["Partly Cloudy", "Mostly Cloudy", "Cloudy"])
    else:
        conditions = random.choice(["Sunny", "Clear", "Mostly Sunny"])
    
    # Adjust for snow in winter months with low temperatures
    if (month <= 2 or month >= 11) and temp < 2 and precipitation_chance > 0.3:
        conditions = random.choice(["Snow", "Light Snow", "Snow Showers"])
    
    # Add daily high and low
    temp_high = temp + random.uniform(2, 5)
    temp_low = temp - random.uniform(2, 6)
    
    # Wind speed - correlate somewhat with conditions
    wind_speed = 5 + random.uniform(0, 15)
    if "Rain" in conditions or "Storm" in conditions or "Snow" in conditions:
        wind_speed += random.uniform(5, 10)
    
    forecast = {
        "date": date,
        "condition": conditions,
        "temperature": {
            "high": round(temp_high, 1),
            "low": round(temp_low, 1),
            "average": round(temp, 1)
        },
        "precipitation": {
            "chance": round(precipitation_chance * 100),
            "amount": round(precipitation_chance * random.uniform(0, 30), 1) if precipitation_chance > 0.2 else 0
        },
        "humidity": round(weather_base["humidity"] + random.uniform(-10, 10)),
        "wind": {
            "speed": round(wind_speed, 1),
            "direction": random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"])
        },
        "forecast_certainty": round(forecast_certainty * 100)
    }
    
    return {
        "location": location,
        "date": date,
        "forecast": forecast
    }

def get_venues(location, venue_type, capacity_min=0, capacity_max=10000, indoor=None):
    """
    Get venues in a location based on type and capacity.
    
    Parameters:
    - location (str): City name
    - venue_type (str): Type of venue (e.g., "restaurant", "conference", "outdoor", "wedding")
    - capacity_min (int): Minimum capacity
    - capacity_max (int): Maximum capacity
    - indoor (bool): True for indoor venues, False for outdoor venues, None for both
    
    Returns:
    - list: List of venue dictionaries
    """
    # Simulated venue database
    all_venues = {
        "New York": [
            {"name": "Central Park Pavilion", "type": "outdoor", "capacity": 500, "indoor": False, "cost_per_hour": 1500, "rating": 4.5, "available_facilities": ["stage", "seating", "lighting"]},
            {"name": "Manhattan Grand Hotel", "type": "conference", "capacity": 800, "indoor": True, "cost_per_hour": 3000, "rating": 4.7, "available_facilities": ["AV equipment", "catering", "wifi"]},
            {"name": "Brooklyn Brewery Hall", "type": "restaurant", "capacity": 150, "indoor": True, "cost_per_hour": 1200, "rating": 4.3, "available_facilities": ["bar", "kitchen", "sound system"]},
            {"name": "Hudson River Plaza", "type": "outdoor", "capacity": 1000, "indoor": False, "cost_per_hour": 2500, "rating": 4.2, "available_facilities": ["stage", "riverside view", "power outlets"]},
            {"name": "Tribeca Loft", "type": "wedding", "capacity": 200, "indoor": True, "cost_per_hour": 2000, "rating": 4.6, "available_facilities": ["dance floor", "kitchen", "bar"]}
        ],
        "Los Angeles": [
            {"name": "Malibu Beach Club", "type": "outdoor", "capacity": 300, "indoor": False, "cost_per_hour": 2800, "rating": 4.8, "available_facilities": ["beach access", "bar", "sound system"]},
            {"name": "Hollywood Hills Mansion", "type": "wedding", "capacity": 120, "indoor": True, "cost_per_hour": 3500, "rating": 4.9, "available_facilities": ["pool", "garden", "catering kitchen"]},
            {"name": "Downtown Conference Center", "type": "conference", "capacity": 1000, "indoor": True, "cost_per_hour": 2500, "rating": 4.4, "available_facilities": ["projectors", "sound system", "breakout rooms"]},
            {"name": "Griffith Observatory Gardens", "type": "outdoor", "capacity": 400, "indoor": False, "cost_per_hour": 1800, "rating": 4.7, "available_facilities": ["scenic view", "parking", "permit included"]},
            {"name": "Beverly Hills Ballroom", "type": "wedding", "capacity": 500, "indoor": True, "cost_per_hour": 4000, "rating": 4.8, "available_facilities": ["chandeliers", "dance floor", "grand piano"]}
        ],
        "Chicago": [
            {"name": "Lakefront Pavilion", "type": "outdoor", "capacity": 350, "indoor": False, "cost_per_hour": 1200, "rating": 4.3, "available_facilities": ["lake view", "covered area", "electricity"]},
            {"name": "Michigan Avenue Hotel", "type": "conference", "capacity": 750, "indoor": True, "cost_per_hour": 2800, "rating": 4.5, "available_facilities": ["business center", "catering", "AV equipment"]},
            {"name": "Wrigleyville Bar & Grill", "type": "restaurant", "capacity": 180, "indoor": True, "cost_per_hour": 900, "rating": 4.1, "available_facilities": ["sports bar", "kitchen", "TVs"]},
            {"name": "Millennium Park Event Space", "type": "outdoor", "capacity": 1200, "indoor": False, "cost_per_hour": 3000, "rating": 4.6, "available_facilities": ["iconic location", "stage area", "city views"]},
            {"name": "Historic Chicago Ballroom", "type": "wedding", "capacity": 300, "indoor": True, "cost_per_hour": 2500, "rating": 4.7, "available_facilities": ["vintage architecture", "dance floor", "grand staircase"]}
        ]
    }
    
    # Check if location exists in our database
    if location not in all_venues:
        return {
            "error": f"No venue information available for {location}",
            "venues": []
        }
    
    # Filter venues based on parameters
    filtered_venues = []
    for venue in all_venues[location]:
        # Check venue type (case insensitive)
        if venue_type.lower() != "any" and venue_type.lower() != venue["type"].lower():
            continue
        
        # Check capacity
        if venue["capacity"] < capacity_min or venue["capacity"] > capacity_max:
            continue
        
        # Check indoor/outdoor preference if specified
        if indoor is not None and venue["indoor"] != indoor:
            continue
        
        filtered_venues.append(venue)
    
    return {
        "location": location,
        "venue_type": venue_type,
        "venues": filtered_venues
    }

def check_venue_availability(venue_name, location, date):
    """
    Check if a specific venue is available on a given date.
    
    Parameters:
    - venue_name (str): Name of the venue
    - location (str): City name
    - date (str): Date in YYYY-MM-DD format
    
    Returns:
    - dict: Dictionary containing availability information
    """
    # Parse date
    try:
        from datetime import datetime
        event_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return {
            "error": "Invalid date format. Use YYYY-MM-DD.",
            "venue_name": venue_name,
            "location": location,
            "date": date,
            "available": False
        }
    
    # List of venues from get_venues function
    all_venues = {
        "New York": ["Central Park Pavilion", "Manhattan Grand Hotel", "Brooklyn Brewery Hall", "Hudson River Plaza", "Tribeca Loft"],
        "Los Angeles": ["Malibu Beach Club", "Hollywood Hills Mansion", "Downtown Conference Center", "Griffith Observatory Gardens", "Beverly Hills Ballroom"],
        "Chicago": ["Lakefront Pavilion", "Michigan Avenue Hotel", "Wrigleyville Bar & Grill", "Millennium Park Event Space", "Historic Chicago Ballroom"]
    }
    
    # Check if location exists and if venue exists in that location
    if location not in all_venues or venue_name not in all_venues[location]:
        return {
            "error": f"Venue {venue_name} not found in {location}",
            "venue_name": venue_name,
            "location": location,
            "date": date,
            "available": False
        }
    
    # Simulate availability - using deterministic algorithm based on date and venue name
    # This ensures consistent results for the same venue and date
    day_of_year = event_date.timetuple().tm_yday
    venue_index = all_venues[location].index(venue_name)
    
    # Algorithm to determine availability
    # - Some venues are generally more booked than others
    # - Weekends are more likely to be booked
    # - Summer months are more booked
    is_weekend = event_date.weekday() >= 5  # Saturday or Sunday
    is_summer = 5 <= event_date.month <= 8  # May to August
    
    # Base availability - higher number means more likely to be booked
    booking_likelihood = (venue_index * 7) % 10  # 0-9 based on venue
    
    # Adjust for weekends and summer
    if is_weekend:
        booking_likelihood += 4
    if is_summer:
        booking_likelihood += 3
    
    # Final deterministic calculation
    hash_value = (day_of_year + booking_likelihood + venue_index) % 10
    available = hash_value < 5  # 50% chance of availability
    
    # Format available time slots if venue is available
    available_times = []
    if available:
        # Simulate available time slots
        import random
        random.seed(hash_value + venue_index + day_of_year)  # Set seed for deterministic results
        
        # Common time slots
        all_slots = ["09:00-12:00", "12:00-15:00", "15:00-18:00", "18:00-21:00", "21:00-00:00"]
        
        # Randomly select available slots
        num_available = random.randint(1, len(all_slots))
        available_times = random.sample(all_slots, num_available)
        available_times.sort()
    
    return {
        "venue_name": venue_name,
        "location": location,
        "date": date,
        "available": available,
        "available_time_slots": available_times,
        "booking_link": f"https://example.com/book/{location}/{venue_name}/{date}" if available else None
    }

def book_venue(venue_name, location, date, time_slot, contact_name, contact_email, attendees):
    """
    Book a venue for an event.
    
    Parameters:
    - venue_name (str): Name of the venue
    - location (str): City name
    - date (str): Date in YYYY-MM-DD format
    - time_slot (str): Time slot in format "HH:MM-HH:MM"
    - contact_name (str): Name of the person booking
    - contact_email (str): Email of the person booking
    - attendees (int): Expected number of attendees
    
    Returns:
    - dict: Dictionary containing booking information
    """
    # First check if venue is available
    availability = check_venue_availability(venue_name, location, date)
    
    if not availability["available"]:
        return {
            "status": "failed",
            "reason": f"Venue {venue_name} is not available on {date}",
            "booking_id": None,
            "venue_name": venue_name,
            "location": location,
            "date": date
        }
    
    # Check if the requested time slot is available
    if time_slot not in availability["available_time_slots"]:
        return {
            "status": "failed",
            "reason": f"Time slot {time_slot} is not available. Available slots: {', '.join(availability['available_time_slots'])}",
            "booking_id": None,
            "venue_name": venue_name,
            "location": location,
            "date": date
        }
    
    # Check if contact details are provided
    if not contact_name or not contact_email:
        return {
            "status": "failed",
            "reason": "Contact name and email are required",
            "booking_id": None,
            "venue_name": venue_name,
            "location": location,
            "date": date
        }
    
    # Get venue details to check capacity
    venues_result = get_venues(location, "any")
    venue_info = None
    
    for venue in venues_result.get("venues", []):
        if venue["name"] == venue_name:
            venue_info = venue
            break
    
    # Check capacity if venue info is available
    if venue_info and attendees > venue_info["capacity"]:
        return {
            "status": "failed",
            "reason": f"The venue can only accommodate {venue_info['capacity']} people, but you requested for {attendees}",
            "booking_id": None,
            "venue_name": venue_name,
            "location": location,
            "date": date
        }
    
    # Generate booking ID
    import random
    import string
    booking_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    # Calculate cost if venue info is available
    cost = None
    if venue_info:
        hours = int(time_slot.split("-")[1].split(":")[0]) - int(time_slot.split("-")[0].split(":")[0])
        cost = venue_info["cost_per_hour"] * hours
    
    # Create booking
    booking = {
        "status": "confirmed",
        "booking_id": booking_id,
        "venue_name": venue_name,
        "location": location,
        "date": date,
        "time_slot": time_slot,
        "contact_name": contact_name,
        "contact_email": contact_email,
        "attendees": attendees,
        "estimated_cost": cost,
        "confirmation_link": f"https://example.com/confirmation/{booking_id}",
        "cancellation_policy": "Free cancellation up to 48 hours before event"
    }
    
    return booking