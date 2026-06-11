class Follower:
    def __init__(self, name):
        self.follower._name = name
    def react(self):
        print(self.follower_name, "liked the message")
    def __str__(self):
        return f"follower({self.follower_name})"
    def __repr__(self):
        return f"rep follower({self.follower_name})"
    
class Creator:
    def __init__(self, name):
       self.sub_list = []
       self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, message):
        print(self.creator_name, "publish this message")
        print(message)
        print()
        self.notify_all()