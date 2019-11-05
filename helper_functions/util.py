from settings import *
from fastai.vision import *
vision.defaults.device = vision.torch.device('cpu')
from flask import flash, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file(request):
  if 'file' not in request.files:
    flash('No file!')
    return redirect(request.url)

  file = request.files['file']
  
  if file.filename == '':
    flash('No selected file')
    return redirect(request.url)

  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    filename = os.path.join(app.config['STATIC_FOLDER'], filename)
    file.save(filename)
    data = request.files['file']
    return data, filename

def make_prediction(learner_path, img):
  path = vision.Path(learner_path)
  learn = vision.load_learner(path)
  pred_class,pred_idx,outputs = learn.predict(img)
  return labels[pred_idx], float(outputs[pred_idx])
  # return jsonify({
  #   'result': str(pred_class),
  #   'accuracy': float(outputs[pred_idx])
  # })
