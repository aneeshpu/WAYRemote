from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class WayRemote(webapp.RequestHandler):
  def get(self,latitude, longitude):
    self.response.headers['Content-Type']='text/plain'
    self.response.out.write("Hi this is WAY and latitude is " + latitude + " and longitude is " + longitude)

application = webapp.WSGIApplication([('/address/(.*)/(.*)',WayRemote)],debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
