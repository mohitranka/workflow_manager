"""
Schema for ecommerce workflow
"""
from steps import *
from ..baseworkflow import BaseWorkflow


class EcommerceWorkflow(BaseWorkflow):
    """Class to manage the workflow for ecommerce
    """

    def __init__(self):
        self.flow = {
            'PickOrderFromHub': PickOrderFromHub(['ScheduleDelivery'], []),
            'ScheduleDelivery': ScheduleDelivery(['SuccessfulDelivery', 'CustomerNotReachable', 'ReseduleDelivery'], ['PickOrderFromHub']),
            'SuccessfulDelivery': SuccessfulDelivery([], ['PickOrderFromHub', 'ScheduleDelivery']),
            'CustomerNotReachable': CustomerNotReachable([], ['PickOrderFromHub', 'ScheduleDelivery']),
            'ReseduleDelivery': ReseduleDelivery([], ['PickOrderFromHub', 'ScheduleDelivery'])
        }
        self.root = self.flow['PickOrderFromHub']
        super(EcommerceWorkflow, self).__init__()
