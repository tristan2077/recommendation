from init import app
from ui import index
from api import (
    auth,
    test,
    get_data,
    critics,
    recommend
)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5050)