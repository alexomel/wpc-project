from flask import Flask
from flask import render_template, request
app = Flask(__name__)
import boto3, os
from media.s3_storage import S3MediaStorage


s3 = boto3.resource('s3')
storage = S3MediaStorage(s3, os.getenv('APP_BUCKET_NAME'))

@app.route("/")
def hello():
   return "T_T"
@app.route("/order-animation")
def order_animation():
  return render_template(
  "order.html",
  invitation="Welcome at ani creator")

@app.route("/upload", methods=["POST"])
def upload():
  if 'my_file' not in request.files:
    return ":("
  my_file = request.files['my_file']
  storage.save(path="ab/bc/photo", file_to_be_uploaded=my_file)

if __name__ =='__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)