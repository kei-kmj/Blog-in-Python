from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-report_date']

    def __str__(self):
        return self.title


def default_position():
    return Position.objects.get_or_create(position='一般社員')[0].id


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)
    position = models.ForeignKey('Position', default=default_position, on_delete=models.CASCADE, blank=True, null=False)

    def calc_tenure(self):
        today = date.today()
        years = today.year - self.joined_date.year

        if (today.month, today.day) < (self.joined_date.month, self.joined_date.day):
            years -= 1

        months = today.month - self.joined_date.month - years + 12 * ((today.month - self.joined_date.month - years) < 0)
        return f'{years}年{months}ヶ月'



    def __str__(self):
        return f"{self.nickname} - {self.department} - {self.team} - {self.position}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Department(models.Model):
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.department


class Team(models.Model):
    team = models.CharField(max_length=255)

    def __str__(self):
        return self.team


class Position(models.Model):
    position = models.CharField(max_length=255, default='一般社員')

    def __str__(self):
        return self.position


class MeetingRoom(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    attendee = models.ForeignKey(User, related_name='attendee', on_delete=models.CASCADE, blank=True, null=True)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.date} - {self.start_time} - {self.end_time} - {self.attendee} - {self.meeting_room}"

