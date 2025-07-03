def get_patient_records(patient_id, include_sensitive=False):
    """
    Retrieve patient records from the healthcare database.
    
    Parameters:
    - patient_id (str): Unique identifier for the patient
    - include_sensitive (bool): Whether to include sensitive information
    
    Returns:
    - dict: Dictionary containing patient information
    """
    # Simulated patient database
    patients = {
        "P12345": {
            "basic_info": {
                "name": "John Smith",
                "date_of_birth": "1985-06-15",
                "gender": "Male",
                "blood_type": "O+",
                "height": 180,  # cm
                "weight": 75,   # kg
                "allergies": ["Penicillin", "Peanuts"]
            },
            "contact_info": {
                "address": "123 Main St, Anytown, USA",
                "phone": "555-123-4567",
                "email": "john.smith@example.com",
                "emergency_contact": {
                    "name": "Jane Smith",
                    "relationship": "Spouse",
                    "phone": "555-987-6543"
                }
            },
            "medical_history": {
                "conditions": [
                    {"condition": "Hypertension", "diagnosed": "2018-03-10", "status": "Ongoing"},
                    {"condition": "Asthma", "diagnosed": "2002-11-22", "status": "Managed"}
                ],
                "surgeries": [
                    {"procedure": "Appendectomy", "date": "2010-08-05", "notes": "No complications"}
                ],
                "medications": [
                    {"name": "Lisinopril", "dosage": "10mg", "frequency": "Daily", "started": "2018-03-15"},
                    {"name": "Albuterol", "dosage": "90mcg", "frequency": "As needed", "started": "2002-12-01"}
                ]
            },
            "sensitive_info": {
                "mental_health": [
                    {"condition": "Anxiety disorder", "diagnosed": "2019-05-12", "status": "Under treatment"}
                ],
                "substance_use": {
                    "alcohol": "Occasional",
                    "tobacco": "Never",
                    "recreational_drugs": "Never"
                },
                "hiv_status": "Negative",
                "genetic_testing": {
                    "performed": True,
                    "results": [
                        {"gene": "BRCA1", "result": "Negative", "date": "2020-07-10"}
                    ]
                }
            },
            "recent_visits": [
                {
                    "date": "2023-01-15",
                    "reason": "Annual physical",
                    "diagnosis": "Healthy",
                    "doctor": "Dr. Robert Johnson",
                    "vitals": {
                        "blood_pressure": "135/85",
                        "heart_rate": 72,
                        "temperature": 36.7,
                        "oxygen_saturation": 98
                    }
                },
                {
                    "date": "2022-09-03",
                    "reason": "Respiratory infection",
                    "diagnosis": "Acute bronchitis",
                    "doctor": "Dr. Sarah Lee",
                    "vitals": {
                        "blood_pressure": "140/88",
                        "heart_rate": 88,
                        "temperature": 38.2,
                        "oxygen_saturation": 95
                    }
                }
            ]
        },
        "P67890": {
            "basic_info": {
                "name": "Emily Johnson",
                "date_of_birth": "1992-09-23",
                "gender": "Female",
                "blood_type": "A-",
                "height": 165,  # cm
                "weight": 58,   # kg
                "allergies": ["Sulfa drugs"]
            },
            "contact_info": {
                "address": "456 Oak Ave, Othertown, USA",
                "phone": "555-234-5678",
                "email": "emily.j@example.com",
                "emergency_contact": {
                    "name": "Michael Johnson",
                    "relationship": "Brother",
                    "phone": "555-876-5432"
                }
            },
            "medical_history": {
                "conditions": [
                    {"condition": "Migraine", "diagnosed": "2015-07-18", "status": "Ongoing"},
                    {"condition": "Hypothyroidism", "diagnosed": "2019-02-14", "status": "Managed"}
                ],
                "surgeries": [],
                "medications": [
                    {"name": "Levothyroxine", "dosage": "50mcg", "frequency": "Daily", "started": "2019-02-20"},
                    {"name": "Sumatriptan", "dosage": "100mg", "frequency": "As needed", "started": "2015-08-05"}
                ]
            },
            "sensitive_info": {
                "mental_health": [
                    {"condition": "Depression", "diagnosed": "2018-11-30", "status": "Managed with therapy"}
                ],
                "substance_use": {
                    "alcohol": "Social",
                    "tobacco": "Never",
                    "recreational_drugs": "Never"
                },
                "hiv_status": "Negative",
                "genetic_testing": {
                    "performed": False,
                    "results": []
                }
            },
            "recent_visits": [
                {
                    "date": "2023-03-10",
                    "reason": "Thyroid follow-up",
                    "diagnosis": "Stable hypothyroidism",
                    "doctor": "Dr. Jennifer Adams",
                    "vitals": {
                        "blood_pressure": "118/75",
                        "heart_rate": 68,
                        "temperature": 36.5,
                        "oxygen_saturation": 99
                    }
                },
                {
                    "date": "2022-12-15",
                    "reason": "Migraine episode",
                    "diagnosis": "Acute migraine",
                    "doctor": "Dr. Michael Chen",
                    "vitals": {
                        "blood_pressure": "125/80",
                        "heart_rate": 80,
                        "temperature": 36.8,
                        "oxygen_saturation": 98
                    }
                }
            ]
        }
    }
    
    # Check if patient exists
    if patient_id not in patients:
        return {
            "error": f"Patient with ID {patient_id} not found",
            "patient_id": patient_id
        }
    
    # Create a copy of the patient data without sensitive info if not requested
    patient_data = patients[patient_id].copy()
    if not include_sensitive:
        patient_data.pop("sensitive_info", None)
    
    return {
        "patient_id": patient_id,
        "data": patient_data
    }

def get_lab_results(patient_id, test_type=None, date_from=None, date_to=None):
    """
    Retrieve lab results for a patient with optional filters.
    
    Parameters:
    - patient_id (str): Unique identifier for the patient
    - test_type (str, optional): Filter by test type
    - date_from (str, optional): Filter by date from (YYYY-MM-DD)
    - date_to (str, optional): Filter by date to (YYYY-MM-DD)
    
    Returns:
    - dict: Dictionary containing lab results
    """
    # Simulated lab results database
    lab_data = {
        "P12345": [
            {
                "test_id": "L-20230215-001",
                "date": "2023-02-15",
                "test_type": "Complete Blood Count (CBC)",
                "ordered_by": "Dr. Robert Johnson",
                "results": [
                    {"marker": "WBC", "value": 7.8, "unit": "K/uL", "reference_range": "4.5-11.0", "flag": "normal"},
                    {"marker": "RBC", "value": 5.2, "unit": "M/uL", "reference_range": "4.5-5.9", "flag": "normal"},
                    {"marker": "Hemoglobin", "value": 15.1, "unit": "g/dL", "reference_range": "13.5-17.5", "flag": "normal"},
                    {"marker": "Hematocrit", "value": 45, "unit": "%", "reference_range": "41-50", "flag": "normal"},
                    {"marker": "Platelets", "value": 250, "unit": "K/uL", "reference_range": "150-450", "flag": "normal"}
                ]
            },
            {
                "test_id": "L-20230215-002",
                "date": "2023-02-15",
                "test_type": "Lipid Panel",
                "ordered_by": "Dr. Robert Johnson",
                "results": [
                    {"marker": "Total Cholesterol", "value": 210, "unit": "mg/dL", "reference_range": "<200", "flag": "high"},
                    {"marker": "HDL", "value": 45, "unit": "mg/dL", "reference_range": ">40", "flag": "normal"},
                    {"marker": "LDL", "value": 130, "unit": "mg/dL", "reference_range": "<100", "flag": "high"},
                    {"marker": "Triglycerides", "value": 175, "unit": "mg/dL", "reference_range": "<150", "flag": "high"}
                ]
            },
            {
                "test_id": "L-20230215-003",
                "date": "2023-02-15",
                "test_type": "Metabolic Panel",
                "ordered_by": "Dr. Robert Johnson",
                "results": [
                    {"marker": "Glucose", "value": 95, "unit": "mg/dL", "reference_range": "70-99", "flag": "normal"},
                    {"marker": "BUN", "value": 15, "unit": "mg/dL", "reference_range": "7-20", "flag": "normal"},
                    {"marker": "Creatinine", "value": 1.0, "unit": "mg/dL", "reference_range": "0.7-1.3", "flag": "normal"},
                    {"marker": "Sodium", "value": 140, "unit": "mmol/L", "reference_range": "136-145", "flag": "normal"},
                    {"marker": "Potassium", "value": 4.2, "unit": "mmol/L", "reference_range": "3.5-5.1", "flag": "normal"},
                    {"marker": "Calcium", "value": 9.5, "unit": "mg/dL", "reference_range": "8.5-10.2", "flag": "normal"}
                ]
            },
            {
                "test_id": "L-20220805-001",
                "date": "2022-08-05",
                "test_type": "Thyroid Panel",
                "ordered_by": "Dr. Sarah Lee",
                "results": [
                    {"marker": "TSH", "value": 2.5, "unit": "uIU/mL", "reference_range": "0.4-4.0", "flag": "normal"},
                    {"marker": "Free T4", "value": 1.2, "unit": "ng/dL", "reference_range": "0.8-1.8", "flag": "normal"},
                    {"marker": "Free T3", "value": 3.1, "unit": "pg/mL", "reference_range": "2.3-4.2", "flag": "normal"}
                ]
            }
        ],
        "P67890": [
            {
                "test_id": "L-20230305-001",
                "date": "2023-03-05",
                "test_type": "Complete Blood Count (CBC)",
                "ordered_by": "Dr. Jennifer Adams",
                "results": [
                    {"marker": "WBC", "value": 6.2, "unit": "K/uL", "reference_range": "4.5-11.0", "flag": "normal"},
                    {"marker": "RBC", "value": 4.6, "unit": "M/uL", "reference_range": "4.0-5.2", "flag": "normal"},
                    {"marker": "Hemoglobin", "value": 12.8, "unit": "g/dL", "reference_range": "12.0-16.0", "flag": "normal"},
                    {"marker": "Hematocrit", "value": 38, "unit": "%", "reference_range": "36-46", "flag": "normal"},
                    {"marker": "Platelets", "value": 280, "unit": "K/uL", "reference_range": "150-450", "flag": "normal"}
                ]
            },
            {
                "test_id": "L-20230305-002",
                "date": "2023-03-05",
                "test_type": "Thyroid Panel",
                "ordered_by": "Dr. Jennifer Adams",
                "results": [
                    {"marker": "TSH", "value": 5.2, "unit": "uIU/mL", "reference_range": "0.4-4.0", "flag": "high"},
                    {"marker": "Free T4", "value": 0.7, "unit": "ng/dL", "reference_range": "0.8-1.8", "flag": "low"},
                    {"marker": "Free T3", "value": 2.2, "unit": "pg/mL", "reference_range": "2.3-4.2", "flag": "low"}
                ]
            },
            {
                "test_id": "L-20221210-001",
                "date": "2022-12-10",
                "test_type": "Vitamin Panel",
                "ordered_by": "Dr. Michael Chen",
                "results": [
                    {"marker": "Vitamin D", "value": 22, "unit": "ng/mL", "reference_range": "30-100", "flag": "low"},
                    {"marker": "Vitamin B12", "value": 450, "unit": "pg/mL", "reference_range": "200-900", "flag": "normal"},
                    {"marker": "Folate", "value": 15, "unit": "ng/mL", "reference_range": "3-17", "flag": "normal"}
                ]
            }
        ]
    }
    
    # Check if patient exists
    if patient_id not in lab_data:
        return {
            "error": f"No lab results found for patient ID {patient_id}",
            "patient_id": patient_id,
            "results": []
        }
    
    # Get all results for the patient
    results = lab_data[patient_id]
    
    # Filter by test type if specified
    if test_type:
        results = [r for r in results if test_type.lower() in r["test_type"].lower()]
    
    # Convert date strings to dates for comparison
    from datetime import datetime
    
    # Filter by date range if specified
    if date_from:
        try:
            date_from_obj = datetime.strptime(date_from, "%Y-%m-%d")
            results = [r for r in results if datetime.strptime(r["date"], "%Y-%m-%d") >= date_from_obj]
        except ValueError:
            return {
                "error": "Invalid date_from format. Use YYYY-MM-DD.",
                "patient_id": patient_id,
                "results": []
            }
    
    if date_to:
        try:
            date_to_obj = datetime.strptime(date_to, "%Y-%m-%d")
            results = [r for r in results if datetime.strptime(r["date"], "%Y-%m-%d") <= date_to_obj]
        except ValueError:
            return {
                "error": "Invalid date_to format. Use YYYY-MM-DD.",
                "patient_id": patient_id,
                "results": []
            }
    
    return {
        "patient_id": patient_id,
        "test_count": len(results),
        "results": results
    }

def analyze_lab_results(patient_id, timeframe="recent"):
    """
    Analyze lab results for a patient and identify abnormalities or trends.
    
    Parameters:
    - patient_id (str): Unique identifier for the patient
    - timeframe (str): "recent" for most recent results, "all" for all available results
    
    Returns:
    - dict: Dictionary containing analysis of lab results
    """
    # Get lab results for the patient
    all_results = get_lab_results(patient_id)
    
    # Check if there was an error
    if "error" in all_results:
        return all_results
    
    # Get the results to analyze based on timeframe
    results_to_analyze = all_results["results"]
    if timeframe == "recent" and results_to_analyze:
        # Get the most recent test date
        most_recent_date = max(result["date"] for result in results_to_analyze)
        results_to_analyze = [r for r in results_to_analyze if r["date"] == most_recent_date]
    
    # Initialize analysis
    abnormal_markers = []
    critical_markers = []
    improving_markers = []
    worsening_markers = []
    
    # Process results
    for test in results_to_analyze:
        test_type = test["test_type"]
        date = test["date"]
        
        for marker in test["results"]:
            if marker["flag"] in ["high", "low"]:
                abnormal_markers.append({
                    "test_type": test_type,
                    "date": date,
                    "marker": marker["marker"],
                    "value": marker["value"],
                    "unit": marker["unit"],
                    "reference_range": marker["reference_range"],
                    "flag": marker["flag"]
                })
            
            # Check if the marker is critically abnormal
            value = marker["value"]
            reference_range = marker["reference_range"]
            
            # Parse reference range
            import re
            range_match = re.search(r'([<>]?)(\d+(?:\.\d+)?)-?(\d+(?:\.\d+)?)?', reference_range)
            
            if range_match:
                operator = range_match.group(1)
                lower_bound = float(range_match.group(2))
                upper_bound = float(range_match.group(3)) if range_match.group(3) else None
                
                # Check if critically abnormal
                is_critical = False
                
                if operator == "<" and value >= lower_bound * 1.5:
                    is_critical = True
                elif operator == ">" and value <= lower_bound * 0.5:
                    is_critical = True
                elif upper_bound and (value <= lower_bound * 0.5 or value >= upper_bound * 1.5):
                    is_critical = True
                
                if is_critical:
                    critical_markers.append({
                        "test_type": test_type,
                        "date": date,
                        "marker": marker["marker"],
                        "value": marker["value"],
                        "unit": marker["unit"],
                        "reference_range": marker["reference_range"],
                        "flag": marker["flag"]
                    })
    
    # Analyze trends if we have all results and more than one time point
    if timeframe == "all" and len(all_results["results"]) > 1:
        # Group tests by type and sort by date
        tests_by_type = {}
        for test in all_results["results"]:
            test_type = test["test_type"]
            if test_type not in tests_by_type:
                tests_by_type[test_type] = []
            tests_by_type[test_type].append(test)
        
        # Sort each test type by date
        for test_type in tests_by_type:
            tests_by_type[test_type].sort(key=lambda x: x["date"])
        
        # Analyze trends for each marker
        for test_type, tests in tests_by_type.items():
            if len(tests) < 2:
                continue
            
            # Get the earliest and latest tests
            earliest_test = tests[0]
            latest_test = tests[-1]
            
            # Compare values for common markers
            earliest_markers = {m["marker"]: m for m in earliest_test["results"]}
            latest_markers = {m["marker"]: m for m in latest_test["results"]}
            
            common_markers = set(earliest_markers.keys()) & set(latest_markers.keys())
            
            for marker_name in common_markers:
                early_value = earliest_markers[marker_name]["value"]
                late_value = latest_markers[marker_name]["value"]
                
                # Skip non-numeric values
                if not isinstance(early_value, (int, float)) or not isinstance(late_value, (int, float)):
                    continue
                
                # Calculate percent change
                percent_change = ((late_value - early_value) / early_value) * 100
                
                # Define significant change as ±15%
                if abs(percent_change) >= 15:
                    marker_info = {
                        "test_type": test_type,
                        "marker": marker_name,
                        "early_date": earliest_test["date"],
                        "early_value": early_value,
                        "late_date": latest_test["date"],
                        "late_value": late_value,
                        "percent_change": round(percent_change, 1),
                        "unit": latest_markers[marker_name]["unit"]
                    }
                    
                    # Determine if improving or worsening
                    flag = latest_markers[marker_name]["flag"]
                    reference_range = latest_markers[marker_name]["reference_range"]
                    
                    # Logic to determine if the change is positive or negative
                    # This is a simplified approach - true medical interpretation would be more complex
                    if ">" in reference_range:
                        # For values where higher is better
                        if percent_change > 0:
                            improving_markers.append(marker_info)
                        else:
                            worsening_markers.append(marker_info)
                    elif "<" in reference_range:
                        # For values where lower is better
                        if percent_change < 0:
                            improving_markers.append(marker_info)
                        else:
                            worsening_markers.append(marker_info)
                    else:
                        # For values with a normal range
                        if flag == "normal":
                            # If now normal, it improved
                            if earliest_markers[marker_name]["flag"] != "normal":
                                improving_markers.append(marker_info)
                        elif flag != "normal":
                            # If was normal before, it worsened
                            if earliest_markers[marker_name]["flag"] == "normal":
                                worsening_markers.append(marker_info)
                            # If moving farther from normal range, it worsened
                            elif (flag == "high" and percent_change > 0) or (flag == "low" and percent_change < 0):
                                worsening_markers.append(marker_info)
                            # If moving closer to normal range, it improved
                            elif (flag == "high" and percent_change < 0) or (flag == "low" and percent_change > 0):
                                improving_markers.append(marker_info)
    
    # Get patient info for context
    patient_info = get_patient_records(patient_id)
    if "error" in patient_info:
        basic_info = {}
        conditions = []
        medications = []
    else:
        basic_info = patient_info["data"].get("basic_info", {})
        conditions = patient_info["data"].get("medical_history", {}).get("conditions", [])
        medications = patient_info["data"].get("medical_history", {}).get("medications", [])
    
    # Generate summary based on findings
    summary = ""
    if not abnormal_markers and not critical_markers:
        summary = "All lab results within normal ranges."
    else:
        abnormal_count = len(abnormal_markers)
        critical_count = len(critical_markers)
        summary = f"Found {abnormal_count} abnormal marker(s), including {critical_count} critical value(s)."
    
    # Add trend information
    if improving_markers or worsening_markers:
        summary += f" {len(improving_markers)} marker(s) improving and {len(worsening_markers)} marker(s) worsening over time."
    
    # Return the analysis
    return {
        "patient_id": patient_id,
        "patient_name": basic_info.get("name", "Unknown"),
        "analysis_date": "2023-04-27",  # Current date
        "timeframe": timeframe,
        "summary": summary,
        "abnormal_markers": abnormal_markers,
        "critical_markers": critical_markers,
        "improving_markers": improving_markers if timeframe == "all" else [],
        "worsening_markers": worsening_markers if timeframe == "all" else [],
        "relevant_conditions": conditions,
        "current_medications": medications
    }

def generate_treatment_recommendation(patient_id):
    """
    Generate treatment recommendations based on patient data and lab results.
    
    Parameters:
    - patient_id (str): Unique identifier for the patient
    
    Returns:
    - dict: Dictionary containing treatment recommendations
    """
    # Get patient information
    patient_info = get_patient_records(patient_id, include_sensitive=True)
    if "error" in patient_info:
        return patient_info
    
    # Get lab analysis
    lab_analysis = analyze_lab_results(patient_id, timeframe="all")
    if "error" in lab_analysis:
        return lab_analysis
    
    # Extract relevant patient data
    patient_data = patient_info["data"]
    basic_info = patient_data.get("basic_info", {})
    conditions = patient_data.get("medical_history", {}).get("conditions", [])
    medications = patient_data.get("medical_history", {}).get("medications", [])
    allergies = basic_info.get("allergies", [])
    age = 0
    
    # Calculate age
    try:
        from datetime import datetime
        birth_date = datetime.strptime(basic_info.get("date_of_birth", ""), "%Y-%m-%d")
        today = datetime.strptime("2023-04-27", "%Y-%m-%d")  # Current date
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    except:
        age = "Unknown"
    
    # Extracting abnormal markers
    abnormal_markers = lab_analysis.get("abnormal_markers", [])
    critical_markers = lab_analysis.get("critical_markers", [])
    
    # Initialize recommendations
    medication_recommendations = []
    lifestyle_recommendations = []
    follow_up_recommendations = []
    
    # Generate recommendations based on abnormal markers
    markers_by_type = {}
    for marker in abnormal_markers:
        test_type = marker["test_type"]
        if test_type not in markers_by_type:
            markers_by_type[test_type] = []
        markers_by_type[test_type].append(marker)
    
    # Analyze each test type
    for test_type, markers in markers_by_type.items():
        if test_type == "Lipid Panel":
            # Check cholesterol levels
            cholesterol_markers = {m["marker"]: m for m in markers}
            
            # High total cholesterol or LDL
            if "Total Cholesterol" in cholesterol_markers or "LDL" in cholesterol_markers:
                # Check if already on statin
                on_statin = any("statin" in med["name"].lower() for med in medications)
                
                if on_statin:
                    medication_recommendations.append({
                        "type": "Adjust Medication",
                        "recommendation": "Consider increasing statin dosage to better control lipid levels.",
                        "rationale": "LDL and/or total cholesterol remain elevated despite current therapy."
                    })
                else:
                    medication_recommendations.append({
                        "type": "New Medication",
                        "recommendation": "Consider starting a moderate-intensity statin therapy.",
                        "rationale": "Elevated LDL and/or total cholesterol levels indicate need for pharmacological intervention."
                    })
                
                lifestyle_recommendations.append({
                    "type": "Diet",
                    "recommendation": "Adopt a heart-healthy diet low in saturated fats and high in fiber.",
                    "details": [
                        "Increase consumption of fruits, vegetables, and whole grains",
                        "Limit red meat and full-fat dairy products",
                        "Incorporate omega-3 rich foods such as fish"
                    ]
                })
                
                lifestyle_recommendations.append({
                    "type": "Exercise",
                    "recommendation": "Engage in regular aerobic exercise for at least 150 minutes per week.",
                    "details": [
                        "Activities like brisk walking, swimming, or cycling",
                        "Aim for 30 minutes per day, 5 days per week"
                    ]
                })
                
                follow_up_recommendations.append({
                    "timeframe": "3 months",
                    "tests": ["Lipid Panel"],
                    "purpose": "Re-evaluate cholesterol levels and medication efficacy"
                })
        
        elif test_type == "Complete Blood Count (CBC)":
            # Check for anemia or other blood disorders
            cbc_markers = {m["marker"]: m for m in markers}
            
            if "Hemoglobin" in cbc_markers and cbc_markers["Hemoglobin"]["flag"] == "low":
                # Check if patient has iron deficiency
                has_iron_test = False
                iron_levels = None
                
                # Check all lab results for iron tests
                all_labs = get_lab_results(patient_id)
                for test in all_labs.get("results", []):
                    for result in test["results"]:
                        if result["marker"] in ["Iron", "Ferritin"]:
                            has_iron_test = True
                            iron_levels = result["value"]
                
                if not has_iron_test:
                    follow_up_recommendations.append({
                        "timeframe": "As soon as possible",
                        "tests": ["Iron Panel", "Ferritin", "TIBC"],
                        "purpose": "Evaluate potential iron deficiency anemia"
                    })
                else:
                    medication_recommendations.append({
                        "type": "Supplement",
                        "recommendation": "Start iron supplementation.",
                        "rationale": "Low hemoglobin levels indicate possible iron deficiency anemia."
                    })
                
                lifestyle_recommendations.append({
                    "type": "Diet",
                    "recommendation": "Increase consumption of iron-rich foods.",
                    "details": [
                        "Lean red meat, beans, spinach, and fortified cereals",
                        "Consume with vitamin C for better absorption"
                    ]
                })
        
        elif test_type == "Thyroid Panel":
            # Check thyroid function
            thyroid_markers = {m["marker"]: m for m in markers}
            
            if "TSH" in thyroid_markers:
                tsh = thyroid_markers["TSH"]
                
                # Determine if hypothyroidism or hyperthyroidism
                if tsh["flag"] == "high":
                    # Check if already on levothyroxine
                    on_thyroxine = any("levothyroxine" in med["name"].lower() for med in medications)
                    
                    if on_thyroxine:
                        medication_recommendations.append({
                            "type": "Adjust Medication",
                            "recommendation": "Consider increasing levothyroxine dosage.",
                            "rationale": "Elevated TSH indicates inadequate thyroid hormone replacement."
                        })
                    else:
                        medication_recommendations.append({
                            "type": "New Medication",
                            "recommendation": "Consider starting levothyroxine therapy.",
                            "rationale": "Elevated TSH with low T4 suggests primary hypothyroidism."
                        })
                    
                    follow_up_recommendations.append({
                        "timeframe": "6-8 weeks",
                        "tests": ["Thyroid Panel"],
                        "purpose": "Monitor TSH and T4 response to therapy"
                    })
                
                elif tsh["flag"] == "low":
                    follow_up_recommendations.append({
                        "timeframe": "Soon",
                        "tests": ["Thyroid Panel", "Thyroid Antibodies"],
                        "purpose": "Evaluate for hyperthyroidism or thyroiditis"
                    })
        
        elif test_type == "Metabolic Panel":
            # Check glucose levels
            metabolic_markers = {m["marker"]: m for m in markers}
            
            if "Glucose" in metabolic_markers and metabolic_markers["Glucose"]["flag"] == "high":
                # Check for diabetes
                glucose = metabolic_markers["Glucose"]["value"]
                
                if glucose >= 126:
                    follow_up_recommendations.append({
                        "timeframe": "Soon",
                        "tests": ["HbA1c", "Fasting Glucose"],
                        "purpose": "Evaluate for diabetes mellitus"
                    })
                    
                    lifestyle_recommendations.append({
                        "type": "Diet",
                        "recommendation": "Adopt a low glycemic index diet.",
                        "details": [
                            "Limit refined carbohydrates and sugars",
                            "Focus on whole grains, lean proteins, and healthy fats"
                        ]
                    })
                    
                    lifestyle_recommendations.append({
                        "type": "Exercise",
                        "recommendation": "Implement regular exercise to improve insulin sensitivity.",
                        "details": [
                            "Aim for 150 minutes of moderate-intensity exercise weekly",
                            "Include both cardio and resistance training"
                        ]
                    })
    
    # Special checks for patients with hypertension
    has_hypertension = any(c["condition"].lower() == "hypertension" for c in conditions)
    if has_hypertension:
        # Check if recent BP readings are elevated
        recent_visits = patient_data.get("recent_visits", [])
        if recent_visits:
            latest_visit = recent_visits[0]
            bp_reading = latest_visit.get("vitals", {}).get("blood_pressure", "")
            
            if bp_reading:
                try:
                    systolic, diastolic = map(int, bp_reading.split("/"))
                    
                    if systolic > 140 or diastolic > 90:
                        # Check current medications
                        on_ace_inhibitor = any("lisinopril" in med["name"].lower() for med in medications)
                        on_arb = any("sartan" in med["name"].lower() for med in medications)
                        on_calcium_channel = any("dipine" in med["name"].lower() for med in medications)
                        
                        if not (on_ace_inhibitor or on_arb or on_calcium_channel):
                            medication_recommendations.append({
                                "type": "New Medication",
                                "recommendation": "Consider starting an ACE inhibitor or ARB for blood pressure control.",
                                "rationale": "Blood pressure remains elevated and patient has hypertension."
                            })
                        else:
                            medication_recommendations.append({
                                "type": "Adjust Medication",
                                "recommendation": "Consider optimizing current antihypertensive therapy or adding a second agent.",
                                "rationale": "Blood pressure remains suboptimally controlled on current regimen."
                            })
                        
                        lifestyle_recommendations.append({
                            "type": "Diet",
                            "recommendation": "Follow the DASH diet for hypertension management.",
                            "details": [
                                "Low sodium (< 2,300 mg daily)",
                                "Rich in fruits, vegetables, and low-fat dairy",
                                "Limited saturated fat and cholesterol"
                            ]
                        })
                except:
                    pass
    
    # Generate final recommendations summary
    has_critical = len(critical_markers) > 0
    urgency_level = "High" if has_critical else "Medium" if abnormal_markers else "Routine"
    
    return {
        "patient_id": patient_id,
        "patient_name": basic_info.get("name", "Unknown"),
        "age": age,
        "gender": basic_info.get("gender", "Unknown"),
        "generation_date": "2023-04-27",  # Current date
        "urgency_level": urgency_level,
        "medication_recommendations": medication_recommendations,
        "lifestyle_recommendations": lifestyle_recommendations,
        "follow_up_recommendations": follow_up_recommendations,
        "lab_summary": lab_analysis.get("summary", ""),
        "note_to_physician": "These recommendations are generated based on available data and should be evaluated in the context of the patient's complete clinical picture."
    }