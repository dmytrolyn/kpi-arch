from event_bus import EventBus

def main():
    event_bus = EventBus()

    EVENT_CREATE_USER = 'user_created'
    EVENT_CREATE_PRODUCT = 'product_created'

    def handle_user_created(user_data):
        print(f"User created: {user_data['name']}")

    def handle_product_created(product_data):
        print(f"Product created: {product_data['id']}")

    event_bus.subscribe(EVENT_CREATE_USER, handle_user_created)
    event_bus.subscribe(EVENT_CREATE_PRODUCT, handle_product_created)

    event_bus.notify(EVENT_USER_CREATED, {'name': 'Dmytro'})
    event_bus.notify(EVENT_ORDER_PLACED, {'id': '3738'})

if __name__ == "__main__":
    main()