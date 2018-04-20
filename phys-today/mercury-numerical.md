# Numerical Simulations and General Relativity for High-School Students
## How you can introduce High-School Students to the basic concepts of numerical simulations and run their first computations including General Relativity -- in just one day

When I was in high-school, my biggest intrest were phenomena beyond the scope of what I currently knew.
Unfortunately, at this point, I did not yet have the theoretical toolset to dig deep.
But even though I was not able to compute things myself, I could grasp some insights of nature through visualisations.
With the growing availability of computational resources and accessibility to coding experience, it is a straight forward task to let students run their own simulations.
In this article we talk about our experience of teaching the basics of a numerical simulations in a playfull way to high-school students.
The working case is the planetary motion of mercury and the modifications to it's orbit coming from general relativity.
This example is particular motivating in the era where we have developed a new, additional sense for astronomical observations through gravitational waves, which has long been a source of fascination not only for trained physicists, but also for the general public.

This article is accompanied by a publication in which we describe the content of a one-day course.
The first idea for this course originates from a school project work in 2014 of one of the publications author, J. Heuer, when she was in 11th grade.
Which was eventually adapted and introduced as a course in the "Schülerakademie Teilchenphysik 2015" ("Student Academy for Particle Physics") which aims at high-school students from 10th to 13th grade.
It usually has about 25 participants, which come from all over Germany (during their vacations), and takes place biannually at the Science Center Overbach in Jülich.
During the four days of academy the students take part in different activities:
* lectures on various topics in particle physics,
* a tour of the particle accelerator COSY and 
* a visit to the high-performance computing facility at the Research Center Jülich.
At the end of the course, the last day is dedicated to hands-on work where studentes have three different choices: one choice being about coding numerical simulations for a physics system.


Figure 1: Image of course


The reason why it was desired to offer a course on numerical simulation is the relevance of simulations in active research.
Simulations are often the best method available for obtaining quantitative results in not only physics.
From NEURONS IN BIOLOGY OVER ATOMS IN CHEMISTRY THROUGH the descriptions of Quarks and Gluons through Lattice Quantum Chromodynamics.
However, in most school curricula, even though students learn about physics and can participate in classes on programming, both topics are seldom combined.
Albeit we see a big opportunity in this approach:
students can experience and experiment with physics systems that otherwise can only be studied theoretically, while, at the same time, they can pick up valuable skills in programming.

The basic outline of the course is at follows:
First, the students programm and visualize the orbit of mercury around the sun as it arises from classical newtonian mechanics.
Here they learn a basic concept of simulations: discretisation.
The orbit is derived by taking small but finite time steps and at each step calculating the position, velocity and acceleration from the one before using Newtons second law.
The students arrive at the typical elliptic curves, which are fixed in space.


Figure 2: Mercury orbit around the sun from newtonian gravity (GIF).


In particular the point of closest approach to the sun, the perihelion, does not move.
These closed curves are actually a consequence of the 1/r potential we have in newtonian gravity.
At this, point, we ask the students to play around with the discretization of time to see it's effect on the orbit and realize the importance of controlling numerical approximations.

To allow for movement of the perihelion the students need to modify the potential by including terms proportional to 1/r^2 and 1/r^3.
Because the actual perihelion motion due to general relativity is less than 42.3'' = 0.011° in a century (which is less than 10% of the total perihelion motion of mercury due to other planets in our solar system), we encourage students to play with the strength of these forces in order to visually observe changes to the orbit.
How would our observations change, if nature was slightly different?


Figure 3: Mercury orbit around the sun from newtonian gravity + general Relativity(GIF).


In the start of the course, we briefly introduce the students to the problem, motivate why it is interesting, summarize the to be used methods and formulate the goals.
The programming language of choice, Python, and the visualization module VPython come in handy because the general syntax and predefined classes can be written like pseudo-code.
Also, Python is also freeware and runs on all platforms.
Because not all students are generally familiar with the differential and vector calculus or programming languages, we spend roughly the first two hours with familiarizing them to these concepts.
This is done with a simple "Ball in the Box simulation" below you can see the full code as well as the output of the simulation.


Figure 4: "Ball in the Box" simulation and the fully working corresponding program.


The students, working in pairs of two, are encouraged to develop own ideas and experiment while we answer questions and guide the students through problems.
We supervise the activity of the students in groups of 1-3 and especially focus on students less familiar with the topic.
Usually, within the first hours, the students adjust to the setting, start to ask extended questions and play around with parameters to investigate their effect.
While all groups were able to visualise the perihelion motion, not all students where also able to extract the numerical value for the perihelion motion in case of enhanced forces from general relativity.
The final step is the comparison of the calculated value to the experimental one.
In order to do so, some students interpolated their results to the size where the strength of forces coming from General Relativity matches the values dictated by nature.
One point, that we could not sufficiently cover in the summer school, is the quantitative discussion of the (numerical) errors.

Furthermore it was very interesting to see, that the students had quite different interests.
While some pushed to solve increasingly difficult physical problems like including a third body and sometimes even tilting the planes of respective orbits, others where more interested in exploring the limits of their current simulation like preferably creating increasingly chaotic trajectories.
Others liked to improve upon their graphical delivery, like explicitly visualizing the position of the perihelion -- an idea we eventually picked up for later courses.
In the breaks we observed the students showing their simulations to students from other projects, also explaining their efforts motivations and results.

Due to these positive feedback we decided to make this course available to a broader public.
We believe this course is well suited to complement the standard curriculum and we hope it will help to inspire students to keep on learning about and exploring the fascinating physical phenomena that govern our world.









