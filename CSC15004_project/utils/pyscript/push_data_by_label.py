import os
import sys
import django

# Add the project's directory to the Python path
django_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(django_project_dir)

# Set the Django settings module manually
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSC15004_project.settings")

# Import and configure Django
django.setup()

from final_lab.models import AmazonLabels

label_dict = {
        'Amazon_Instant_Video': 0,
        'Apps_for_Android': 1,
        'Automotive': 2,
        'Baby': 3,
        'Beauty': 4,
        'Books': 5,
        'CDs_and_Vinyl': 6,
        'Cell_Phones_and_Accessories': 7,
        'Clothing_Shoes_and_Jewelry': 8,
        'Digital_Music': 9,
        'Electronics': 10,
        'Grocery_and_Gourmet_Food': 11,
        'Health_and_Personal_Care': 12,
        'Home_and_Kitchen': 13,
        'Kindle_Store': 14,
        'Movies_and_TV': 15,
        'Musical_Instruments': 16,
        'Office_Products': 17,
        'Patio_Lawn_and_Garden': 18,
        'Pet_Supplies': 19,
        'Sports_and_Outdoors': 20,
        'Tools_and_Home_Improvement': 21,
        'Toys_and_Games': 22,
        'Video_Games': 23}

# Iterate over the label_dict and create AmazonLabels instances
for cat_name, label in label_dict.items():
    AmazonLabels.objects.create(label=label, cat_name=cat_name)
