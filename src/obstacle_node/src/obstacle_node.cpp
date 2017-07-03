#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sensor_msgs/LaserScan.h"

void scanValues(const sensor_msgs::LaserScan laser)
{
    //fprintf(stderr,"\n -------- size[%d] ---------- ", (int)laser.ranges.size());
    
    float m = 100;
    float thresh = 0.25;
    int ang = -1;

    for (unsigned int i=0; i<laser.ranges.size();i++)
    {
    	if(laser.ranges[i] < thresh)
	{
          if(laser.ranges[i] < m)
	  {
	    m = laser.ranges[i];
	    ang = i;
	  }
          // fprintf(stderr, "Obstacle detected at : %d degrees\n", i/2);
	}
       // fprintf(stderr, "range[%d]=[%f]: ", i, laser.ranges[i]);

    }
    if(ang != -1)
    {
      fprintf(stderr,"\nCLOSEST OBSTACLE AT: %d\n", ang/2);
    }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "obstacle_node");
  ros::NodeHandle n;
  ros::Rate r(2);
  while(ros::ok())
  {
    ros::Subscriber hokuyoSubscriber = n.subscribe("/scan", 1, scanValues);
    r.sleep();
  //  ros::Duration(10).sleep();
    ros::spinOnce();
  }
  return 0;
}
