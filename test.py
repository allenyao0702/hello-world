import sys
class User(object):
    
    
    userId=-1
    followers_id=[]

    def Add_followers(self, followerids):
        for item in followerids:
            self.followers_id.append(item)

    def Remove_followers(self, followerid):
        self.followers_id.remove(followerid)
