from flask import Flask,render_template,requests
app= Flask(__name__)

def get_user_submissions(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to load user submissions for {handle}.")
        return []

    data = response.json()

    if data["status"] != "OK":
        print(f"Error: {data['comment']}")
        return []

    return data["result"]
@app.route("/")
def start():

    return "Server is runing"

@app.route("/alpha")
def end():
    data=get_user_submissions('Sushant81')
    return(data)


