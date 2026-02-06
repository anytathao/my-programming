def calculate_height(h0, t):
    g=9.8
    height=h0-0.5*g*t**2
    return round(height)

def calculate_car_distance(time_for_car):
        speed=20
        distance=speed*t
        return distance

if __name__=='__main__':
      h0= float(input("Enter a initial height in m: "))
      t= float(input("Enter the time elapsed(in seconds): "))
      time_for_car=float(input("Enter the time(in seconds): "))
      print(f"The height of the ball at the initial height of {h0} meters and at {t} second(s) is {{calculate_height(h0,t)}} meters")
      print(f"The car distance at the speed 20 m/s and at {time_for_car} second(s) is {{calculate_car_distance(time_for_car)}} meters")
