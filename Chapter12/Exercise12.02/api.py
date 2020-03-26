from flask import Flask, request
import pickle

# load the model from pickle file
file = open('model.pkl', 'rb')  # read bytes
model = pickle.load(file)
file.close()

# create an API with Flask
app = Flask('Titanic')


@app.route('/hi', methods=['GET'])
def hello():
    return 'Hello world!'


# call this: curl -X POST -H "Content-Type: application/json" \
# -d '{"Pclass": 3, "Sex": 0, "Age": 72, "SibSb": 2, "Parch": 0, "Fare": 8.35}' http://127.0.0.1:5000/survived
@app.route('/survived', methods=['POST'])
def survived():
    payload = request.get_json()
    person = [payload['Pclass'], payload['Sex'], payload['Age'], payload['SibSb'], payload['Parch'], payload['Fare']]
    result = model.predict([person])
    print(f'{person} -> {str(result)}')
    return f'I predict that person {person} has {"_not_ " if result == [0] else ""}survived the Titanic\n'


app.run()
