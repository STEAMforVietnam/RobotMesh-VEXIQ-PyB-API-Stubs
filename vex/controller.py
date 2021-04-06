from .abstract import Device


class Controller(Device):
    """
    Use the controller class to get values from the remote controller
    as well as write to the controller's screen.
    """


class ControllerAxis:
    """
    Use the axis class to get values from one of the controller's joysticks.
    """


class ControllerButton:
    """
    Use the button class to get values from the controller's buttons.
    """
