# Google Play Metadata Scraper

This project provides a script to scrape app details and app IDs from the Google Play Store across various categories through [google_play_scraper](https://github.com/JoMingyu/google-play-scraper).
The script fetches detailed information about apps and saves the data to a JSON file while also saving the app IDs to a CSV file.
It will catch 30 app information for 35 categories in Google Play Store.

## Features

- Fetches detailed information about apps from the Google Play Store.
- Supports multiple app categories.
- Saves app details to a JSON file
- Saves app IDs to a CSV file.
- Incrementally updates the files to prevent data loss.

## Requirements

- Python 3.6+
- `google-play-scraper` library
- `pandas` library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/google-play-metadata-scraper.git
cd google-play-metadata-scraper
```

2. Install the required libraries:

```sh
pip install google-play-scraper pandas
```

## Usage

1. Open the `scraper.py` file and review the categories listed in the `main` function. You can add or remove categories as needed.

2. Run the script:

```sh
python scraper.py
```

The script will:

- Fetch app details and app IDs for each category.
- Save the detailed app data to `google_play_apps.json`.
- Save the app IDs to `google_play_apps.csv`.

## Metadata Information

The JSON file will contain detailed information about each app, including but not limited to the following fields:

- `title`: The title of the app.
- `description`: The description of the app.
- `descriptionHTML`: The HTML-formatted description of the app.
- `summary`: A brief summary of the app.
- `installs`: The number of installs.
- `minInstalls`: The minimum number of installs.
- `realInstalls`: The real number of installs.
- `score`: The average user rating.
- `ratings`: The number of ratings.
- `reviews`: The number of reviews.
- `histogram`: The distribution of ratings.
- `price`: The price of the app.
- `free`: Whether the app is free.
- `currency`: The currency used for the price.
- `sale`: Whether the app is on sale.
- `saleTime`: The time when the sale ends.
- `originalPrice`: The original price of the app.
- `saleText`: Text describing the sale.
- `offersIAP`: Whether the app offers in-app purchases.
- `inAppProductPrice`: The price range for in-app products.
- `developer`: The developer of the app.
- `developerId`: The developer's ID.
- `developerEmail`: The developer's email address.
- `developerWebsite`: The developer's website.
- `developerAddress`: The developer's physical address.
- `privacyPolicy`: The privacy policy URL.
- `genre`: The genre of the app.
- `genreId`: The genre ID.
- `categories`: A list of categories the app belongs to.
- `icon`: The URL of the app's icon.
- `headerImage`: The URL of the app's header image.
- `screenshots`: A list of URLs for the app's screenshots.
- `video`: The URL of the app's video.
- `videoImage`: The URL of the app's video image.
- `contentRating`: The content rating of the app.
- `contentRatingDescription`: A description of the content rating.
- `adSupported`: Whether the app contains ads.
- `containsAds`: Whether the app contains ads.
- `released`: The release date of the app.
- `lastUpdatedOn`: The last update date of the app.
- `updated`: The timestamp of the last update.
- `version`: The version of the app.
- `comments`: A list of comments for the app.
- `appId`: The app ID.
- `url`: The URL of the app on the Google Play Store.

## Code Explanation

### Main Functions

- `get_app_details(app_id)`: Fetches detailed information about an app using its app ID.
- `fetch_app_ids_for_category(category, num_apps=10)`: Fetches app IDs for a specific category.
- `save_to_json(data)`: Saves the detailed app data to a JSON file.
- `save_to_csv(app_ids)`: Saves the app IDs to a CSV file.
- `main()`: Main function that iterates through the specified categories, fetches app details and IDs, and saves the data to files.

### Script Structure

1. **Fetch App IDs**: For each category, the script fetches app IDs.
2. **Fetch App Details**: For each app ID, the script fetches detailed app information.
3. **Save Data**: The script saves the detailed app information to `google_play_apps.json` and app IDs to `google_play_apps.csv`.

### Example

```python
# Fetch app IDs for the 'Books & Reference' category
app_ids = fetch_app_ids_for_category('Books & Reference')

# Fetch detailed information for each app ID
category_apps = []
for app_id in app_ids:
    app_details = get_app_details(app_id)
    if app_details:
        category_apps.append(app_details)

# Save the detailed app data and app IDs
save_to_json(category_apps)
save_to_csv(app_ids)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The `google-play-scraper` library for providing an easy way to scrape Google Play Store data.
