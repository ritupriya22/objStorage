from flask import Flask, request, jsonify

import boto3

from botocore.exceptions import ClientError
 
app = Flask(__name__)
 
# Configure the S3 client with NooBaa's endpoint and credentials

s3 = boto3.client('s3',

                 endpoint_url='https://s3-openshift-storage.apps.cflab6.cfz4.jio.indradhanus.com',

                 aws_access_key_id='32XOXW7WZDCVdiWxRgs6',

                 aws_secret_access_key= 'y+xmbchtySqW728L9LCzH8pQRXnLqdsS8cRC6iiJ' ,
                 verify=False)
@app.route('/upload/<bucket_name>/<file_name>', methods=['POST'])
def upload_file(bucket_name,file_name):
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
 
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    
    file_name = file_name+'/' + file.filename

    try:
        s3.upload_fileobj(file, bucket_name, file_name)
        return jsonify({"success": "File uploaded successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == '__main__':
    app.run(debug=True) 
