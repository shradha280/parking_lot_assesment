import heapq
from collections import defaultdict, OrderedDict


class Car:
    def __init__(self, registration_number, age):
        self.registration_number = registration_number
        self.age = age

    def __str__(self):
        return "Car [registration_number=" + self.registration_number + ", age=" + self.age + "]"


class ParkingLot:
    def __init__(self, total_slots):
        self.registration_slot_mapping = dict()
        self.age_registration_mapping = defaultdict(list)
        # we need to maintain the orders of cars while showing 'status'
        self.slot_car_mapping = OrderedDict()

        # initialize all slots as free
        self.available_parking_lots = []
        # Using min heap as this will always give minimun slot number in O(1) time
        for i in range(1, total_slots + 1):
            heapq.heappush(self.available_parking_lots, i)

    def status(self):
        for slot, car in self.slot_car_mapping.items():
            print("Slot no: {} {}".format(slot, car))

    def get_nearest_slot(self):
        return heapq.heappop(self.available_parking_lots) if self.available_parking_lots else None

    def free_slot(self, slot_to_be_freed):
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = registration_no

        # Cleanup from all cache
        if found:
            del self.registration_slot_mapping[found]
            car_to_leave = self.slot_car_mapping[slot_to_be_freed]
            self.age_registration_mapping[car_to_leave.age].remove(found)
            del self.slot_car_mapping[slot_to_be_freed]
            print("leave ", slot_to_be_freed)
        

    def park_car(self, car):
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        self.slot_car_mapping[slot_no] = car
        self.registration_slot_mapping[car.registration_number] = slot_no
        self.age_registration_mapping[car.age].append(car.registration_number)

    # ● Registration numbers of all cars of a particular colour.
    def get_registration_nos_by_age(self, age):
        return self.age_registration_mapping[age]
    def get_age_by_slot(self, reg_no):
       for age,reno in self.age_registration_mapping.items():
        if reg_no in reno:
          # print('sxs',reno)
          #print(age)
          
          return age
       
       # return self.age_registration_mapping[reno]
    # ● Slot numbers of all slots where a car of a particular colour is parked.
    def get_slot_numbers_by_age(self, age):
        return [self.registration_slot_mapping[reg_no] for reg_no in self.age_registration_mapping[age]]
    def get_slot_numbers_by_rno(self, rno):
     # print(self.registration_slot_mapping)
      for reno,slot in self.registration_slot_mapping.items():
        if(reno==rno):
         
          return int(slot)
    def get_rno_by_slot_numbers(self, slot_num):
     
      for reno,slot in self.registration_slot_mapping.items():
        if(slot==int(slot_num)):
          
          return reno
       


if __name__ == "__main__":
  file_obj = open("input.txt", "r")

  for line in file_obj:
    ParkingList = line.split()
    if(ParkingList[0] == "Create_parking_lot"):
      parking_lot = ParkingLot(int(ParkingList[1]))
      print("Created parking of " +ParkingList[1]+ " slots")
    elif(ParkingList[0]=="Park"):
      car = Car(ParkingList[1], ParkingList[3])
      parking_lot.park_car(car)
      slot_nos = parking_lot.get_slot_numbers_by_rno(ParkingList[1])
      print("Car with vehicle registration number"+' "'+ ParkingList[1]+ '" '+"has been parked at slot number "+ str(slot_nos))
    # When no slots are available then
    #slot_no = parking_lot.get_nearest_slot()
    #print(slot_no)
    #slot_no = parking_lot.get_nearest_slot()
    #print(slot_no)

    # Leave slot no 4
    elif(ParkingList[0]== "Leave"):
      reg_nos = parking_lot.get_rno_by_slot_numbers(ParkingList[1])
      age = parking_lot.get_age_by_slot(reg_nos)
      slot_no_to_be_freed = ParkingList[1]
      parking_lot.free_slot(slot_no_to_be_freed)
      heapq.heappush(parking_lot.available_parking_lots, int(ParkingList[1]))
      
      print("Slot number " +ParkingList[1]+ " vacated, the car with vehicle registration number"+' "'+str(reg_nos)+ '" '+"left the space, the driver of the car was of age " + str(age ))
   
    elif(ParkingList[0]=="Slot_number_for_car_with_number"):
      slot_nos = parking_lot.get_slot_numbers_by_rno(ParkingList[1])
      print(slot_nos)
      
      # print(ParkingList[1].format(slot_nos))

    elif(ParkingList[0]=="Slot_numbers_for_driver_of_age"):
      slot_nos = parking_lot.get_slot_numbers_by_age(ParkingList[1])
      print(*slot_nos, sep = ",") 

    elif(ParkingList[0]=="Vehicle_registration_number_for_driver_of_age"):
      registration_numbers = parking_lot.get_registration_nos_by_age(ParkingList[1])
     # print(ParkingList[1].format(registration_numbers))

  file_obj.close()
 
