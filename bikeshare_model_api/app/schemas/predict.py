from typing import Any, List, Optional

from pydantic import BaseModel
from bikeshare_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "season": "fall",
                        "hr": "7pm",
                        "holiday": "No",
                        "workingday": "Yes",
                        "weathersit": "Mist",
                        "temp": 15.5,
                        "atemp": 15.9968,
                        "hum": 55.00000000000001,
                        "windspeed": 11.0014,
                        "yr": 2011,
                        "mnth": "September",
                        "weekday": "Fri",
                        "dteday": "2011-09-16", # datetime.datetime.strptime("2012-11-05", "%Y-%m-%d")  

                    }
                ]
            }
        }
