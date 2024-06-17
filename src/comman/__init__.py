import pandas as pd
from src.services.aws_services import S3CSVReader
import matplotlib.pyplot as plt
from io import BytesIO


def get_csv_from_s3(bucket_name, file_path):
    s3_reader = S3CSVReader()
    df = s3_reader.read_csv_from_s3(bucket_name, file_path)
    return df




def top_scorers_team(team_name, n):
    # deliveries = pd.read_csv('/Users/abhishek.chaudhary/Abhishek/Developer/CricReader/src/dataset/deliveries.csv')
    deliveries = get_csv_from_s3(bucket_name="abhishekchaudhary", file_path="cric-reader/deliveries.csv")
    team_df = deliveries[deliveries['batting_team'] == team_name]
    team_batsman_runs_sum = team_df.groupby('batter')['batsman_runs'].sum().reset_index()
    team_batsman_runs_sum.rename(columns={'batsman_runs': 'total_batsman_runs'}, inplace=True)
    team_batsman_runs_sum = team_batsman_runs_sum.sort_values(by='total_batsman_runs', ascending=False)
    top_n_run_scorers = team_batsman_runs_sum.head(n)
    plt.bar(top_n_run_scorers['batter'], top_n_run_scorers['total_batsman_runs'])
    plt.xlabel('Batter')
    plt.ylabel('Runs Scored')
    plt.title(f'Top run scorers')
    image_buffer = BytesIO()
    plt.savefig(image_buffer, format='png')
    image_buffer.seek(0)
    import time
    current_timestamp = time.time()
    time = int(current_timestamp)
    file_name = f"img_{time}.png"
    graph = S3CSVReader.get_graph_signed_url(bucket_name="abhishekchaudhary", file_name=file_name, image_buffer=image_buffer)
    return graph


def top_scorers(n):
    deliveries = get_csv_from_s3(bucket_name="abhishekchaudhary", file_path="cric-reader/deliveries.csv")
    team_batsman_runs_sum = deliveries.groupby('batter')['batsman_runs'].sum().reset_index()
    team_batsman_runs_sum.rename(columns={'batsman_runs': 'total_batsman_runs'}, inplace=True)
    team_batsman_runs_sum = team_batsman_runs_sum.sort_values(by='total_batsman_runs', ascending=False)
    top_n_run_scorers = team_batsman_runs_sum.head(n)
    return top_n_run_scorers.values.tolist()


def top_wicket_taker_for_team(team_name, n):
    deliveries = get_csv_from_s3(bucket_name="abhishekchaudhary", file_path="cric-reader/deliveries.csv")
    team_b_df = deliveries[deliveries['bowling_team'] == team_name]
    team_b_bowler_wicket_sum = team_b_df.groupby('bowler')['is_wicket'].sum().reset_index()
    team_b_bowler_wicket_sum.rename(columns={'is_wicket': 'total_bowler_wickets'}, inplace=True)
    team_b_bowler_wicket_sum = team_b_bowler_wicket_sum.sort_values(by='total_bowler_wickets', ascending=False)
    top_n_wicket_taker = team_b_bowler_wicket_sum.head(n)
    return top_n_wicket_taker.values.tolist()


def top_wicket_taker(n):
    deliveries = get_csv_from_s3(bucket_name="abhishekchaudhary", file_path="cric-reader/deliveries.csv")
    team_b_bowler_wicket_sum = deliveries.groupby('bowler')['is_wicket'].sum().reset_index()
    team_b_bowler_wicket_sum.rename(columns={'is_wicket': 'total_bowler_wickets'}, inplace=True)
    team_b_bowler_wicket_sum = team_b_bowler_wicket_sum.sort_values(by='total_bowler_wickets', ascending=False)
    top_n_wicket_taker = team_b_bowler_wicket_sum.head(n)
    return top_n_wicket_taker.values.tolist()


def most_wins():
    print("I am here")
    matches = get_csv_from_s3(bucket_name="abhishekchaudhary", file_path="cric-reader/matches.csv")
    print("\n\n\n\nRead File\n\n\n")
    matches_won = matches.groupby('winner').size().reset_index(name='matches_won')
    matches_won = matches_won.sort_values(by='matches_won', ascending=False)
    return matches_won.values.tolist()
