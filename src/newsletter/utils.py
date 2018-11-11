from django.conf import settings

# mailchimp
from mailchimp3 import MailChimp

# python3
import hashlib #import md5
import threading
import os


class SendSubscribeMail(object):
  def __init__(self, email, name):
    self.email = email
    self.name = name
    thread = threading.Thread(target=self.run, args=())
    thread.daemon = True                     
    thread.start()                                 

  def run(self):
    apiKey = os.environ['MAILCHIMP_API_KEY']
    username = os.environ['MAILCHIMP_USERNAME']
    listId = os.environ['MAILCHIMP_LIST_ID']

    client = MailChimp(mc_api=apiKey, mc_user=username)
    try:
     
      client.lists.members.create(listId, {
        'email_address': self.email,
        'status': 'pending',
        'merge_fields': {
          'FNAME': self.name,
        },
      })
      return True
    except:
      pass

    try:
      subscriberHash = hashlib.md5()
      subscriberHash.update(self.email.lower().encode('utf-8'))
      client.lists.members.update(list_id=listId, 
        subscriber_hash=subscriberHash.hexdigest(), 
        data={
          'status': 'pending',
          'merge_fields': {
            'FNAME': self.name,
          },
        })
      return True
    except:
      pass

    return False