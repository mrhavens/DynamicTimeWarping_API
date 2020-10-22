from minio import Minio
from minio.error import ResponseError
import json
from http.client import HTTPResponse
import os

def main():
    """

    This function will be used to get the data from out MinIO and copy it to
    our flask folder.

    """
    minioClient = Minio(
        '127.0.0.1:9000',
        access_key='YOUR_ACCESS_KEY',
        secret_key='YOUR_SECRET_KEY',
        secure=False,  #Set secure = True if you are using a https connection
    )
    #try:
    print("hi")
    try:
        minioClient.fget_object('test','asl_training.txt','fs.json')
        os.rename('../flask/fs.json','../flask/train.json' )
    except ResponseError as err:
        print(err)
    try:
        minioClient.fget_object('test','asl_test.txt','fs.json')
        os.rename('../flask/fs.json','../flask/test.json' )
    except ResponseError as err:
        print(err)

def upload(file_path):
    """
    This fucntion will be used to upload the file to MinIO bucket

    input: file_path ( This will help us open the file and extract the data)

    """
    minioClient = Minio(
        '127.0.0.1:9000',
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False,  #Set secure = True if you are using a https connection
    )
    file_stat = os.stat(file_path)
    with open(file_path, 'rb') as data:
        minioClient.put_object(
            'output_bucket', 'output', data, file_stat.st_size, 'text/plain',
        )
