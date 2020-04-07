from django.db import models
from register.models import Student
# Create your models here.
class Profile(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    test_uid = models.CharField(max_length=10, help_text='Enter Your Test ID')
    test_score = models.IntegerField(help_text='Your Test Score',default=0)
    student_emailid = models.EmailField(help_text='Confirm your email',default='abc@abc.com')

    # Metadata
    class Meta: 
        ordering = ['test_uid']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.test_uid
