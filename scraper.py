import pandas as pd
from google_play_scraper import app, search
import time
import os
import json

def get_app_details(app_id):
    try:
        print(f"Fetching details for {app_id}")
        app_info = app(app_id)
        return app_info
    except Exception as e:
        print(f"Failed to fetch details for {app_id}: {e}")
        return None

def fetch_app_ids_for_category(category, num_apps=10):
    try:
        print(f"Fetching app IDs for {category}")
        results = search(category, n_hits=30)
        return [result['appId'] for result in results]
    except Exception as e:
        print(f"Failed to fetch app IDs for {category}: {e}")
        return []

def save_to_json(data):
    json_file = 'google_play_apps.json'

    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.extend(data)

    with open(json_file, 'w') as f:
        json.dump(existing_data, f, indent=4)

    print(f"Data saved to {json_file}")

def save_to_csv(app_ids):
    csv_file = 'google_play_apps.csv'

    if os.path.exists(csv_file):
        existing_df = pd.read_csv(csv_file)
        df = pd.DataFrame(app_ids, columns=['appId'])
        combined_df = pd.concat([existing_df, df]).drop_duplicates(subset=['appId'])
    else:
        combined_df = pd.DataFrame(app_ids, columns=['appId'])

    combined_df.to_csv(csv_file, index=False)
    print(f"App IDs saved to {csv_file}")

def main():
    categories = ['Art & Design', 'Auto & Vehicles', 'Beauty', 'Books & Reference', 'Business', 
                'Comics', 'Communication', 'Dating', 'Education', 'Entertainment', 
                'Events', 'Finance', 'Food & Drink', 'Health & Fitness', 'House & Home', 
                'Libraries & Demo', 'Lifestyle', 'Maps & Navigation', 'Medical', 'Music & Audio', 
                'News & Magazines', 'Parenting', 'Personalization', 'Photography', 'Productivity', 
                'Shopping', 'Social', 'Sports', 'Tools', 'Travel & Local', 'Video Players & Editors', 
                'Weather', 'Family Creativity', 'Family Education', 'Family Music & Video', 'Family Pretend Play']

    for category in categories:
        print(f"Fetching app for category: {category}")
        app_ids = fetch_app_ids_for_category(category)
        category_apps = []
        for app_id in app_ids:
            app_details = get_app_details(app_id)
            if app_details:
                category_apps.append(app_details)
            time.sleep(1)

        save_to_json(category_apps)
        save_to_csv(app_ids)

if __name__ == "__main__":
    main()
