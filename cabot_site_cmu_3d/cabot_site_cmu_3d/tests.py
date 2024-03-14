def config(tester):
    tester.config['init_x'] = -5.0
    tester.config['init_y'] = 0.0
    tester.config['init_z'] = 0.0
    tester.config['init_a'] = 90.0
    tester.config['init_floor'] = 3


def checks(tester):
    tester.check_topic_error(
        topic="/cabot/activity_log",
        topic_type="cabot_msgs/msg/Log",
        condition="msg.category=='cabot/interface' and msg.text=='vibration' and msg.memo=='unknown'"
    )


def wait_ready(tester):
    tester.wait_localization_started()
    # tester.wait_ready()


def test8_door_goal_and_manual_back(tester):
    tester.reset_position(x=10, a=0)
    tester.goto_node('EDITOR_node_1490112635059')
    tester.wait_goal("NavGoal")
    tester.wait_for(seconds=1)
    tester.button_down(3)
    tester.reset_position(x=20, a=0)
    tester.button_down(4)
    tester.wait_navigation_completed()


def test7_door_goal(tester):
    tester.reset_position(x=10, a=0)
    tester.goto_node('EDITOR_node_1490112635059')
    tester.wait_goal("NavGoal")
    tester.reset_position(x=16.5, a=0)
    tester.wait_navigation_completed()


def test6_pause_and_resume(tester):
    tester.reset_position()
    tester.goto_node('EDITOR_node_1495220208195')
    tester.wait_for(7)
    tester.info("push left button to pause")
    tester.button_down(3)
    tester.wait_for(7)
    tester.info("push right button to resume")
    tester.button_down(4)
    tester.wait_navigation_completed()


def test5_sending_another_goal(tester):
    tester.reset_position()
    tester.goto_node('EDITOR_node_1495220343136')
    tester.wait_for(7)
    tester.goto_node('EDITOR_node_1495220208195')
    tester.wait_navigation_completed()


def test4_sending_another_goal_while_changing_heading_at_goal(tester):
    tester.reset_position()
    tester.goto_node('EDITOR_node_1495220343136@180')
    tester.wait_navigation_arrived()
    tester.goto_node('EDITOR_node_1495220208195')
    tester.wait_navigation_completed()


def test3_check_navigation_events(tester):
    tester.reset_position()
    tester.goto_node('EDITOR_node_1495220343136@180')
    tester.check_navigation_arrived()  # do not wait
    tester.check_turn_towards()        # do not wait
    tester.wait_navigation_completed()


def test2_navigate_twice(tester):
    tester.reset_position()
    tester.goto_node('EDITOR_node_1495220343136')
    tester.wait_navigation_arrived()
    tester.goto_node('EDITOR_node_1495220208195')
    tester.wait_navigation_arrived()


def test1_cancel_navigation_and_another_navigation(tester):
    tester.reset_position()
    tester.goto_node('EDITOR_node_1495220210524')
    tester.wait_for(10)
    tester.cancel_navigation()
    tester.wait_for(10)
    tester.goto_node('EDITOR_node_1495563142750')
    tester.wait_navigation_arrived()


def test0_navigation_to_a_goal(tester):
    tester.reset_position()
    tester.goto_node('EDITOR_node_1495563142750')
    tester.wait_navigation_arrived()
