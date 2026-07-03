import pandas as pd
import random

products = [
    ("iPhone 15",4.6),("Samsung Galaxy S24",4.5),("OnePlus 12",4.5),
    ("Google Pixel 8",4.4),("Nothing Phone 2",4.3),("Realme GT 6",4.4),
    ("Redmi Note 13 Pro",4.3),("POCO X6 Pro",4.4),("Vivo V30",4.4),
    ("OPPO Reno 11",4.3),("Motorola Edge 50 Pro",4.4),("iQOO Neo 9 Pro",4.5),
    ("Samsung Galaxy A55",4.4),("Realme Narzo 70 Pro",4.3),("OnePlus Nord CE 4",4.4),
    ("Redmi 13C",4.2),("Nothing Phone 2a",4.4),("Vivo T3",4.3),
    ("OPPO F27 Pro+",4.2),("Moto G85",4.3)
]

titles = {
    5:["Excellent phone","Mind-blowing purchase","Worth every penny","Awesome camera","Highly recommended"],
    4:["Value for money","Good choice","Very good","Nice product","Satisfied"],
    3:["Decent phone","Average experience","Good but could improve","Okay overall","Mixed feelings"],
    2:["Needs improvement","Disappointing battery","Could be better","Average camera","Not as expected"]
}

texts = {
    5:[
        "Excellent display, smooth performance and amazing battery life.",
        "Camera quality is outstanding in all lighting conditions.",
        "Very fast phone with premium build quality.",
        "Gaming performance is excellent without heating.",
        "Highly recommended for everyday use."
    ],
    4:[
        "Overall performance is good for the price.",
        "Battery lasts all day with moderate usage.",
        "Display is bright and colourful.",
        "Good software experience.",
        "Worth buying."
    ],
    3:[
        "Performance is decent but software needs improvement.",
        "Camera is average in low light.",
        "Battery backup could be better.",
        "Expected more features.",
        "Overall an average experience."
    ],
    2:[
        "Battery performance is disappointing.",
        "Camera quality did not meet expectations.",
        "Software has occasional lag.",
        "Heating issue during gaming.",
        "Not worth the current price."
    ]
}

rows = []

for product, overall in products:
    ratings = [5]*10 + [4]*7 + [3]*2 + [2]*1
    random.shuffle(ratings)

    for rating in ratings:
        rows.append({
            "product_name": product,
            "overall_rating": overall,
            "review_rating": rating,
            "review_title": random.choice(titles[rating]),
            "review_text": random.choice(texts[rating])
        })

df = pd.DataFrame(rows)

df.to_csv("data/reviews.csv", index=False)

print("Dataset created successfully!")
print(df.shape)