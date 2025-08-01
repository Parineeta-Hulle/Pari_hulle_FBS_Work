feet=int(input("Enter the feet:"))
inches =int(input("Enter the inches:"))

total_meters=(feet*0.3048) + (inches*0.0254)

meters = int(total_meters)
centimeter=(total_meters - meters)*100
print("meters",meters)
print("centimeters",centimeter)