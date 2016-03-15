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
            'ScheduleDelivery': ScheduleDelivery(['ProcessDelivery'], ['PickOrderFromHub']),
            'ProcessDelivery': ProcessDelivery(['SuccessfulDelivery', 'CustomerNotReachable', 'ReseduleDelivery'], ['PickOrderFromHub', 'ScheduleDelivery']),
            'SuccessfulDelivery': SuccessfulDelivery([], ['PickOrderFromHub', 'ScheduleDelivery', 'ProcessDelivery']),
            'CustomerNotReachable': CustomerNotReachable([], ['PickOrderFromHub', 'ScheduleDelivery', 'ProcessDelivery']),
            'ReseduleDelivery': ReseduleDelivery([], ['PickOrderFromHub', 'ScheduleDelivery', 'ProcessDelivery'])
        }
        self.root = self.flow['PickOrderFromHub']
        super(EcommerceWorkflow, self).__init__()
