from matplotlib import pyplot as plt
from requests import Session

figure = plt.figure()
subplot_rows = 1
subplot_columns = 1

session = Session()
session.headers = {"content-type" : "application/json"}

polls_res = session.get("http://localhost:9999/v1/polls")
polls = polls_res.json()
polls_num = len(polls)

polls_choices = {}
for poll in polls:
    votes_res = session.get(f"http://localhost:9999/v1/votes?poll_id={poll['id']}")
    votes = votes_res.json()
    votes_num = len(votes)
    for option in poll["options"]:
        polls_choices[option["value"]] = [vote['value'] for vote in votes].count(option["value"])





print(polls_choices)


poll_counter = 1
for poll in polls:
    poll_plt = figure.add_subplot(subplot_rows, subplot_columns, poll_counter)
    poll_plt.plot([],[])
    poll_counter = poll_counter + 1

plt.show()
    