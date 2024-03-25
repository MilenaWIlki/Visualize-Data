import matplotlib.pyplot as plt

def visualize_data_trends(data):
    # Visualize data trends (e.g., followers over time)
    dates = [entry["date"] for entry in data]
    followers = [entry["followers"] for entry in data]
    plt.plot(dates, followers)
    plt.xlabel("Date")
    plt.ylabel("Followers")
    plt.title("Follower Growth Over Time")
    plt.show()

data_trends = fetch_social_media_data("example_handle")
visualize_data_trends(data_trends)
