'''
heapq.nlargest(n, iterable, key=None) is used to
find the n largest elements from a dataset defined by iterable.


people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 40},
    {"name": "Dave", "age": 20}
]

# Using nlargest to find the two oldest people
oldest_two = heapq.nlargest(2, people, key=lambda person: person["age"])

print(oldest_two)
# Output: [{'name': 'Carol', 'age': 40}, {'name': 'Alice', 'age': 30}]

'''

from collections import defaultdict
from heapq import nlargest
from typing import List

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.tweet_time = defaultdict(int)  # id => timestamp
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweet_time[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        following = self.user_following[userId]
        users = set(following)
        users.add(userId)  # should see my own tweets too
        tweets = [self.user_tweets[u][::-1][:10] for u in users]  # Get the 10 most recent tweets
        '''
        unconventional way to flatten a list of lists into a single list:
            lists = [[1, 2, 3], [4, 5], [6]]
            flattened = sum(lists, [])
            print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

        or, another way getting flattened tweets:
            flattened_tweets = [tweet for each_user_tweets in tweets for tweet in each_user_tweets]
        '''
        tweets = sum(tweets, [])
        return nlargest(10, tweets, key=lambda tweet: self.tweet_time[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        following = self.user_following[followerId]
        if followeeId in following:
            following.remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

############

import heapq


class Twitter(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.ts = 0
    self.tweets = collections.defaultdict(list)
    self.friendship = collections.defaultdict(set)

  def postTweet(self, userId, tweetId):
    """
    Compose a new tweet.
    :type userId: int
    :type tweetId: int
    :rtype: void
    """
    tInfo = self.ts, tweetId, userId, len(self.tweets[userId])
    self.tweets[userId].append(tInfo)
    self.ts -= 1

  def getNewsFeed(self, userId):
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    :type userId: int
    :rtype: List[int]
    """
    ret = []
    heap = []
    if self.tweets[userId]:
      heapq.heappush(heap, self.tweets[userId][-1])

    for followeeId in self.friendship[userId]:
      if self.tweets[followeeId]:
        heapq.heappush(heap, self.tweets[followeeId][-1])
    cnt = 10
    while heap and cnt > 0: # not using nlargest()
      _, tid, uid, idx = heapq.heappop(heap)
      ret.append(tid)
      if idx > 0:
        heapq.heappush(heap, self.tweets[uid][idx - 1])
      cnt -= 1
    return ret

  def follow(self, followerId, followeeId):
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    if followerId == followeeId:
      return
    self.friendship[followerId] |= {followeeId}

  def unfollow(self, followerId, followeeId):
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    self.friendship[followerId] -= {followeeId}

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)