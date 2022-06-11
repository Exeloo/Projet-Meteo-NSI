class GetConfig:
    def __init__(self):
        # MNU4UKWYRFVT992QVFK2RPSRT
        #
        self.api_key = "MNU4UKWYRFVT992QVFK2RPSRT"
        self.cities = {
            "Lille": {"x": 325, "y": 75},
            "le Havre": {"x": 225, "y": 135},
            "Brest": {"x": 90, "y": 180},
            "Angers": {"x": 180, "y": 215},
            "Paris": {"x": 315, "y": 160},
            "la Rochelle": {"x": 225, "y": 300},
            "Biarritz": {"x": 175, "y": 440},
            "Bordeaux": {"x": 200, "y": 380},
            "Toulouse": {"x": 280, "y": 430},
            "Perpignant": {"x": 300, "y": 480},
            "Marseille": {"x": 400, "y": 420},
            "Nice": {"x": 475, "y": 420},
            "Grenoble": {"x": 420, "y": 330},
            "Nancy": {"x": 430, "y": 150},
            "Dijon": {"x": 400, "y": 240},
            "Orléans": {"x": 280, "y": 230},
            "Bourges": {"x": 340, "y": 300},
            "Rodez": {"x": 340, "y": 380},
            "Ajaccio": {"x": 560, "y": 500}
        }
        self.precise_type = ["today", "three_day", "week"]
        self.wind_force = {
            "low": 7,
            "mid": 15
        }
        self.size = {
            "arrow": 50
        }
