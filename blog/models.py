from django.db import models
from django.utils import timezone

# Los diferentes estados de una tarea
STATUS = (
    ('S', 'Sin asignar'),
    ('P','Pendiente'),
    ('R', 'Realizada')
)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)  
    text = models.TextField()
    created_date = models.DateTimeField(
	default=timezone.now)
    published_date = models.DateTimeField(
	blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Event(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def pending_tasks(self):
        return self.tasks.filter(status='S')

    def __str__(self):
        return self.title

class Task(models.Model):
    event = models.ForeignKey('blog.Event', related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS, default='S')
    budget = models.FloatField(default=0.0)
    owner = models.ForeignKey('blog.Parent', related_name='parentasks', null=True, blank=True)


    def __str__(self):
        return self.title

class Pupil(models.Model):
    GENDER = (
        ('M','Masculino'),
        ('F', 'Femenino')
        )
    name = models.CharField(max_length=40)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    eventsassisted = models.ManyToManyField('blog.Event',related_name='pupilassists', null=True, blank=True)

    def __str__(self):
        return self.name

class Parent(models.Model):

    name = models.CharField(max_length=40)
    pupil = models.ForeignKey('blog.Pupil', related_name='parents')
    eventsorganized = models.ManyToManyField('blog.Event',related_name='parentorganizes', null=True, blank=True)
    eventsassisted = models.ManyToManyField('blog.Event',related_name='parentassists', null=True, blank=True)

    def __str__(self):
        return self.name













