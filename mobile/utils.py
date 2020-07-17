SERVER_URI = 'http://data-dive.com:9999/'
#SERVER_URI = 'http://cloudcb.herokuapp.com/'

def show_error(req, error):
    print(
        "Errors: %s" % error,
        "Request: %s" % req.__dict__,
        "This seems unusual. Please file a bug report with above details",
        "at https://github.com/krsoninikhil/cloud-clipboard/issues"
    )
