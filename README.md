

# Table of Content
- [Table of Content](#table-of-content)
- [Description of the machine](#description-of-the-machine)
- [References](#references)

# Description of the machine
The design of the system can be seperated into two distinct subsystems: the sorting subsystem and the delivery subsystem. Each of these subsystems are connected to their own BrickPi, and work independently. As such, each subsystem has their own hardware design and software design. For the sorting subsystem, it uses a color sensor to read the foam cube’s cube so that it can know which bucket the cube needs to go into. There is also a conveyor belt that is used to move the cube in front of its respective bucket, and 3 kick motors that are used to push the cube into its respective motor. Finally, there are 3 buckets, one for the blue, green and red colored cubes. A picture of this subsystem can be viewed in Figure 1 for more information.
<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/SortingAndDeliveryBot/main/Picture/Figure%201.PNG" width="500" height="400" />
</p>
<p align="center">
Figure 1 : Picture of the final design of sorting subsystem
</p>
For the delivery subsystem, it uses a color sensor to read the client’s request so that it can know which cube to deliver into the delivery zone. There are also three motors, one for each bucket, that will push the appropriate cube out of the bottom of the bucket. The bucket is designed with a hole at the bottom, which lets out the cube at the very bottom. A picture of the inside and the outside of this subsystem can be viewed in Figure 2 and 3 for more information.
<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/SortingAndDeliveryBot/main/Picture/Figure%202.PNG" width="400" height="300" />
</p>
<p align="center">
Figure 2 : Picture of the final design of the delivery subsystem from the inside
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/SortingAndDeliveryBot/main/Picture/Figure%203.PNG" width="400" height="400" />
</p>
<p align="center">
Figure 3 : Picture of the final design of the delivery subsystem from the outside
</p>

# References
Special thanks to the TA's and the Professors from the course Design Principles and Methods in Winter 2022 for providing the SortingAndDeliveryBot folder and everything necessary for completing this project.
