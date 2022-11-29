from matplotlib import pyplot as plt
from requests import Session
import argparse

parser= argparse.ArgumentParser()
parser.add_argument("-t", "--type", type=str, help="Type of charts to visualise the polls votes", default="bar", choices=["pie", "bar"])

args = parser.parse_args()
chart_type = args.type

session = Session()
session.headers = {"content-type" : "application/json"}

polls_res = session.get("http://localhost:9999/v1/polls")
polls = polls_res.json()


polls_choices = {}
for poll in polls:
    polls_choices[poll["title"]] = {} 
    votes_res = session.get(f"http://localhost:9999/v1/votes?poll_id={poll['id']}")
    votes = votes_res.json()
    votes_num = len(votes)
    for option in poll["options"]:
        polls_choices[poll["title"]][option["value"]] = [vote['value'] for vote in votes].count(option["value"])

plots_per_row = 3
subplot_rows = round(len(polls)/3)

subplot_row = 1
for poll_title, poll_votes in polls_choices.items():
    figure = plt.figure(figsize=[10,10])
    subplot_columns = 1
    poll_plt = figure.add_subplot(1,1,1)
    poll_plt.set_title(poll_title)
    x_axis = []
    y_axis = []
    for option, votes in poll_votes.items():
        x_axis.append(option)
        y_axis.append(votes)
    
    if chart_type == "pie":
        poll_plt.pie(
            y_axis,
            labels=x_axis,
            explode=[0.01 for i in range(len(x_axis))],
            autopct="%1.1f%%")
    elif chart_type == "bar":
        poll_plt.set_xlabel("Choices")
        poll_plt.set_ylabel("votes")
        poll_plt.bar(
            x_axis,
            y_axis
        )
    if subplot_row == 3:
        subplot_row = subplot_row + 1
    else:
        subplot_row = 1
plt.show()

    