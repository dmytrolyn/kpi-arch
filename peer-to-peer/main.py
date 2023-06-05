import socket

class Peer:
    def __init__(self, name):
        self.name = name
        self.peers = []

    def add_peer(self, peer):
        if peer not in self.peers:
            if peer.establish_connection(self):
                self.peers.append(peer)
                self.notify_connection_established(peer)

    def establish_connection(self, peer):
        print(f"{peer.name} is establishing a connection with {self.name}")

        if peer not in self.peers:
            print(f"{self.name} accepted connection with {peer.name}")
            self.peers.append(peer)
            self.notify_connection_established(peer)
            return True

    def notify_connection_established(self, peer):
        print(f"{self.name} is now connected to {peer.name}")

    def send_message(self, peer, message):
        peer.receive_message(self, message)

    def receive_message(self, peer, message):
        if peer in self.peers:
            print(f"{self.name} received a message from {peer.name}: {message}")
        else:
            print(f"{peer.name} is not connected to {self.name}")

if __name__ == "__main__":
    peer1 = Peer("Peer 1")
    peer2 = Peer("Peer 2")
    peer3 = Peer("Peer 3")

    peer1.add_peer(peer2)
    peer1.add_peer(peer3)

    peer1.send_message(peer2, "Hello")
    peer2.send_message(peer1, "Hello World")
    peer2.send_message(peer3, "Hello World!")