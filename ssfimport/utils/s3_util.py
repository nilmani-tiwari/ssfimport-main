# coding=utf-8

import os

import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key as s3Key
from django.conf import settings


class S3Base(object):
    def __init__(self, bucket_name=None):
        self.conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        if not bucket_name:
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        self.bucket = self.conn.lookup(bucket_name)

    def upload_file(self, file_name, file_object, folder_name=None, content_type=None, public=False):
        """

        Args:
            file_name (str):
            file_object ():
            folder_name (str):
            content_type (str):
            public (bool):

        Returns:

        """

        if folder_name:
            key_name = os.path.join(folder_name, file_name)
        else:
            key_name = file_name

        key = self.bucket.new_key(key_name)  # type: s3Key

        if content_type:
            key.set_metadata('content-type', content_type)

        key.set_contents_from_file(file_object)

        if public:
            key.make_public()

        return key

    def delete_file(self, file_name, folder_name=None):

        if folder_name:
            key_name = os.path.join(folder_name, file_name)
        else:
            key_name = file_name

        return self.bucket.delete_key(key_name)

    def get_file_content(self, file_name, folder_name):
        key_name = os.path.join(folder_name, file_name)
        k = self.bucket.get_key(key_name)

        return k.get_contents_as_string()


class TmpPicsHandler(object):
    tmp_folder = settings.S3_TMP_DIR
    org_tmp_folder = settings.S3_TMP_DIR + "/org"

    def __init__(self, file_name):
        self.conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        # self.bucket = self.conn.lookup(settings.AWS_STORAGE_BUCKET_NAME)
        self.key_name = os.path.join(self.org_tmp_folder, file_name)

    def upload_temp_pic(self, pic, image_type):
        self.delete_tmp_pic()
        mp = self.bucket.initiate_multipart_upload(self.key_name)
        key = mp.upload_part_from_file(pic, part_num=1)

        mp.complete_upload()

        key.set_metadata('Content-Type', image_type)
        key.set_acl('public-read')

        return key.name, key.generate_url(expires_in=0, query_auth=False)

    def delete_tmp_pic(self):
        return self.bucket.delete_key(self.key_name)


def push_file_to_s3(file_name, bucket_name, make_public=False):
    """
    :param bucket_name:
    :param file_name:
    :param make_public:
    :return: :rtype:
    """

    doc_url = ''
    try:
        conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(bucket_name)
        k = s3Key(bucket, file_name)
        k.set_contents_from_filename(file_name)
        if make_public:
            k.make_public()
        doc_url = k.generate_url(120 * 24 * 60 * 60)
        os.remove(file_name)
    except Exception as e:
        logger.exception(e)

    return doc_url
