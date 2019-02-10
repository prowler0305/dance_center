from dance_center import dance_center_app


if __name__ == '__main__':

    dance_center_app.run(debug=dance_center_app.config.get('DEBUG'), threaded=dance_center_app.config.get('THREADED'),
                         port=dance_center_app.config.get('PORT'), host=dance_center_app.config.get('HOST'))
