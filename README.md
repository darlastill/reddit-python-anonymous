# Determining Anonymity with Reddit Data

This program assumes you have acquired Reddit data and have the corpus of all authors to compare with authors in your sample. This program was used with High Performance Computing through a university server. 

## Getting Started

Want the Reddit data? See this archived [Reddit post](https://www.reddit.com/r/datasets/comments/3mg812/full_reddit_submission_corpus_now_available_2006/?st=jbrdzusl&sh=fe5ec1aa). 

### How it Works

* Anonymity is defined as an author (OP) on Reddit who only uses their username in one subreddit to write posts. This code does not account for comments outside of the subreddit of study. 

* Read in three data files - sample authors, sample commenters, and the corpus of authors outside of your sample. 

* The code creates a numpy array for you to search the corpus for authors and create binary variable indicating whether an author appears outside of the subreddit of study. 

* Then, save this as a new csv file. 

## Built With and Versioning

This code and workshop was written using Python 3.7.4 with the [Anaconda distribution](https://www.anaconda.com/products/individual). 

## Authors

* **Darla Still** 