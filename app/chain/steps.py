from pydantic import BaseModel
from transformers import pipeline

from .runnable import Runnable

class AskInput(BaseModel):
  question: str
  stats: dict
  
class PromptOutput(BaseModel):
  prompt: str
    
class LLMOutput(BaseModel):
  question: str
  raw_answer: str
  
class FinalAnswer(BaseModel):
    question: str
    answer: str
    model: str
    
class PromptBuilder(Runnable):
  def invoke(self, data: AskInput):
    prompt = f"""
you are a civilian.
  
statistik: 
{data.stats}
  
question:
{data.question}
"""
    return PromptOutput(prompt=prompt)
  
class LLMRunner(Runnable):
  def __init__(self):
    self.model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"
    self.generator = pipeline("text-generation", model=self.model_name)

  def invoke(self, data: PromptOutput):
    result = self.generator(data.prompt, max_new_tokens=80)
    text = result[0]["generated_text"]
        
    return LLMOutput(
          question="",
          raw_answer=text
        )

class ResponseParser(Runnable):
  def invoke(self, data: LLMOutput):
    answer = data.raw_answer
    
    return FinalAnswer(
    question=data.question,
    answer=answer,
    model="HuggingFaceTB/SmolLM2-135M-Instruct"
  )