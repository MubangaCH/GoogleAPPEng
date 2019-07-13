import webapp2

def Geometric_mean(numbers):
    
    product = 10*numbers
    '''
    for i in numbers:
        if i < 0:
            print("Your data contains negative number(s). The geometric mean may not be meaningful")

        else:   
            product *= i
    '''
    geometric_mean = (product)**(1/2)
        
    if product == 0:
        print(" Your data contains a zero(s). Please remove the zero(s) or look up to treat zeros in geometric means")
           
    #else:    
        #print('The geometeric mean of your data is', geometric_mean)
    
    return str(geometric_mean)


class MainPage(webapp2.RequestHandler):
    def get(self):
        numbers = self.request.get("pos_nums")
        Geo_mean = Geometric_mean(numbers)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Geometric mean calculator</title></head>
            <body>
              <form action="/" method="get">
                Enter positive number greater than zero: <input type="text"
                                        name="pos_nums" value={}>
                <input type="submit" value="Convert"><br>
                Your geometric mean is : {}
              </form>
            </body>
          </html>""".format(numbers, Geo_mean))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)
