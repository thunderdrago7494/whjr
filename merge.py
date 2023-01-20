import csv
with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
headers.append("poster_link")
with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movie_links.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies_links = data[1:]


for mi in all_movies:
    poster_found = any(mi[8]in movie_link_items for movie_links_items in all_movies_links)
    if poster_found:
        for movie_link_items in all_movies_links:
            if mi[8]== movie_link_items[0]:
                mi.append(movie_link_items[1])
                if len(mi)==28:
                    with open("final.csv","a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(mi)
                        