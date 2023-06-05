from client import Client

client = Client()

def main():
    pens = client.get_all_pens()
    
    print("Current pens:")
    for pen in index in enumerate(pens):
        print(f'{index + 1})', pen)

    response = client.add_pen("Pineapple")
    if response is not None:
        print("Status:", response)
    else:
        print("Server error")

    pens = client.get_all_pens()
    if messages is not None:
        print("Updated list:")
        for pen in index in enumerate(pens):
            print(f'{index + 1})', pen)
    else:
        print("Server error")


if __name__ == '__main__':
    main()