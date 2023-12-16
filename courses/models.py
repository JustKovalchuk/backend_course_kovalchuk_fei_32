from django.db import models


class CourseInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=10)
    rating = models.FloatField(default=3)
    image = models.ImageField(upload_to="courses_info/covers/", default="courses_info/covers/default.jpg")
    url_text = models.TextField()

    def __str__(self):
        return str(self.id) + ". " + str(self.title)


class Section(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)

    def __str__(self):
        return str(CourseInfo.objects.filter(id=self.course.id)[0]) + "/" + str(self.title)


class SectionElement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    order = models.IntegerField(default=0)
    duration = models.IntegerField(default=5)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
