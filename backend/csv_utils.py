# csv_utils.py

import os
import pandas as pd


def save_reviews_to_csv(
    reviews,
    product_name,
    overall_rating,
    category="Mobile",
    output_folder="data"
):

    os.makedirs(output_folder, exist_ok=True)

    csv_path = os.path.join(output_folder, "reviews.csv")

    rows = []

    for review in reviews:

        rows.append({
            "Product Name": product_name,
            "Category": category,
            "Overall Rating": overall_rating,
            "Review Rating": review["rating"],
            "Review Title": review["title"],
            "Review Text": review["review"]
        })

    df = pd.DataFrame(rows)

    if os.path.exists(csv_path):

        df.to_csv(
            csv_path,
            mode="a",
            header=False,
            index=False,
            encoding="utf-8-sig"
        )

    else:

        df.to_csv(
            csv_path,
            index=False,
            encoding="utf-8-sig"
        )

    print(f"\nSaved {len(df)} reviews to {csv_path}")