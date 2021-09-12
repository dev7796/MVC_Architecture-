from base import app

print("in main")

app.run(port=9001, threaded=True, debug=True)