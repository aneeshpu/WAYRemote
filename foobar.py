from google.appengine.ext import webapp

class WayRemote(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type']='text/html'
    self.response.out.write("<html>")
    self.response.out.write("<head>")
    self.response.out.write('<meta name="google-site-verification" content="iuM_bUQzg_Qc9u3LbPAYKoomftjPikFD9sH4DZnv9WE" />')
    self.response.out.write("</head>")
    self.response.out.write("<body>")
    self.response.out.write("Hi this is WAY Remote fantastic")
    self.response.out.write("</body>")
    self.response.out.write("</html>")


