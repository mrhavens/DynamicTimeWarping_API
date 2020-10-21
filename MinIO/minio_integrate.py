from minio import Minio
from minio.error import ResponseError
import json
from http.client import HTTPResponse

def main():
    minioClient = Minio(
        '127.0.0.1:9000',
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False,  #Set secure = True if you are using a https connection
    )
    #try:
    print("hi")
    try:
        minioClient.fget_object('test','asl_training.txt','fs.json')
    except ResponseError as err:
        print(err)
    try:
        minioClient.fget_object('test','asl_test.txt','fs1.json')
    except ResponseError as err:
        print(err)

    
