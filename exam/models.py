from django.db import models
from register.models import Student
from dashboard.models import Profile
# Create your models here.
class Mcq(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    test_no = models.CharField(max_length=10,help_text='Test Number')
    q_no = models.IntegerField(help_text='Question number')
    ques = models.TextField(help_text="Question Description")
    op1 = models.CharField(max_length=100,help_text='Option 1')
    op2 = models.CharField(max_length=100,help_text='Option 2')
    op3 = models.CharField(max_length=100,help_text='Option 3')
    op4 = models.CharField(max_length=100,help_text='Option 4')
    ans1 = models.BooleanField(help_text='Answer option number1')
    ans2 = models.BooleanField(help_text='Answer option number2')
    ans3 = models.BooleanField(help_text='Answer option number3')
    ans4 = models.BooleanField(help_text='Answer option number4')
    points = models.IntegerField(help_text='Marks alooted to this question')

    ...

    # Metadata
    class Meta: 
        ordering = ['q_no']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        string=""
        string+=self.test_no
        string+='--'
        string+=str(self.q_no)
        return string
