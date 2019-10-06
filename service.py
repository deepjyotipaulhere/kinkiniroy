from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from connection import connect, image_save_path, image_fetch_path
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
CORS(app)

@app.route("/savephotos", methods=['POST'])
def savephotos():
    con=connect()
    try:
        x=request.files['test']
        print(x)
        import random
        filename = secure_filename(str(random.randint(1,10000))+x.filename)
        x.save(os.path.join(image_save_path, filename))
        from PIL import Image
        image=Image.open(os.path.join(image_save_path, filename))
        image.save(os.path.join(image_save_path, filename),quality=20,optimize=True)
        photo=con.kinkiniroy.photos
        photoid=photo.insert_one({'path':filename})
        return str(photoid.inserted_id)
    except Exception as ex:
        print(ex)
        return make_response(str(ex),500)
    finally:
        con.close()


@app.route("/getphotos/<id>", methods=['GET'])
def getphotos(id):
    con=connect()
    try:
        photo=con.kinkiniroy.photos
        from bson.objectid import ObjectId
        x=photo.find_one({"_id":ObjectId(id)})
        x["_id"]=str(x["_id"])
        x["path"]=image_fetch_path+x["path"]
        return jsonify(x)
    except Exception as ex:
        print(ex)
        return make_response(str(ex),500)
    finally:
        con.close()


@app.route("/updatephoto", methods=['POST'])
def updatephoto():
    con=connect()
    try:
        photo=con.kinkiniroy.photos
        p=request.get_json()
        from bson.objectid import ObjectId
        x=photo.update_one({ "_id": ObjectId(p["_id"]) }, { "$set": { "title": str(p['title']), "price": str(p['price']),"description": str(p['description']),"category": str(p['cat']) } })
        return "ok"
    except Exception as ex:
        print(ex)
        return make_response(str(ex),500)
    finally:
        con.close()

@app.route("/getphotoscat/<id>", methods=['GET'])
def getphotoscat(id):
    con=connect()
    try:
        photo=con.kinkiniroy.photos
        x=photo.find({ "category": str(id) })
        k=[]
        for i in x:
            i["_id"]=str(i["_id"])
            i["path"]=image_fetch_path+i["path"]
            k.append(i)
        return jsonify(k)
    except Exception as ex:
        print(ex)
        return make_response(str(ex),500)
    finally:
        con.close()

@app.route("/sendmessage", methods=['POST'])
def sendmessage():
    con=connect()
    p=request.get_json()
    try:
        message=con.kinkiniroy.message
        import datetime
        p['date']=str(datetime.datetime.utcnow())
        x=str(message.insert_one(p).inserted_id)
        con.close()
        return x
    except Exception as ex:
        print(ex)
        return make_response(str(ex),500)
    finally:
        con.close()

if __name__ == "__main__":
    app.run(debug=True)