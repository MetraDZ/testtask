import csv
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user:Kranvagn13@cluster0.du8uq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['test']
collection = db['facebook']

def main():
    #opening profiles.csv file
    with open('profiles.csv', 'r') as f:
        #reading contents
        read = csv.reader(f)
        cnt = 1
        #iterating through them
        for data in read:
            #if there is no document with this id
            if not collection.find_one({'_id': cnt}):
                #creating document
                post = {'_id': cnt, 'name': data[0].strip(), 'code': data[1].strip()}
                #sending it
                collection.insert_one(post)
            cnt += 1
            
if __name__ == "__main__":
    main()