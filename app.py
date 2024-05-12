import os
from flask import Flask
from flask import request
app = Flask(__name__)



hooks_results = [
]

@app.route("/", methods = ['GET', 'POST', 'DELETE'])
def main():
    global hooks_results
    if request.method == 'POST':
        hooks_results.append(request.json)    
    return {
        "q": "Pochemy na nebe tak mnogo zvezd?",
        "q1": "Mi kazahi",
        "hooks": hooks_results,
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8055)
