from django.db import models

# Create your models here.
class HuggingFaceModel(models.Model):
    pub_path = models.CharField(max_length=200)
    upd_date = models.DateTimeField("date updated")

    def __str__(self):
        return self.pub_path

class ModelInfor(models.Model):
    model_path = models.ForeignKey(HuggingFaceModel, on_delete=models.CASCADE)
    
    train_los = models.DecimalField(max_digits=15, decimal_places=12)
    train_acc = models.DecimalField(max_digits=15, decimal_places=12)

    val_los = models.DecimalField(max_digits=15, decimal_places=12)
    val_acc = models.DecimalField(max_digits=15, decimal_places=12)

    test_los = models.DecimalField(max_digits=15, decimal_places=12)
    test_acc = models.DecimalField(max_digits=15, decimal_places=12)

    def __str__(self):
        return self.test_acc
    
class AmazonLabels(models.Model):
    label = models.IntegerField(default=0)
    cat_name = models.CharField(max_length=64)
    svg_str = models.CharField(max_length=3000, default="nothing")

    def __str__(self):
        return str(self.label)
    
class AmazonProductReviews(models.Model):
    label = models.ForeignKey(AmazonLabels, on_delete=models.CASCADE)
    reviewText = models.CharField(max_length=1500)

    def __str__(self):
        return self.reviewText

