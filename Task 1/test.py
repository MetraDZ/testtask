import csv
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user:Kranvagn13@cluster0.du8uq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['test']
collection = db['test']

def main():
    #opening file.csv with data
    with open('file.csv', 'r') as f:
        read = csv.reader(f)
        cnt = 1
        for data in read:
            if not collection.find_one({'_id': cnt}):
                post = {'_id': cnt, 'one': data[0], 'two': data[1], 'three': data[2], 'four': data[3], 'five': data[4], 'six': data[5]}
                collection.insert_one(post)
            cnt += 1

def delete():
    for cnt in range(1, collection.estimated_document_count() + 1):
        for i in collection.find({'_id':cnt},{'three'}):
            if i['three'][0].isalpha():
                collection.delete_one(i)

if __name__ == "__main__":
    main()
    delete()