class BusinessLayer:
    def __init__(self, data_layer):
        self.data_layer = data_layer

    def get_data(self):
        return self.data_layer.fetch_data()