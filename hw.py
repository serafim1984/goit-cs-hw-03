import argparse
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

config = dotenv_values(".env_mongo")

uri = f"mongodb+srv://{config['USER_MDB']}:{config['PASSWORD_MDB']}@cluster0.hyo17fr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.HW_06

parser = argparse.ArgumentParser(description="Manage cats")
parser.add_argument("--action", help="[create, read, update, delete, info, show_age, add_feature, delete_cat, delete_all]")
parser.add_argument("--id", help="ID of the cat")
parser.add_argument("--name", help="Name of the cat")
parser.add_argument("--age", help="Age of the cat")
parser.add_argument("--features", help="Features of the cat", nargs="+")
parser.add_argument("--new_feature", help="New feature to add to the cat's existing features")

args = vars(parser.parse_args())
action = args["action"]
pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]
new_feature = args["new_feature"]


def read():
    cats = db.cats.find()
    return cats


def create(name, age, features):
    return db.cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })


def update(pk, name, age, features):
    return db.cats.update_one({"_id": ObjectId(pk)}, {"$set": {"name": name, "age": age, "features": features}})


def delete(pk):
    return db.cats.delete_one({"_id": ObjectId(pk)})


def info(name):
    cat = db.cats.find_one({"name": name})
    if cat:
        print(f"Name: {cat['name']}, Age: {cat['age']}, Features: {cat['features']}")
    else:
        print(f"Cat with name {name} not found")


def show_age(name):
    cat = db.cats.find_one({"name": name})
    if cat:
        print(f"Age of {name} is {cat['age']}")
    else:
        print(f"Cat with name {name} not found")


def add_feature(name, new_feature):
    cat = db.cats.find_one({"name": name})
    if cat:
        existing_features = cat.get("features", [])
        existing_features.append(new_feature)
        update_result = db.cats.update_one({"_id": cat["_id"]}, {"$set": {"features": existing_features}})
        if update_result.modified_count > 0:
            print(f"New feature '{new_feature}' added to {name}")
        else:
            print("Failed to add new feature")
    else:
        print(f"Cat with name {name} not found")


def delete_cat(name):
    result = db.cats.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Cat {name} deleted successfully")
    else:
        print(f"Cat with name {name} not found")


def delete_all():
    result = db.cats.delete_many({})
    print(f"{result.deleted_count} records deleted")


if __name__ == "__main__":
    match action:
        case "create":
            r = create(name, age, features)
            print(r.inserted_id)
        case "read":
            [print(cat) for cat in read()]
        case "update":
            r = update(pk, name, age, features)
            print(r.modified_count)
        case "delete":
            r = delete(pk)
            print(r.deleted_count)
        case "info":
            info(name)
        case "show_age":
            show_age(name)
        case "add_feature":
            add_feature(name, new_feature)
        case "delete_cat":
            delete_cat(name)
        case "delete_all":
            delete_all()
        case _:
            print("Wrong action")




