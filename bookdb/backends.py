import logging
import datetime
import hashlib
import requests
from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPBindError

from django.conf import settings
from django.contrib.auth import get_user_model



logger = logging.getLogger(__name__)
UserModel = get_user_model()


class LDAPBackend:

    def authenticate(self, request, username=None, password=None, **kwargs):
        now = datetime.datetime.now()
        text = str(now.day) + 'ls@bBk3y'
        def computeMD5hash(my_string):
            m = hashlib.md5()
            m.update(my_string.encode('utf-8'))
            return m.hexdigest()
        # set username to lowercase for consistency
        username = username.lower()
        # get the bind client to resolve DN
        logger.info('authenticating %s' % username)

        '''
        try:
            print("begin connect!")
            # set your server
            server = Server("ldap://", port=389)
            
            #conn = Connection(server, f"{username}@{settings.LDAP_DOMAIN}", password=password, auto_bind=True, authentication=computeMD5hash(text).upper())
            #conn = Connection(server, user=username, password=password, auto_bind=True,
            #                  authentication=computeMD5hash(text).upper(), raise_exceptions=False)
            conn = Connection(server, user=username, password=password, auto_bind=True,)
            conn.open()
            conn.bind()
            print("connected")


        except LDAPBindError as e:
            logger.info('LDAP authentication failed')
            logger.info(e)
            return None'''
        try:
            #print("begin LDAP connect!")
            headers = {'Authorization': computeMD5hash(text).upper()}

            body = {"username": username, "password": password}

            response = requests.post(url="https://backpack.suss.edu.sg/REST/json/service/loginStaff", json=body, headers=headers)
            result = response.json()

            #print(result)

            if result['code'] != "OK":
                logger.info("Wrong Login Information")
                return None
            #print("connected")
        except Exception as e:
            print(e)
        user, created = UserModel.objects.get_or_create(username=username)

        #print(type(user))
        return user

    def get_user(self, user_id):
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None