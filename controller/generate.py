from flask import Flask, Response, request,jsonify, make_response
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from PIL import Image
from io import BytesIO
import requests
import random
import base64
from flask_restful import Resource
from models.model import Malename, Femalename, Lastname, Streetname

class Random_user(Resource):
    def get(self):
        def extract_features(images):
            features=[]
            for image in images:
                img=image.load_img(image,grayscale=True)
                img=img.resize((128,128),Image.ANTIALIAS)
                img=np.array(img)
                features.append(img)
                features=np.array(features)
                features=features.reshape(len(features),128,128,1)
                return features
        
        def random_password():
            lower='abcdefghijklmnopqrstuvwxyz'
            upper='ABCDEFGHIJKLMONPQRSTUVWXYZ'
            num='0123456789'
            special='!@#$%&*()^'
            inipass=lower+upper+num+special
            length=16
            password="".join(random.sample(inipass,length))
            return password

        response = requests.get('https://thispersondoesnotexist.com/image')
        test_path=BytesIO(response.content)
        img=Image.open(test_path)
        img.save('test.png','PNG')
        test_X=extract_features(['test.png'])
        mp=tf.keras.models.load_model('./cnn')
        res=mp.predict(test_X.reshape(1,128,128,1))
        gender_dict={0:'Female',1:'Male'}
        pred_gender=gender_dict[round(res[0][0])]
        fn=random.randint(1,100)
        ln=random.randint(1,100)
        sn=random.randint(1,100)
        d=random.randint(1,30)
        m=random.randint(1,12)
        y=random.randint(1972,2004)

        if pred_gender == 'Male':
            fname_obj=Malename.objects(fn_id=fn).first()
        else:
            fname_obj=Femalename.objects(fn_id=fn).first()

        lname_obj=Lastname.objects(fn_id=fn).first()
        sname_obj=Streetname.objects(fn_id=fn).first()
        fname=fname_obj.to_json()['name']
        lname=lname_obj.to_json()['name']
        sname=sname_obj.to_json()['name']+' st.'
        fpass=random_password()
        gmail=fname+lname+'@gmail.com'
        dob=str(d)+'/'+str(m)+'/'+str(y)
        with open('test.png','rb') as f:
            img_string=base64.b64encode(f.read())
        img_string=str(img_string)
        img_string=img_string[2:-1]        

        fin_result={
            'Image':"data:image/png;base64, "+img_string,
            'Name':fname+" "+lname,
            'Email Id':gmail,
            'Date of Birth':dob,
            'Address':sname,
            'Password':fpass
        }

        return make_response(jsonify(fin_result),200)