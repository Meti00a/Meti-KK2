class Runnable:
  def invoke(self, data):
    raise NotImplementedError()
  
  def __or__(self, next_step):
    return RunnableSequence(self, next_step)
  
class RunnableSequence:
  def __init__(self, first_step, second_step):
    self.first_step = first_step
    self.second_step = second_step
    
  def invoke(self, data):
    result = self.first_step.invoke(data)
    return self.second_step.invoke(result)
    
  def __or__(self, next_step):
    return RunnableSequence(self, next_step)