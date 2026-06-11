from ._anvil_designer import FeedbackFormForNothingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class FeedbackFormForNothing(FeedbackFormForNothingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  def clear_inputs(self):
    self.name_box.text = ""
    self.
  
  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    anvil.server.call('add_feedback', name, email, feedback)
    alert("YOU clicked the button.... Bad idea...")
    Notification("Feedback submitted!").show()
    pass
