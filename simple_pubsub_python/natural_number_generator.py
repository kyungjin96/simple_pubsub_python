import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
class BasicPublisher(Node):
    
    def __init__(self):
        super().__init__('natural_number_genertor')
        self.publisher_ = self.create_publisher(Int64, 'natural_number_signal', 1)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = Int64()
        msg.data = self.count
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    basic_publisher = BasicPublisher()
    rclpy.spin(basic_publisher)
    basic_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()