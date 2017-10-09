import argparse as ap
import imdb_poster_downloader as imdb

parser = ap.ArgumentParser()
parser.add_argument('--movie', type = str, help = 'Movie name.')
parser.add_argument('--loc', type = str, help = 'Saving location.')

args = parser.parse_args()

imdb.movie(args.movie, args.loc)
