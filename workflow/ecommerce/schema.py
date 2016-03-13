from steps import *
flow = {
    1: PickOrderFromHub(1, []),
    2: ScheduleDelivery(2, [1]),
    3: SuccessfulDelivery(3, [1,2]),
    4: CustomerNotReachable(4, [1,2]),
    5: ReseduleDelivery(5, [1,2])
}