import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
class BasicSubscriber(Node):
    
    def __init__(self):
        super().__init__('sum_calculator')
        self.subscription = self.create_subscription(Int64,'natural_number_signal',self.listener_callback,1)
        self.sum1 = 1
        self.subscription
        




    def listener_callback(self, msg):
        if msg.data <=0:
            msg.data = 1
        else :
            self.sum1 *=msg.data

        self.get_logger().info('Received: "%d"' % self.sum1)



def main(args=None):
    rclpy.init(args=args)
    basic_subcriber = BasicSubscriber()
    rclpy.spin(basic_subcriber)
    basic_subcriber.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()