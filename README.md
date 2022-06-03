

# Table of Content
- [Table of Content](#table-of-content)
- [Description of the machine](#description-of-the-machine)
- [References](#references)

# Description of the machine
The design of the system can be seperated into two distinct subsystems: the sorting subsystem and the delivery subsystem. Each of these subsystems are connected to their own BrickPi, and work independently. As such, each subsystem has their own hardware design and software design. For the sorting subsystem, it uses a color sensor to read the foam cube’s cube so that it can know which bucket the cube needs to go into. There is also a conveyor belt that is used to move the cube in front of its respective bucket, and 3 kick motors that are used to push the cube into its respective motor. Finally, there are 3 buckets, one for the blue, green and red colored cubes. A picture of this subsystem can be viewed in Figure 1 for more information.

# References
Special thanks to the TA's and the Professors from the course Design Principles and Methods in Winter 2022 for providing the SortingAndDeliveryBot folder and everything necessary for completing this project.
