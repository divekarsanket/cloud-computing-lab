import os
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render("./index.html", {"name": "Bob"}))

app = webapp2.WSGIApplication([("/", MainPage)], debug=True)
