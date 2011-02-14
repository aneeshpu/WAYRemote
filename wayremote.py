from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from foobar import WayRemote
from oauthwayremote import OAuthWayRemote

#class WayRemote(webapp.RequestHandler):
#  def get(self):
#    self.response.headers['Content-Type']='text/html'
#    self.response.out.write("<html>")
#    self.response.out.write("<head>")
#    self.response.out.write('<meta name="google-site-verification" content="iuM_bUQzg_Qc9u3LbPAYKoomftjPikFD9sH4DZnv9WE" />')
#    self.response.out.write("</head>")
#    self.response.out.write("<body>")
#    self.response.out.write("Hi this is WAY Remote")
#    self.response.out.write("</body>")
#    self.response.out.write("</html>")

application = webapp.WSGIApplication([('/',WayRemote),('/OAuth',OAuthWayRemote)],debug=True)
#application = webapp.WSGIApplication([('/address/(.*)/(.*)',WayRemote)],debug=True)

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
