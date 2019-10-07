# TODO install pymongo and MongoDB
# import pymongo

class ScrapeheroPipeline(object):
    
    # def __init__(self):
        # connection = pymongo.MongoClient('localhost', 27017)
        # db = connection['ScrapeHero']
        # self.collection = db['songs']
    
    def process_item(self, item, spider):
        # valid = True
        # for data in item:
        #     if not data:
        #         valid = False
        #         raise DropItem("Missing {0}!".format(data))
        # if valid:
        #     self.collection.insert(dict(item))
        #     log.msg('Song added to the MongoDB database!', level=log.DEBUG, spider=spider)
        return item
