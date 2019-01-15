# TIE-02107: Programming 1: Introduction
# Solution of Task - 12.3
# A program works as routing protocol simulator
"""
group members:
    prasun biswas(267948)
    Mahbub hasan(281749)
"""



class Router:
    def __init__(self, Router_name):
        self.name = Router_name
        self.neighbours = []
        self.networks = {}

    def add_neighbour(self, neighbour):
        """neighbour to list of neighbour
        """
        if neighbour.name not in self.neighbours:
            self.neighbours.append(neighbour.name)
            self.neighbours.sort()

    def add_network(self, network, distance):
        """Adds network and distance in the routing table
        """
        self.networks[network] = distance

    def print_info(self):
        """Prints router info"""
        print(f'  {self.name}')
        print('    N:', end='')
        if self.neighbours:
            print(' ' + ', '.join(self.neighbours))
        else:
            print('')

        networks = [f'{k}:{v}' for k, v in sorted(self.networks.items())]

        print('    R:', end='')
        if self.networks:
            print(' ' + ', '.join(networks))
        else:
            print('')

    def receive_routing_table(self, router):
        """ receives routing table from a router
        """
        for network, distance in router.networks.items():
            # Only if the network doesn't exist in current routing table or
            # current distance is more than new info then add the new info
            if (network not in self.networks or
                    self.networks[network] > distance + 1):
                self.networks[network] = distance + 1

    def has_route(self, network):
        """Prints routing info to a network
        """
        try:
            distance = self.networks[network]
            if distance == 0:
                print('Router is an edge router for the network.')
            else:
                print(f'Network {network} is {distance} hops away')
        except KeyError:
            print('Route to the network is unknown.')


class RouterSimulator:
    def __init__(self):
        self.routers = {}

    def read_from_file(self, filename):
        """ Reads a file and and adds routers accordingly
        """
        with open(filename, 'r') as f:
            for line in f.read().splitlines():
                name, neighbours, r_table = line.split('!')

                self.add_new(name)
                if neighbours:
                    for neighbour in neighbours.split(';'):
                        try:
                            self.add_neighbours(name, neighbour)
                        except Exception as e:

                            pass
                if r_table:
                    for network in r_table.split(';'):
                        net_name, distance = network.split(':')

                        distance = int(distance)
                        self.add_network(name, net_name, distance)

    def add_new(self, name):
        """ Adds a new router
        """
        if name not in self.routers:
            self.routers[name] = Router(name)
            return True
        return False

    def add_neighbours(self, router1, router2):
        """ Adds two routers as neighbours of each other
        """
        router1 = self.routers[router1]
        router2 = self.routers[router2]

        router1.add_neighbour(router2)
        router2.add_neighbour(router1)

    def add_network(self, router, network, distance):
        """ Adds a network to a router
        """
        self.routers[router].add_network(network, distance)

    def send(self, name):
        """ Send routing table to neighbours of the router named 'name'"""
        router = self.routers[name]
        for neighbour in router.neighbours:
            neighbour = self.routers[neighbour]
            neighbour.receive_routing_table(router)

    def has_route(self, name, network):
        router = self.routers[name]
        router.has_route(network)

    def print_info(self, name):
        self.routers[name].print_info()

    def print_all(self):
        for name, router in sorted(self.routers.items()):
            router.print_info()


def print_router(router_simulator):
    """Asks for a router name and prints it's info
    """
    name = input('Enter router name: ')
    try:
        router_simulator.print_info(name)
    except KeyError:
        # the router was not found. Hence KeyError was raised
        print('Router was not found.')


def connect(router_simulator):
    """Asks for two router name and connects them

    """
    router1 = input('Enter 1st router: ')
    router2 = input('Enter 2nd router: ')
    try:
        router_simulator.add_neighbours(router1, router2)
    except KeyError:
        print('Router was not found.')


def send(router_simulator):
    """Asks for router name and send it's routing table to all neighbors
    """
    router = input('Sending router: ')
    try:
        router_simulator.send(router)
    except KeyError:
        print('Router was not found.')


def new_network(router_simulator):
    """Asks for a new network info and adds it to the specified router adds a new new network from
    """
    router = input('Enter router name: ')
    network = input('Enter network: ')
    try:
        distance = int(input('Enter distance: '))
    except ValueError:
        print('Distance not valid.')
        return

    try:
        router_simulator.add_network(router, network, distance)
    except KeyError:
        print('Router was not found.')


def receive(router_simulator):
    """Receives command from the user
    """
    while True:
        command = input("> ")
        command = command.upper()

        if command == "P":
            print_router(router_simulator)

        elif command == "PA":
            router_simulator.print_all()

        elif command == "S":
            send(router_simulator)

        elif command == "C":
            connect(router_simulator)

        elif command == "RR":
            name = input('Enter router name: ')
            network = input('Enter network name: ')
            router_simulator.has_route(name, network)

        elif command == "NR":
            name = input('Enter a new name: ')
            added = router_simulator.add_new(name)
            if not added:
                print('Name is taken.')

        elif command == "NN":
            new_network(router_simulator)

        elif command == "Q":
            print("Simulator closes.")
            return

        else:
            print("Erroneous command!")
            print("Enter one of these commands:")
            print("NR (new router)")
            print("P (print)")
            print("C (connect)")
            print("NN (new network)")
            print("PA (print all)")
            print("S (send routing tables)")
            print("RR (route request)")
            print("Q (quit)")


def main():
    router_simulator = RouterSimulator()

    routerfile = input("Network file: ")
    if routerfile:
        try:
            router_simulator.read_from_file(routerfile)
        except Exception as e:
            print("Error: the file could not be read or", end='')
            print("there is something wrong with it.")
            return

    receive(router_simulator)


main()
