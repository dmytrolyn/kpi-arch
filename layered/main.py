from layers import DataLayer, BusinessLayer, PresentationLayer

def main():
    data_layer = DataLayer()
    business_logic = BusinessLayer(data_layer)
    presentation = PresentationLayer(business_logic)

    presentation.display_data()

if __name__ == '__main__':
    main()