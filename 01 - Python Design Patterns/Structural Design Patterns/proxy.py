import time


# Scenario: Only a fixed number of Producer artists can exist at a given time. The proxy (the artist)
# checks to see if the producer is available and is responsible for creating the producer objects.f

class Producer:
    """Define the 'resource-intensive' object to instantiate!"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


# A proxy object can be treated as a middleman to be used until the target object can be instantiated.
class Proxy:
    """"Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available ...")

        if self.occupied == 'No':
            # If the producer is available, create a producer object!
            self.producer = Producer()

            # Make the prodcuer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            print("Producer is busy!")

# Instantiate a Proxy
p = Proxy()

# Make the proxy: Artist produce until Producer is available
p.produce()

# Change the state to 'occupied'
p.occupied = "Yes"

# Make the Producer produce
p.produce()