import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class GesturePublisher(Node):

    def __init__(self):
        super().__init__('gesture_publisher')
        self.publisher_ = self.create_publisher(String, 'hand_gesture', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.example = ['wait','turn', 'heart', 'stop']

    def timer_callback(self):
        msg = String()
        msg.data = self.example[self.i]
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)
        self.i += 1
        if self.i > 3:
            self.i = 0

def main(args=None):
    rclpy.init(args=args)

    gesture_publisher = GesturePublisher()

    rclpy.spin(gesture_publisher)
    gesture_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__name__':
    main()