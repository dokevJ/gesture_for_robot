import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import String

class GestureSubscriber(Node):

    def __init__(self):
        super().__init__("gesture_subscriber")
        self.subscription = self.create_subscription(
            String,
            'gesture_cmd',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rp.init(args=args)

    gesture_subscriber = GestureSubscriber()
    rp.spin(gesture_subscriber)

    gesture_subscriber.destroy_node()
    rp.shutdown()

if __name__ == '__name__':
    main()