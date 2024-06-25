from web import start_app

'''
@Author: Claudia Landeira
'''
app = start_app() 

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=80, threads=100)