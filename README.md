# Google image Scraper using python (requests & lxml)

By default this will download 100 images from google of seach query "Goku"


Steps on how to use:
1. git clone https://github.com/takshil-k/google_image_scraper.git
2. cd google_image_scraper
3. virtualenv -p python3.6 .venv
4. source .venv/bin/activate
5. pip install -r requirements.txt
6. python image_scraper.py

To change this default download images open image_scraper.py in your favourite editor & do the following:
* Go to line no 51 
* Instead of "Goku" after query_search =, write your search query for which you want to download images.
* Done now, run the script, python image_scraper.py

Improvements:
- [ ] Make good search query (Maybe take a input by prompt).
- [ ] Make code modular.
- [ ] Do for selective images ? like 1 to 50 or 20 to 40.
- [ ] Support for scraping more then 100 images.