## FAST F1
import fastf1
import pandas as pd

uselessColumns = [
    "Stint",
    "Position",
    "Deleted",
    "PitOutTime",
    "PitInTime",
    "Sector1Time",
    "Sector2Time",
    "Sector3Time",
    "Sector1SessionTime",
    "Sector2SessionTime",
    "Sector3SessionTime",
    "SpeedI1",
    "SpeedI2",
    "SpeedFL",
    "SpeedST",
    "IsPersonalBest",
    "Team",
    "LapStartTime",
    "LapStartDate",
    "DeletedReason",
]
year = 2025
round = 5
session = "FP2"

sData = fastf1.get_session(year, round, session)
sData.load()

verLaps = sData.laps[sData.laps["Driver"] == "VER"]
stint1 = verLaps[verLaps["Stint"] == 3]
stint1 = stint1.drop(columns=uselessColumns)
print(stint1)
