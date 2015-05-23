import sys
class User(object):
    
    def __init__(self):
        pass
    userId=-1
    followers_id=[]

    def Add_followers(self, followerids):
        for item in followerids:
            self.followers_id.append(item)

    def Remove_followers(self, followerid):
        self.followers_id.remove(followerid)

class Photo(object):

    def __init__(self):
        CommentList=[];

    photoID = -1
    url = ''
    userId = -1
    CommentList = []

    def Add_Comments(self, commentId):
        CommentList.append(item)

    def Remove_Comments(self, commentId):
        commentList.remove(commentId)

class PhotoList(object):
    
    def __init__(self):
        pass

    userId=-1
    PhotoList=[]

    def Add_photo(self, photoid):
        PhotoList.append(photoid);

    def Remove_photo(self, photoid):
        photoList.remove(photoid)



