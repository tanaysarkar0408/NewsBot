from pydantic import BaseModel, Field
from typing import List

class CareerGoal(BaseModel):
    target_role: str = "SDE-1"
    target_companies: List[str] = ["MAANG"]
    focus_areas: List[str] = Field(default_factory=list, description="Topics currently focusing on")

class WeeklyCareerAdvice(BaseModel):
    date: str
    learning_suggestion: str = Field(..., description="What should be learned next")
    project_idea: str = Field(..., description="A project to build to stand out")
    system_design_concept: str = Field(..., description="A specific system design concept to understand")
    motivational_quote: str = Field(..., description="A small quote to keep motivation high")
