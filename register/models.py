from django.db import models

# Create your models here.
class Student(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    student_name = models.CharField(max_length=100, help_text='Enter Your Name')
    student_email = models.EmailField(help_text='Enter Your Email ID',primary_key=True)
    student_mobile = models.CharField(max_length=10,help_text='Enter Your Mobile Number')
    student_password = models.CharField(max_length=30,help_text='Enter a strong password')
    ...

    # Metadata
    class Meta: 
        ordering = ['student_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.student_email