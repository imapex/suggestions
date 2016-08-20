import os
import json
import requests
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel
from django.db import models

class ContentTypeAware(models.Model):
    def get_content_type(self):
        """:return: Content type for this instance."""
        return ContentType.objects.get_for_model(self)

    def get_content_type_id(self):
        """:return: Content type ID for this instance"""
        return self.get_content_type().pk

    def add_vote(self, vote_value):
        self.score += vote_value
        if vote_value == 1:
            self.ups += 1
        elif vote_value == -1:
            self.downs += 1

    class Meta:
        abstract = True


class MttpContentTypeAware(MPTTModel):
    def get_content_type(self):
        """:return: Content type for this instance."""
        return ContentType.objects.get_for_model(self)

    def get_content_type_id(self):
        """:return: Content type ID for this instance"""
        return self.get_content_type().pk

    class Meta:
        abstract = True


def create_spark_room(submission):
    """
    #If a submission get's more than X votes, let's open a spark room

    :param submission: submission object
    :return: response

    """
    url = os.environ.get('SPARK_URL', 'https://api.ciscospark.com/v1/')
    token = os.environ.get('SPARK_TOKEN', None)

    # Determine if the room is already created

    rooms_url = url + "rooms"
    messages_url = url + "messages"

    data = json.dumps({'title': submission.title })

    headers = {
        'authorization': "Bearer {}".format(token),
        'content-type': "application/json; charset=utf-8"
        }

    resp = requests.post(rooms_url, data=data, headers=headers)
    room_id = resp.json()['id']

    # TODO remove static URL reference
    intro = 'Based on high activity level @ the imapex suggestions site ' \
            'this room was automatically created to continue the conversation ' \
            'You can see the full history of the thread at [http://suggestions.imapex.io/comments/{}] ' \
            'heres a summary of the submission'.format(submission.pk)

    for m in [intro, submission.text]:
        # Send intro message
        data = json.dumps({'markdown': m,
                           'roomId': room_id})
        resp = requests.post(messages_url, data=data, headers=headers)
        print(resp.text)

