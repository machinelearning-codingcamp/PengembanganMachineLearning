import pandas as pd

# GANTI INI

movies = {
    "Deadpool_N_Wolverine": "https://www.rottentomatoes.com/m/deadpool_and_wolverine/reviews?type=user",
    # "The_Marvels": "https://www.rottentomatoes.com/m/the_marvels/reviews?type=userr",
    "Guardians_of_the Galaxy_Vol3": "https://www.rottentomatoes.com/m/guardians_of_the_galaxy_vol_3/reviews?type=user",
    "Ant-Man_and_The_Wasp_Quantumania": "https://www.rottentomatoes.com/m/ant_man_and_the_wasp_quantumania/reviews?type=user",
    "Black_Panther_Wakanda_Forever": "https://www.rottentomatoes.com/m/black_panther_wakanda_forever/reviews?type=user",
    "Thor_Love_and_Thunder": "https://www.rottentomatoes.com/m/thor_love_and_thunder/reviews?type=user",
    "Doctor_Strange_in_the_Multiverse_of_Madness": "https://www.rottentomatoes.com/m/doctor_strange_in_the_multiverse_of_madness/reviews?type=user",
    "Spider-Man_No_Way_Home": "https://www.rottentomatoes.com/m/spider_man_no_way_home/reviews?type=user",
    "Eternals": "https://www.rottentomatoes.com/m/eternals/reviews?type=user",
}

for title, url in movies.items():
    filename = f"{title}_reviews.txt"
    with open(filename, "r", encoding="utf-8") as file:
        reviews = file.readlines()

    df = pd.DataFrame({"Review": [review.strip() for review in reviews]})

    filenameCSV = f"{title}_reviews.csv"
    df.to_csv(filenameCSV, index=False, encoding="utf-8")

    print("Reviews saved to csv")
