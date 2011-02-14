from google.appengine.ext import webapp

import urllib
import time
import random
import hashlib
import hmac
import httplib
import binascii

class OAuthWayRemote(webapp.RequestHandler):
  def get(self):
    base_url = urllib.quote_plus("https://www.google.com/accounts/OAuthGetRequestToken")
    http_method = "GET"
    request_parameters = self.request_parameters()
    self.response.out.write(request_parameters)
    self.response.out.write("<br/>")
    signature_base_string = self.signature_base_string(http_method, base_url, request_parameters)
    self.response.out.write("signature base string in request is {0}".format(signature_base_string))
    self.response.out.write("<br/>")
    hmac_sha1 = hmac.new ('8ZIsnRdNjD6eBtQ1oTjlnosZ&',signature_base_string, hashlib.sha1)
    signature = urllib.quote_plus(binascii.b2a_base64(hmac_sha1.digest())[:-1])
    self.response.out.write("<hr/>")
    self.response.out.write(signature)
    self._get_request_token(signature)

  def _get_request_token(self, signature):
    https_connection = httplib.HTTPSConnection("www.google.com")
    oauth_headers = self._make_oauth_headers(signature)
    https_connection.request('GET',"/accounts/OAuthGetRequestToken?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Flatitude",{},headers=oauth_headers)
    http_response = https_connection.getresponse()
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(http_response.status)
    self.response.out.write("<br/>")
    self.response.out.write(http_response.read())
    

  def _make_oauth_headers(self,signature):
    headers = {'Authorization': 'OAuth oauth_callback="http%3A%2F%2Flocalhost%2FWAYRemote",oauth_consumer_key="wayremote.appspot.com",oauth_nonce="{0}",oauth_signature_method="HMAC-SHA1",oauth_signature="{1}",oauth_timestamp="{2}"'.format(self._oauth_nonce,signature,self._oauth_timestamp)}
    self.response.out.write("<hr/>")
    self.response.out.write(headers)
    self.response.out.write("<br/>")
    return headers
    

  def signature_base_string(self, http_method,request_baseurl, request_parameters):
    encoded_params = urllib.urlencode(request_parameters)
    encoded_params = urllib.quote(encoded_params)
    return http_method + "&" + request_baseurl + "&" + encoded_params

  def request_parameters(self):
    oauth_consumer_key = ("oauth_consumer_key", "wayremote.appspot.com")
    self._oauth_nonce = self.oauth_nonce()
    oauth_nonce = ('oauth_nonce',self._oauth_nonce)
    oauth_signature_method = ("oauth_signature_method", "HMAC-SHA1")
    self._oauth_timestamp = str(int(time.time()))
    oauth_timestamp = ("oauth_timestamp", self._oauth_timestamp)
    google_scope = ("scope", "https://www.googleapis.com/auth/latitude")
    oauth_callback = ("oauth_callback", "http://localhost/WAYRemote")
    req_params = [oauth_consumer_key, oauth_nonce, oauth_signature_method, oauth_timestamp, google_scope,oauth_callback]
    req_params.sort()
    return req_params
    

  def oauth_nonce(self):
    rand_dot_joined_string = '.'.join(str(random.randint(0,9)) for i in range(40))
    m = hashlib.md5()
    m.update(str(time.time()) + rand_dot_joined_string)
    return m.hexdigest()

