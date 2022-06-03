

# Table of Content
- [Table of Content](#table-of-content)
- [Description of the machine](#description-of-the-machine)
- [How it works](#how-it-works)
- [Capabilities of the system](#capabilities-of-the-system)
- [Performance of the system ](#performance-of-the-system)
- [Limitations of the system](#limitations-of-the-system)
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

# How it works

For the sorting subsystem, the user places a foam cube on the conveyor belt in front of the color sensor. The color sensor will read the cube’s color, and will instruct the sorting subsystem to rotate the conveyor belt so that the foam cube is in front of its appropriate bucket, and will then be kicked by the motor into
the bucket. The motor used to kick the cube will then retract back to its original position, and the processcan be done again until the bucket has been completely filled. Figure 4 shows a visual representation of this process.
<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/SortingAndDeliveryBot/main/Picture/Figure%204.PNG" width="800" height="400"/>
</p>
<p align="center">
Figure 4 : Flowchart of sorting subsystem
</p>

The bucket’s are designed so that there is an opening at the bottom that is large enough for one foam cube to pass through, with all other stored foam cubes placed on top of it. At the bottom of the bucket, behind it there is a motor that serves to push the cube out and into the delivery zone.

For the delivery subsystem, the user requests the desired colored cube by placing it in front of the color sensor. The color sensor will read the cube’s color, and the system will be instructed to push the appropriate cube out of the bucket through the opening described above and into the delivery area. The motor used to push the foam cube out will then retract back to its original position, which will allow the foam cube on top to replace the foam cube that has been pushed out, and the process can then be repeated until the buckets are empty . Figure 5 shows a visual representation of this process.

<p align="center">
<img src="https://raw.githubusercontent.com/rajanptl/SortingAndDeliveryBot/main/Picture/Figure%205.PNG" width="800" height="400"/>
</p>
<p align="center">
Figure 5 : Flowchart of delivery subsystem
</p>

# Capabilities of the system

The system is capable of sorting different coloured cubes with the use of the paper conveyor belt on top of
four wheels attached with one motor for movement. After the sorting has finished, the system is capable
of storing up to 6 cubes in three different bucket-like structures allocated to that colored cube. Also, the
system is capable of delivering any of the three coloured cubes that are requested with the help of another
color sensor.

# Performance of the system 
The system is quite performant in distinguishing between the three colors of cubes during the sorting
process. The system's sorting process is very fast and accurate at sorting the cubes in their allocated
buckets without failure. The system can hold up to 6 cubes of each color per bucket which is equivalent to
18 cubes in total. The delivery process is about 85% to 90% successful at delivering any colored cube
being requested. The total delivery time for a cube to be recognized by the color sensor and delivered to
the allocated area is very quick and done within less than 5 seconds. Overall the entire process of the
system consisting of sorting, storing and delivering are quick and fairly accurate. The time for one cube
being sorted and requested right after is done within less than 10 seconds in total (time varies for each
color). The system’s design is fairly simple so if it ever breaks or a component falls off, it is simple to
repair and to place the components correctly back in place.
# Limitations of the system 
Only one cube needs to be placed one at a time on the conveyor belt during the sorting phase. The
placement of the system on the base does take some time, it needs to be placed very precisely such that
every component aligns well. As mentioned, the delivery process is about 85% to 90% successful, the
system relies on the placement of the cubes in the buckets such that the kicking mechanism can deliver
the cubes smoothly without the obstruction of the cardboard funnel on the buckets. Another limitation is
that the system was built by only taking into account the size, weight and dimensions of the provided
cubes, which influenced the placement and speed of the kicking arms as well as the placement of the color
sensor used for sorting. Any other object placed on the system for sorting or delivery might not be as
effective.
# References
Special thanks to the TA's and the Professors from the course Design Principles and Methods in Winter 2022 for providing the SortingAndDeliveryBot folder and everything necessary for completing this project.
