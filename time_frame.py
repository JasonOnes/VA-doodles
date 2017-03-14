""" testing time_frame module (frequency?)"""


time_frame_rough = input("""How often would you like to invest? Daily, monthly,
                          quarterly, biannually, yearly: """)


#alternative time_frame using dicts
def time_frame(time_frame_rough):
    time_table = {"Daily": 365, "monthly": 12, "quarterly": 4, "biannually": 2,
                  "yearly": 1}
    if time_frame_rough in time_table:
        frequency = time_table[time_frame_rough]
    else:
        print("Sorry, not an option")
        frequency = None
    print(frequency)
    return frequency

time_frame(time_frame_rough) 
