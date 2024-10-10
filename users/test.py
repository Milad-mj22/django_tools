import imutils

import numpy as np
import cv2
im = np.random.rand(1920,1200)
cv2.imshow('a',im)
# cv2.waitKey(0)
import time
for i in range(1000):
    t1= time.time()

    im = imutils.rotate(image=im,angle=90)

    t2 =time.time()

    cv2.imshow('a',im)
    # cv2.waitKey(0)

    print(t2-t1)



                # Example of how to access and print the data
            # for mother in mother_materials:
            #     print(f"Mother Material: {mother.name}")
            #     print(f"Total Quantity: {mother.total_quantity}")

            #     # Loop through each raw material associated with the mother material
            #     for raw in mother.mother_material.all():  # Adjust if this is not the correct related name
            #         print(f"  Raw Material: {raw.name}, Total Quantity: {raw.total_quantity if raw.total_quantity else 0}")




            # Query to get each raw material and the sum of its quantity in the inventory
            # raw_materials = raw_material.objects.annotate(total_quantity=Sum('inventory__quantity')).order_by('name')

            # for material in raw_materials:
            #     print(f"Raw Material asdw: {material.name}, Total Quantity: {material.total_quantity}")





            # Query to get total quantity of each raw material per warehouse
            # warehouse_quantities = Inventory.objects.values('warehouse__name', 'inventory_raw_material__name').annotate(total_quantity=Sum('quantity')).order_by('warehouse__name', 'inventory_raw_material__name')

            # for item in warehouse_quantities:
            #     print(f"Warehouse: {item['warehouse__name']}, Raw Material: {item['inventory_raw_material__name']}, Total Quantity: {item['total_quantity']}")







            # Warehouse name to filter by
            # warehouse_name = 'خاقانی'

            # # Query to get total quantity of each raw material in the specified warehouse
            # warehouse_quantities = Inventory.objects.filter(warehouse__name=warehouse_name) \
            #     .values('inventory_raw_material__name') \
            #     .annotate(total_quantity=Sum('quantity'))

            # Output the quantities for the specified warehouse
            # for item in warehouse_quantities:
            #     print(f"Raw Material: {item['inventory_raw_material__name']}, Total Quantity: {item['total_quantity']}")


