from flask import Flask, request , jsonify

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

#creating a GET request
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
         "user_id" : user_id,
         "name"    : "John Doe",
         "email"   : "johndoe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

# creating a POST request 
@app.route("/create-user",methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201



# GET 
# POST
# PUT
# DELETE


if __name__ == "__main__":
    app.run(debug=True)