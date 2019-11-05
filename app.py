from server import *
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
  if request.method == 'GET':
    return render_template('predict.html')
  if request.method == 'POST':
    data, filename = validate_file(request)
    img = open_image(data)
    result, accuracy = make_prediction(learner_path = './models', img = img)
    return render_template('prediction.html', img=filename, result = result, accuracy = accuracy)


if __name__ == '__main__':
  app.run(debug=True)