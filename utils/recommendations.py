def recommendation(brain): 
    if brain == "Dead": 
        return {
            "board": "9x9", 
            "bot": "21k", 
            "study": "No study"
        }
    elif brain == "Sleepy": 
        return {
            "board": "13x13", 
            "bot": "18k", 
            "study": "5 Tsumegos" 
        }
    return {
        "board": "19x19", 
        "bot": "15k", 
        "study": "Review game"
    }