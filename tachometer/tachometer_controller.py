from flash import Bluprint
from tachometer_controller import tachometer_api

tachometer_api = Bluprint('tachometer')

@tachometer_api.route('/', methods=['POST'])
def create_route_record():
    return 'Hello'
