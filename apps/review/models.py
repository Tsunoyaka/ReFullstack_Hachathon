from django.db import models
from apps.hotel.models import Hotel
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Comment(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    RAITING_CHOICES = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
        (SIX, '6'),
        (SEVEN, '7'),
        (EIGHT, '8'),
        (NINE, '9'),
        (TEN, '10'),
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    hotel = models.ForeignKey(
        to=Hotel,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    rating = models.FloatField(blank=True, null=True)
    good_review = models.TextField(blank=True, null=True)
    bad_review = models.TextField(blank=True, null=True)
    staff = models.PositiveSmallIntegerField(choices=RAITING_CHOICES, blank=True, null=True)
    comfort = models.PositiveSmallIntegerField(choices=RAITING_CHOICES, blank=True, null=True)
    purity = models.PositiveSmallIntegerField(choices=RAITING_CHOICES, blank=True, null=True)
    price_quality_ratio = models.PositiveSmallIntegerField(choices=RAITING_CHOICES, blank=True, null=True)
    location = models.PositiveSmallIntegerField(choices=RAITING_CHOICES, blank=True, null=True)
    facilities = models.PositiveSmallIntegerField(choices=RAITING_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def rating_avg(self):
        number_list = [self.staff, self.comfort, self.purity, self.price_quality_ratio, self.location, self.facilities]
        number_list1 = []
        try:
            for i in number_list:
                if i is not None:
                    number_list1.append(i)
            self.rating = round(sum(number_list1)/len(number_list1), 1)
        except:
            self.rating = None
        return self.rating

    def save(self, *args, **kwargs):
        self.rating_avg()
        super().save(*args, **kwargs)

    
    class Meta:
        verbose_name = '??????????????????????'
        verbose_name_plural = '??????????????????????'

    def __str__(self) -> str:
        return f'Comment from {self.user.username} to {self.hotel.title}'

    def get_adsolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})


class Like(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    def __str__(self) -> str:
        return f'Liked by {self.user.username}'

    class Meta:
        verbose_name = '????????????????'
        verbose_name_plural = '????????????????'


class Dislike(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='dislikes'
    )
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        related_name='dislikes'
    )

    def __str__(self) -> str:
        return f'Dislike by {self.user.username}'

    class Meta:
        verbose_name = '???? ????????????????'
        verbose_name_plural = '???? ????????????????'