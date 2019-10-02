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

if __name__ == "__main__":
    app.run(debug=True)